# SOP 01: Content engine Google Drive folder

Owner: Bosi.
Applies to: every organic content engine we set up, for Kongwa Bakes or any other brand.
Version: 1.0, 18 October 2026.

---

## 1. When to use this

The moment we start an organic content engine for a brand, before any filming, scraping or generating.

One brand, one folder.

No loose files in "My Drive".

---

## 2. Create the folder

Name it exactly:

`<Brand Name> Organic Content Engine`

Inside it, create these six subfolders, numbered so they always sort in workflow order:

| # | Folder | What goes in it | Who adds it |
|---|---|---|---|
| 01 | Reference Videos | Other brands' videos we are learning from. Analysis only, never reposted. One subfolder per format (for example `pause-challenge`, `gotcha-switch`, `cake-reveal`). | Research (Claude or Bosi) |
| 02 | Raw Videos | Our own unedited footage straight off the phone, plus any AI bait drafts before editing. | Whoever filmed it |
| 03 | Edited Videos | Finished verticals. A clean master (no captions) and a captioned version of each. | Editor (Claude or Bosi) |
| 04 | Feedback | One note per video: Bosi's review, what to change, the decision (approve, edit, kill). | Bosi |
| 05 | Audios | Our own stings (Gotcha, Psych, whoosh), voiceovers, licensed music from TikTok's Commercial Music Library, ElevenLabs sound effects. Never other creators' audio. | Editor |
| 06 | Winners | Copies of the posts that beat the winner bar (section 5), with their numbers, so we can recreate them. | Claude, every Monday review |

Add a Google Doc at the top level called `00 SOP: How this folder works` with a copy of this SOP, so anyone opening the folder knows the rules.

Folders we may add later (not yet): `07 Photos`, `08 Covers and thumbnails`, `09 Scripts`.

---

## 3. File naming

Every file follows one pattern, so search and sorting just work:

`YYYY-MM-DD_<concept-slug>_<what>_v<NN>.<ext>`

Examples:

- `2026-10-19_pause-croissant-slice_raw-01.mov`
- `2026-10-19_pause-croissant-slice_master_v01.mp4`
- `2026-10-19_pause-croissant-slice_captioned_v02.mp4`
- `2026-10-19_pause-croissant-slice_feedback.md`
- `2026-10-18_wantsandneeds_bugatti-gotcha_ref.mp4` (references: date posted, account, slug)

Lower case, hyphens inside words, underscores between parts.

Never overwrite a version.

Bump `v01` to `v02`.

---

## 4. The flow

1. **Reference** goes in `01`, with a line in `research/examples.jsonl` (link, plays, account median, multiple of median).
2. **Raw** footage goes in `02` the same day it is filmed. Filmed vertical, 4K if the phone allows, 30fps, kitchen light, and a 3 second hold at the start and end of every shot.
3. **Edit** goes in `03`. Export 1080x1920, H.264, 30fps, around -14 LUFS. Both clean master and captioned version.
4. **Feedback** goes in `04`. Bosi writes approve, edit or kill, plus the reason. Nothing is posted until it says approve.
5. **Post** through Postiz. TikTok first, Instagram Reels the same day, YouTube Shorts with a keyword title.
6. **Measure** every Monday. Anything over the winner bar is copied to `06`.

---

## 5. The winner bar

A post is a winner if it hits **any one** of these within 7 days of posting:

- 3 times or more our own account median plays for that month on that platform;
- top 10% of our posts that month for shares plus saves per 1,000 plays;
- a confirmed order where the customer named that post or "saw it on TikTok or Instagram".

When a post wins, save into `06 Winners`:

- the captioned video;
- a `_winner.md` note with the date, platform, plays, average watch time, shares, saves, comments, profile visits, link clicks, orders, and the account median at the time;
- one line on why we think it won, labelled THINK, so we never confuse a guess with the data.

Every month, the top 3 winners get remade as a new variant (new bake, same mechanic).

---

## 6. Rules that apply to every file in the folder

- No em-dash characters in any caption, script or note.
- Real food only in the product half of any video. AI only for the bait, the setting and the motion.
- Reference videos are never reposted or used as AI input with an identifiable person in them.
- Any stock image used as AI input is logged in `references/stock/LICENSES.csv` in the repo with its licence URL and the date checked.

---

## 7. Kongwa Bakes folder (created 18 October 2026)

- Main folder: [Kongwa Bakes Organic Content Engine](https://drive.google.com/drive/folders/1qD_0Tu4fJnloDNFYZyZsqoB7K-COp0Jx)
- [01 Reference Videos](https://drive.google.com/drive/folders/1VomN5JliBZ-RF2w8xScRI9U6YYhu1hnc)
- [02 Raw Videos](https://drive.google.com/drive/folders/1BsCUkUU3VZgc_keHQYTXUAPRdQn5qQf3)
- [03 Edited Videos](https://drive.google.com/drive/folders/1nLHn6UpLMNQXTe1s-Y9SXWHxc4k2RHsN)
- [04 Feedback](https://drive.google.com/drive/folders/1_UxGAKfKZT9Dj9Id6UINyrhQFi14lGO8)
- [05 Audios](https://drive.google.com/drive/folders/1uBjgnAIswLEvP-jSNx5Lj_p8eY_CjHqB)
- [06 Winners](https://drive.google.com/drive/folders/1C6xSRcnTDTva62lJKKmMCN54zG-c10iH)
