import json,re,sys
J=json.load(open(sys.argv[1]))
def nums(s):
    out=[]
    for m in re.finditer(r'\$\s?(\d{2,3}(?:,\d{3})+|\d{2,3}(?:\.\d)?\s?[kK])',s):
        v=m.group(1).replace(',','').replace(' ','')
        out.append(float(v[:-1])*1000 if v[-1] in 'kK' else float(v))
    return [x for x in out if 20000<x<1000000]
keep=[];nosal=[]
for j in J:
    if j.get('closed'): continue
    if 'criteria' not in j: continue
    et=j['criteria'].get('Employment type','')
    if et and et!='Full-time': continue
    s=' '.join([j['li_salary'],j['card_salary']]+j['desc_salaries'])
    n=nums(s); j['max']=max(n) if n else 0; j['min']=min(n) if n else 0
    (keep if j['max']>=125000 else nosal).append(j)
keep.sort(key=lambda j:-j['max'])
for j in keep:
    print(f"{j['id']} | {j['company'][:28]} | {j['title'][:60]} | {j['location'][:25]} | {j['posted']} | {j['li_salary'] or j['card_salary'] or j['desc_salaries'][:2]} | lvl={j['criteria'].get('Seniority level','')} | hyb={j['hybrid']} | geo={bool(j['geo_restrict'])}")
print(len(keep),'with salary>=125k;',len(nosal),'without/low', file=sys.stderr)
