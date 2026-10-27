# Workflow: Creative Crossroads podcast episode edit (Descript)

First run: Steve Riach | Eterne Films Podcast (Oct 2026). Notes here feed a future skill.

## 1. Trigger
A Zoom interview recording (gallery view) is in Descript, possibly split into parts.

## 2. Steps
1. Read the transcript (export_transcript) and list off-air sections: pre-show, mid-show breaks, "let me rephrase", post-show. Cut with *ignore* (restorable).
2. Fix misheard names in the transcript (text correction only). Seen so far: "Attorney Films" -> "Eterne Films".
3. Work on a duplicated composition ("<name> - Edit v1"), never the original.
4. Ben runs speaker detection in the Descript app (the connector can't) and names the speakers.
5. Agent Underlord builds layouts from the PNG frames:
   - Two speakers (CC-16x9-two-speakers-square.png): opening, rapid back-and-forth, goodbye.
   - Solo (CC-16x9-<name>.png): whoever is speaking; the speaker's half of the gallery view, zoomed ~2x.
   - Interjections under ~2s don't trigger a switch.
6. Captions: Poppins Bold 72px, white, active word #F7941D, one line, bottom of frame.
7. Ben reviews in the app (Underlord can't hear audio or see captions in its preview).

## 3. Gotchas learned
- Check for stray audio tracks before editing. An extra copy of Part 2 sat unmuted on its own track from 0:00 and caused double audio.
- For two-speaker crops, the second video layer must use the SAME source file at the SAME timecode as the script, and must be muted.
- Speaker detection is not available through the connector.
- Cost: about 125 Descript AI credits for a full 55-min episode across 5 Underlord runs (trims+captions ~23, layout rollout ~46).

## 4. Judgment calls (Ben)
Framing approval, which segments stay (e.g. the book-trailer segment stayed, sponsor/summit mentions cut), final review before publishing.

## 5. Never
Publish or share the episode without Ben's OK.
