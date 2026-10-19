# Kongwa Bakes organic content engine

The official Kongwa Bakes organic content engine: research, concepts, templates and weekly drafts for faceless, real-food short-form video that leads to orders.

## Start here

| What | Where |
|---|---|
| The brief | `docs/05-CLAUDE-CODE-CONTENT-ENGINE-PROMPT.md` |
| Bosi's editing, hook and analytics bar | `docs/house-standards.md` |
| Everything on kongwabakes.com (products, prices, rules, brand) | `docs/website-context.md` |
| Drive folder SOP | `sops/SOP-01-content-engine-drive-folder.md` |
| What works, with numbers | `research/summary.md` |
| Ranked concepts | `concepts/backlog.md` |
| This week's drafts for review | `out/2026-W43/REVIEW.md` |

## Folders

```
docs/                 brief, house standards, website context
sops/                 standard operating procedures
research/             examples.jsonl (99), notes, summary, raw scrapes
concepts/             backlog.md, one folder per concept that needs notes
references/website/   screenshots and text of every page
references/videos/    third-party reference videos (analysis only, not committed)
assets/library/       real Kongwa Bakes photos and video, indexed in library.json
assets/brand/         KB monogram, labels, Fraunces and Mulish fonts (OFL)
templates/            ffmpeg and Python assembly recipes
out/YYYY-Www/         finished drafts, captions.json, REVIEW.md
generations/log.csv   every AI generation and quote
metrics/              weekly metrics
scripts/              checks (em-dash)
```

## Templates

| Template | Makes | Needs |
|---|---|---|
| `templates/pause-challenge.sh` | video pause challenge or meme over real footage, seamless loop | a real clip |
| `templates/photo_pause.py` | photo pause challenge with a sweeping ring and a hidden reward frame | a real photo |
| `templates/pause_roulette.py` | real bakes cycling with name and price ("wherever you pause...") | real photos |
| `templates/overlay.py` | shared overlay: KB label, hook card, order chip, target outline, all in the safe zone | |

All templates use the brand fonts and colours, render 4K (2160x3840) plus a 1080 phone copy and a cover, and keep text inside the safe zone (x 70 to 900, y 250 to 1530).

## Google Drive

[Kongwa Bakes Organic Content Engine](https://drive.google.com/drive/folders/1qD_0Tu4fJnloDNFYZyZsqoB7K-COp0Jx): 01 Reference Videos, 02 Raw Videos, 03 Edited Videos, 04 Feedback, 05 Audios, 06 Winners.

## Rules

Run `scripts/check-emdash.sh` before every commit.
Nothing is posted without Bosi's approval.
