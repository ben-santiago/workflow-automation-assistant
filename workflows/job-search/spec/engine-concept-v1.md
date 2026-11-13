# Engine spec piece: concept, copy and Magnific prompts (v1, draft for Ben's review)

Spec concept by Ben Santiago. Not produced for or approved by Engine.

## Facts used (all from Engine's public pages and press; recheck on engine.com before sending)
- Engine Groups is a free tool for group hotel bookings.
- Each event gets a dedicated event page attendees book from, and organizers see bookings in real time on a dashboard.
- Engine either lets attendees self-book curated hotels or negotiates a room block for larger groups (about 10+ rooms).
- There's no booking fee for group booking support; Engine is commission-funded.
- Business features: DirectBill, travel policy enforcement, Approvals, consolidated billing, 24/7 live support, and 750,000+ hotels.
- Flex and FlexPro let travelers change or cancel when plans change.

Sources: [Lodging Magazine](https://lodgingmagazine.com/engine-debuts-new-features-for-group-travel-planning/), [Business Wire](https://www.businesswire.com/news/home/20260722586063/en/Engine-Reimagines-Group-Travel-with-New-Suite-of-Free-Tools-for-Events-of-Any-Size), [Engine group bookings](https://engine.com/groups), [Engine corporate travel](https://engine.com/book-corporate-travel), [Engine blog: choosing a group platform](https://engine.com/blog/how-to-choose-group-travel-booking-platform)

## Concept territory: "The offsite, minus the spreadsheet"
Everyone who has planned a team trip knows the spreadsheet: who's coming, who booked, which hotel,
who's paying. Engine replaces it with one event page, one room block, and one view of who's booked.
The territory is the relief of handing that off.

## Three hooks (one per buyer)

| | Hook A: Team lead | Hook B: Travel or ops manager | Hook C: Finance lead |
|---|---|---|---|
| Who | The person "voluntold" to plan the offsite | Owns travel for the company | Approves the spend |
| Pain | Planning on top of their real job | Chasing 40 people for booking status | Receipts, policy exceptions, surprise bills |
| Headline | You got voluntold to plan the offsite. | 40 people. One link. Zero reply-alls. | One offsite. One bill. |
| Support line | Engine finds the hotels and sets up the room block. Your team books from one page. | Send one event page. Everyone books in the block. You watch it fill in real time. | Room blocks, travel policy and billing in one place, with no booking fee for group support. |
| CTA | Plan your offsite free | Set up a group trip | See how group booking works |

**Format rules**
- **1:1 and 4:5:** headline + support line + CTA button. Headline 6 words max where possible.
- **9:16:** headline in the top third, support line mid-frame, CTA above the bottom safe zone (keep the bottom ~250px and top ~220px clear for platform UI).
- **Optional "proof card"** for Hook B: a simple designed card ("Q1 Offsite · 32 of 40 rooms booked") as a graphic, not a fake screenshot of Engine's product.

**Brand:** Ben, pull Engine's colors and type from engine.com, or give Claude Design the URL and ask it to match. I couldn't open engine.com from here, so I haven't guessed their palette.

## Magnific prompts

**Locked style block (paste at the end of every prompt):**
> editorial lifestyle photography, natural daylight, warm neutral palette with clean whites and soft wood tones, 35mm lens, shallow depth of field, candid and unposed, modern business-casual wardrobe, diverse group of adults, no logos, no text, no signage, generous empty space for a headline

Generate each plate at **4:5 and 9:16**; the 1:1 can be cropped from the 4:5.

**Plate 1, Hook A (team lead):**
> a small team of coworkers arriving together in a bright modern hotel lobby, rolling carry-on suitcases, two people laughing mid-conversation, one checking a phone, calm and relieved mood, empty wall space in the upper third of the frame, [STYLE BLOCK]

**Plate 2, Hook B (travel or ops manager):**
> over-the-shoulder view of a professional at a clean desk holding a smartphone with a blank screen facing the camera, laptop softly out of focus, bright airy office, relaxed confident posture, empty space on the right side of the frame, [STYLE BLOCK]
>
> *(The blank screen is where the designed "32 of 40 rooms booked" card goes in Claude Design.)*

**Plate 3, Hook C (finance lead):**
> top-down flat lay of a tidy wooden desk with a single folded invoice, a pen, a coffee cup and a closed laptop, orderly and minimal, soft morning light, large empty area across the top half, [STYLE BLOCK]

**Plate 4, hero and backup for any hook:**
> a team of twelve coworkers sharing a long dinner table on a boutique hotel terrace at golden hour, string lights, candid laughter, plates being passed, wide shot with open sky in the upper third, [STYLE BLOCK]

**If a render breaks:** keep the style block, simplify the scene sentence, and regenerate before changing the style. Watch hands and phone screens closely, and reject any render with garbled text or fake logos.

## Build order in Claude Design (Nov 19)
1. Set up brand: Engine colors and type (from the URL), plus a CTA button style.
2. Build Hook A in 4:5 first and lock the layout.
3. Duplicate it to 1:1 and 9:16, then swap in Hooks B and C. That's 9 ads.
4. Add a cover page with the concept line and the spec label. Ads stay clean, with no label on each one.

## Open questions for Ben
- Keep "voluntold"? It's playful and good for a scroll-stopping hook, but it may be too casual for Engine's voice.
- Group travel or Engine X (their business card) as the territory? Group travel has more public detail to work from, so I'd stay with it.
