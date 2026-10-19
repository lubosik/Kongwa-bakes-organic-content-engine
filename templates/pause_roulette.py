#!/usr/bin/env python3
"""Pause roulette: real bake photos cycling a few times a second, each with its real name and price.
"Wherever you pause is your Saturday order." Loops seamlessly (the cycle is a whole number of photos).

Usage:
  templates/pause_roulette.py OUT_BASENAME --hook "..." --item PHOTO "Name" "£0.00" [--item ...]
"""
import argparse
import os
import subprocess
import sys
import tempfile

from PIL import Image, ImageDraw, ImageFilter, ImageFont

sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from photo_pause import BRAND, HERE, cover, write_ticks  # noqa: E402


def label(draw, name, price, s, y):
    """Name and price pill under the card, centred in the safe zone."""
    nf = ImageFont.truetype(os.path.join(BRAND, "fonts", "Fraunces-SemiBold.ttf"), int(54 * s))
    pf = ImageFont.truetype(os.path.join(BRAND, "fonts", "Mulish-SemiBold.ttf"), int(44 * s))
    text_w = draw.textlength(name, font=nf) + 24 * s + draw.textlength(price, font=pf)
    pad = 34 * s
    h = 96 * s
    x0 = 485 * s - text_w / 2 - pad
    draw.rounded_rectangle([x0, y, x0 + text_w + 2 * pad, y + h], radius=h / 2, fill=(0xFB, 0xF3, 0xE2, 240))
    draw.text((x0 + pad, y + 14 * s), name, font=nf, fill=(0x2E, 0x1C, 0x12, 255))
    draw.text((x0 + pad + draw.textlength(name, font=nf) + 24 * s, y + 24 * s), price, font=pf,
              fill=(0xC1, 0x5B, 0x33, 255))


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("out")
    ap.add_argument("--hook", required=True)
    ap.add_argument("--wrap", type=int, default=18)
    ap.add_argument("--item", nargs=3, action="append", metavar=("PHOTO", "NAME", "PRICE"), required=True)
    ap.add_argument("--hold", type=int, default=7, help="frames per photo at 30 fps (7 = about 4 a second)")
    ap.add_argument("--loops", type=int, default=2, help="times through the list")
    ap.add_argument("--scale", type=float, default=2)
    ap.add_argument("--card-y", type=int, default=600)
    ap.add_argument("--chip", default="orders close Thursday 5pm")
    ap.add_argument("--ticks", action="store_true")
    a = ap.parse_args()

    s = a.scale
    W, H = int(1080 * s), int(1920 * s)
    fps = 30
    n = len(a.item) * a.hold * a.loops
    dur = n / fps

    with tempfile.TemporaryDirectory() as tmp:
        ovl = os.path.join(tmp, "overlay.png")
        subprocess.run([sys.executable, os.path.join(HERE, "overlay.py"), ovl, "--scale", str(s),
                        "--hook", a.hook, "--wrap", str(a.wrap), "--chip", a.chip,
                        "--font", os.path.join(BRAND, "fonts", "Fraunces-SemiBold.ttf"),
                        "--font-italic", os.path.join(BRAND, "fonts", "Fraunces-SemiBoldItalic.ttf"),
                        "--chip-font", os.path.join(BRAND, "fonts", "Mulish-SemiBold.ttf"),
                        "--logo", os.path.join(BRAND, "kb-monogram-1024-transparent.png")], check=True)
        overlay = Image.open(ovl).convert("RGBA")

        # One finished frame per item: blurred fill, square card, name and price pill, overlay.
        frames = []
        cw = int(1080 * s)
        for photo, name, price in a.item:
            im = Image.open(photo).convert("RGB")
            bg = cover(im, W, H).filter(ImageFilter.GaussianBlur(40 * s))
            bg = Image.blend(bg, Image.new("RGB", bg.size, (20, 14, 10)), 0.35).convert("RGBA")
            card = cover(im, cw, cw)
            bg.paste(card, (0, int(a.card_y * s)))
            # Above the order chip, inside the safe zone (y 250 to 1530).
            label(ImageDraw.Draw(bg), name, price, s, 1300 * s)
            bg.alpha_composite(overlay)
            frames.append(bg.convert("RGB").tobytes())

        audio = []
        if a.ticks:
            wav = os.path.join(tmp, "ticks.wav")
            write_ticks(wav, dur, bpm=fps * 60 / a.hold)
            audio = ["-i", wav]
        else:
            audio = ["-f", "lavfi", "-t", str(dur), "-i", "anullsrc=r=48000:cl=stereo"]
        out = a.out + "_captioned.mp4"
        p = subprocess.Popen(["ffmpeg", "-nostdin", "-v", "error", "-y", "-f", "rawvideo", "-pix_fmt", "rgb24",
                              "-s", f"{W}x{H}", "-r", str(fps), "-i", "-", *audio, "-map", "0:v", "-map", "1:a",
                              "-af", "loudnorm=I=-14:TP=-1.5:LRA=11", "-c:v", "libx264", "-profile:v", "high",
                              "-pix_fmt", "yuv420p", "-crf", "17", "-preset", "slow", "-c:a", "aac", "-b:a", "320k",
                              "-ar", "48000", "-movflags", "+faststart", "-t", str(dur), out], stdin=subprocess.PIPE)
        for i in range(n):
            p.stdin.write(frames[(i // a.hold) % len(frames)])
        p.stdin.close()
        if p.wait():
            raise SystemExit("ffmpeg failed")

    subprocess.run(["ffmpeg", "-nostdin", "-v", "error", "-y", "-i", out, "-vf", "scale=1080:1920:flags=lanczos",
                    "-c:v", "libx264", "-crf", "19", "-preset", "slow", "-maxrate", "6M", "-bufsize", "12M",
                    "-pix_fmt", "yuv420p", "-c:a", "copy", "-movflags", "+faststart", a.out + "_captioned-1080.mp4"],
                   check=True)
    subprocess.run(["ffmpeg", "-nostdin", "-v", "error", "-y", "-i", out, "-frames:v", "1", "-q:v", "2",
                    a.out + "_cover.jpg"], check=True)
    print("wrote", out, f"({dur:.2f}s)")


if __name__ == "__main__":
    main()
