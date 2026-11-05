"""LinkedIn guest job search: remote US, recent postings, creative leadership titles.
Usage: python3 -I li_search.py <outdir> [time_filter e.g. r604800]
Writes <outdir>/results.json with one entry per unique job id.
"""
import html, json, re, subprocess, sys, time, urllib.parse

OUT = sys.argv[1]
TPR = sys.argv[2] if len(sys.argv) > 2 else "r1209600"  # 14 days
KEYWORDS = [
    "Creative Director", "Associate Creative Director", "Head of Creative",
    "Creative Lead", "Director of Creative Operations", "Creative Operations Director",
    "Director of Brand Design", "Brand Creative Director", "Director Brand Creative",
    "Director of Brand and Creative", "Creative Systems", "AI Creative Director",
    "AI Creative Lead", "Senior Creative Manager", "Head of Brand Design",
    "Creative Strategy Director", "Director of Content and Creative",
    "Director Marketing Creative", "Creative Technology Director",
    "Director of Creative Production", "Design Director Marketing",
    "Creative Automation", "Director of Creative", "Brand Design Director",
]
TITLE_RE = re.compile(r"creative|brand design|design director|art director", re.I)
EXCLUDE_TITLE = re.compile(r"intern|freelance|contract|part[- ]time|copywriter|ux|product design|associate,? creative services|coordinator|specialist|assistant(?! creative)", re.I)


def get(url):
    r = subprocess.run(["curl", "-sS", "--max-time", "25", "-A", "Mozilla/5.0", url],
                       capture_output=True, text=True)
    return r.stdout


def clean(s):
    return re.sub(r"\s+", " ", html.unescape(re.sub(r"<[^>]+>", " ", s))).strip()


jobs = {}
for kw in KEYWORDS:
    for start in (0, 25, 50):
        q = urllib.parse.urlencode({"keywords": kw, "location": "United States", "f_WT": "2",
                                    "f_TPR": TPR, "start": start})
        page = get("https://www.linkedin.com/jobs-guest/jobs/api/seeMoreJobPostings/search?" + q)
        cards = page.split('data-entity-urn="urn:li:jobPosting:')[1:]
        if not cards:
            break
        for c in cards:
            jid = c.split('"')[0]
            title = clean(re.search(r'base-search-card__title">(.*?)</h3>', c, re.S).group(1)) if 'base-search-card__title' in c else ""
            comp = re.search(r'base-search-card__subtitle">(.*?)</h4>', c, re.S)
            loc = re.search(r'job-search-card__location">(.*?)</span>', c, re.S)
            date = re.search(r'datetime="([^"]+)"', c)
            sal = re.search(r'job-search-card__salary-info">(.*?)</span>', c, re.S)
            if jid in jobs:
                continue
            jobs[jid] = dict(id=jid, title=title, company=clean(comp.group(1)) if comp else "",
                             location=clean(loc.group(1)) if loc else "",
                             posted=date.group(1) if date else "",
                             card_salary=clean(sal.group(1)) if sal else "",
                             url=f"https://www.linkedin.com/jobs/view/{jid}/", kw=kw)
        time.sleep(0.7)

cands = [j for j in jobs.values() if TITLE_RE.search(j["title"]) and not EXCLUDE_TITLE.search(j["title"])]
print(f"{len(jobs)} total, {len(cands)} title matches", file=sys.stderr)

money = re.compile(r"\$\s?\d{2,3}(?:,\d{3})+(?:\.\d+)?\s*(?:-|–|to)\s*\$?\s?\d{2,3}(?:,\d{3})+|\$\s?\d{2,3}(?:\.\d)?\s?[kK]\s*(?:-|–|to)\s*\$?\s?\d{2,3}(?:\.\d)?\s?[kK]")
for j in cands:
    d = get(f"https://www.linkedin.com/jobs-guest/jobs/api/jobPosting/{j['id']}")
    text = clean(re.sub(r"(?s)<(script|style)[^>]*>.*?</\1>", " ", d))
    j["closed"] = "No longer accepting applications" in text
    crit = dict(re.findall(r'description__job-criteria-subheader">\s*(.*?)\s*</h3>\s*<span[^>]*>\s*(.*?)\s*</span>', d, re.S))
    j["criteria"] = {k.strip(): clean(v) for k, v in crit.items()}
    sal = re.search(r'compensation__salary">(.*?)</div>', d, re.S)
    j["li_salary"] = clean(sal.group(1)) if sal else ""
    j["desc_salaries"] = sorted(set(m.group(0) for m in money.finditer(text)))[:6]
    apply_ = re.search(r'https?://[^"\s]*(?:greenhouse|lever|ashbyhq|workday|rippling|smartrecruiters|workable|icims|jobvite)[^"\s]*', html.unescape(d))
    j["offsite_apply"] = apply_.group(0) if apply_ else ""
    j["texas_mentions"] = [m.group(0) for m in re.finditer(r".{0,120}\b(Texas|TX)\b.{0,120}", text)][:3]
    j["geo_restrict"] = [m.group(0) for m in re.finditer(r".{0,100}(not eligible|unable to hire|cannot hire|only (?:hire|accept)|following states|residents of).{0,160}", text, re.I)][:3]
    j["hybrid"] = bool(re.search(r"\bhybrid\b|in[- ]office|days a week in", text, re.I))
    j["desc"] = text[:4000]
    time.sleep(0.7)

json.dump(cands, open(f"{OUT}/results.json", "w"), indent=1)
