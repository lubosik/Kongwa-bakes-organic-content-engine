#!/usr/bin/env python3
"""Render every meme in concepts/memes/memes.json with templates/meme.py, then write captions.json
and a contact sheet for review.

Usage: templates/render_memes.py [OUT_DIR] [--only MEME-01,MEME-07]
"""
import argparse
import json
import os
import subprocess
import sys

from PIL import Image, ImageDraw, ImageFont

HERE = os.path.dirname(os.path.abspath(__file__))
ROOT = os.path.join(HERE, "..")
LIB = os.path.join(ROOT, "assets", "library", "website")
CHARACTERS = {
    "cow": {"file": "chubby-cow-dance-alpha-v1.webm", "h": 1500, "x": 640, "bottom": 2010},
    "seagull": {"file": "fat-seagull-waddle-alpha-v1.webm", "h": 1800, "x": 640, "bottom": 2330},
}
SIGN_OFF = {
    "order": "Orders close Thursday 5pm.\nCollection or local delivery in Medway, Saturday 8am to midday.\nORDER at the link in bio.",
    "cakes": "Celebration cakes need 10 days.\nTell us about yours at the link in bio.",
    "catering": "Events need 14 days.\nTell us what you need at the link in bio.",
    "starter": "Starting a starter? Our free guide is on kongwabakes.com/sourdough/starter-guide/",
    "default": "Real bakes from our family kitchen in Medway.\nOrders close Thursday 5pm, link in bio.",
}
TAGS = {
    "home bakers": ["#sourdough", "#sourdoughstarter", "#bakingmemes", "#sourdoughmemes"],
    "home bakers and locals": ["#sourdough", "#bakingmemes", "#medway", "#kentbakery"],
    "locals": ["#medway", "#kentbakery", "#bakingmemes", "#rochester"],
    "cake buyers": ["#birthdaycake", "#medway", "#kentbakery", "#bakingmemes"],
    "office managers": ["#officetreats", "#medway", "#kentbakery", "#fridayfeeling"],
}


def contact_sheet(rows, out_dir):
    tw, th = 270, 480
    cols = 6
    n = len(rows)
    sheet = Image.new("RGB", (cols * tw, ((n + cols - 1) // cols) * (th + 30)), "white")
    d = ImageDraw.Draw(sheet)
    font = ImageFont.load_default()
    for i, (mid, cover) in enumerate(rows):
        im = Image.open(cover).convert("RGB").resize((tw, th))
        x, y = (i % cols) * tw, (i // cols) * (th + 30)
        sheet.paste(im, (x, y))
        d.text((x + 6, y + th + 8), mid, fill="black", font=font)
    path = os.path.join(out_dir, "contact-sheet.jpg")
    sheet.save(path, quality=82)
    return path


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("out_dir", nargs="?", default=os.path.join(ROOT, "out", "memes-v1"))
    ap.add_argument("--only", default="")
    a = ap.parse_args()
    os.makedirs(a.out_dir, exist_ok=True)
    memes = json.load(open(os.path.join(ROOT, "concepts", "memes", "memes.json")))
    only = set(filter(None, a.only.split(",")))
    captions, sheet = [], []
    for m in memes:
        base = os.path.join(a.out_dir, f"{m['id']}_{m['slug']}")
        if not only or m["id"] in only:
            cmd = [sys.executable, os.path.join(HERE, "meme.py"), os.path.join(LIB, m["photo"]), base,
                   "--text", m["text"], "--dur", str(m.get("dur", 6 if "photo2" in m else 5))]
            if "photo2" in m:
                cmd += ["--photo2", os.path.join(LIB, m["photo2"]), "--text2", m["text2"]]
            if m.get("character"):
                c = CHARACTERS[m["character"]]
                path = os.path.join(ROOT, "assets", "characters", c["file"])
                if not os.path.exists(path):
                    print(f"skip {m['id']}: character {c['file']} not ready")
                    continue
                cmd += ["--character", path, "--char-h", str(c["h"]), "--char-x", str(c["x"]),
                        "--char-bottom", str(c["bottom"])]
            if m.get("steps"):
                cmd += ["--steps", str(m["steps"])]
            if m.get("eyes"):
                cmd += ["--eyes", m["eyes"], "--look", m.get("look", "side")]
            subprocess.run(cmd, check=True)
        if os.path.exists(base + "_cover.jpg"):
            sheet.append((m["id"], base + "_cover.jpg"))
            cta = m.get("cta", "default")
            captions.append({
                "id": m["id"], "file": os.path.basename(base) + "_captioned.mp4",
                "audience": m["audience"], "format": m["format"],
                "on_screen": m["text"] + (f" / {m['text2']}" if "text2" in m else ""),
                "caption": m["caption"] + "\n\n" + SIGN_OFF[cta],
                "hashtags": TAGS[m["audience"]], "location": "Medway",
                "ai_label": bool(m.get("character")), "destination_cta": cta,
                "check": m.get("check", ""),
            })
    json.dump(captions, open(os.path.join(a.out_dir, "captions.json"), "w"), indent=2, ensure_ascii=False)
    print("contact sheet:", contact_sheet(sheet, a.out_dir))


if __name__ == "__main__":
    main()
