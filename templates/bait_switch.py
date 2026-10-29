#!/usr/bin/env python3
"""Bait-and-switch: bait clip up to the peak of tension, glitch, hard cut, real bakes, end card.

Structure (house standards 2, brief 7.2):
  bait 0..CUT   hook text and a small KB label from frame 1, optional doorbell-cam HUD, rising drone
  CUT           4-frame glitch, dead air, then a boom on the first product frame
  product       3 to 5 real photos, about 1.6s each, slow push, switch line held across all of them
  end card      KB monogram, one line, CTA

Our own sound design is synthesised here (nothing to license); add the trending sound in the app.

Usage:
  templates/bait_switch.py BAIT.mp4 OUT_BASENAME --cut 7.5 --hook "..." --switch "..." \
      --shot photo.jpg [--shot ...] [--hud doorbell] [--end "..."] [--cta "..."]
"""
import argparse
import math
import os
import struct
import subprocess
import sys
import tempfile
import wave

import numpy as np
from PIL import Image, ImageDraw, ImageFilter, ImageFont, ImageOps

sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from meme import text_box  # noqa: E402
from photo_pause import BRAND  # noqa: E402

W, H, FPS = 1080, 1920, 30
SAFE_X0, SAFE_X1, SAFE_Y0, SAFE_Y1 = 70, 900, 250, 1530
FRAUNCES = os.path.join(BRAND, "fonts", "Fraunces-SemiBold.ttf")
FRAUNCES_I = os.path.join(BRAND, "fonts", "Fraunces-SemiBoldItalic.ttf")
MULISH = os.path.join(BRAND, "fonts", "Mulish-SemiBold.ttf")
LOGO = os.path.join(BRAND, "kb-monogram-1024-transparent.png")


def logo(size):
    im = Image.open(LOGO).convert("RGBA")
    return im.resize((size, int(im.height * size / im.width)), Image.LANCZOS)


def hud_doorbell(stamp, cam="FRONT DOOR"):
    """Our own doorbell-camera overlay: timestamp, camera name, REC dot. Drawn here, never by the AI model."""
    im = Image.new("RGBA", (W, H), (0, 0, 0, 0))
    d = ImageDraw.Draw(im)
    f = ImageFont.truetype("/usr/share/fonts/truetype/dejavu/DejaVuSansMono.ttf", 34)
    d.text((SAFE_X0, 262), stamp, font=f, fill=(255, 255, 255, 230))
    d.text((SAFE_X0, 306), cam, font=f, fill=(255, 255, 255, 200))
    d.ellipse([SAFE_X1 - 40, 268, SAFE_X1 - 14, 294], fill=(230, 40, 40, 255))
    d.text((SAFE_X1 - 120, 262), "LIVE", font=f, fill=(255, 255, 255, 230))
    # vignette corners like a fisheye doorbell lens
    vig = Image.new("L", (W, H), 0)
    ImageDraw.Draw(vig).ellipse([-260, -200, W + 260, H + 200], fill=255)
    vig = vig.filter(ImageFilter.GaussianBlur(120))
    dark = Image.new("RGBA", (W, H), (0, 0, 0, 170))
    dark.putalpha(Image.eval(vig, lambda v: int((255 - v) * 0.67)))
    im.alpha_composite(dark)
    return im


def cover_crop(img, w, h, focus=(0.5, 0.5)):
    r = max(w / img.width, h / img.height)
    img = img.resize((math.ceil(img.width * r), math.ceil(img.height * r)), Image.LANCZOS)
    x = int((img.width - w) * focus[0])
    y = int((img.height - h) * focus[1])
    return img.crop((x, y, x + w, y + h))


def switch_card(text):
    """Switch line: brand serif, white with soft shadow, top of the safe zone (the product sits below)."""
    im = Image.new("RGBA", (W, H), (0, 0, 0, 0))
    lines, f = [], ImageFont.truetype(FRAUNCES, 70)
    d = ImageDraw.Draw(im)
    words, cur = text.split(), ""
    for w_ in words:
        t = (cur + " " + w_).strip()
        if d.textlength(t, font=f) > SAFE_X1 - SAFE_X0:
            lines.append(cur)
            cur = w_
        else:
            cur = t
    lines.append(cur)
    sh = Image.new("RGBA", (W, H), (0, 0, 0, 0))
    ds = ImageDraw.Draw(sh)
    y = SAFE_Y0 + 20
    for line in lines:
        x = (SAFE_X0 + SAFE_X1) / 2 - d.textlength(line, font=f) / 2
        ds.text((x, y + 4), line, font=f, fill=(0, 0, 0, 170))
        d.text((x, y), line, font=f, fill=(255, 255, 255, 255))
        y += 82
    sh = sh.filter(ImageFilter.GaussianBlur(9))
    # soft dark gradient behind the line so it reads on bright frosting
    grad = Image.new("L", (1, H), 0)
    for yy in range(H):
        grad.putpixel((0, yy), int(150 * max(0.0, 1 - max(0, yy - (y + 40)) / 260)) if yy < y + 300 else 0)
    shade = Image.new("RGBA", (W, H), (20, 14, 10, 255))
    shade.putalpha(grad.resize((W, H)))
    shade.alpha_composite(sh)
    sh = shade
    sh.alpha_composite(im)
    lg = logo(96)
    sh.alpha_composite(lg, (SAFE_X0 + 10, SAFE_Y1 - lg.height - 10))
    return sh


def end_card(line, cta):
    im = Image.new("RGB", (W, H), (0x2E, 0x1C, 0x12))
    lg = logo(300)
    im.paste(lg, ((W - lg.width) // 2, 640), lg)
    d = ImageDraw.Draw(im)
    f1 = ImageFont.truetype(FRAUNCES_I, 64)
    f2 = ImageFont.truetype(MULISH, 40)
    # wrap the line inside the safe zone, then the CTA underneath
    words, rows, cur = line.split(), [], ""
    for w_ in words:
        t = (cur + " " + w_).strip()
        if d.textlength(t, font=f1) > SAFE_X1 - SAFE_X0:
            rows.append(cur)
            cur = w_
        else:
            cur = t
    rows.append(cur)
    y = 1010
    for row in rows:
        d.text(((W - d.textlength(row, font=f1)) / 2, y), row, font=f1, fill=(0xFB, 0xF3, 0xE2))
        y += 80
    d.text(((W - d.textlength(cta, font=f2)) / 2, y + 30), cta, font=f2, fill=(0xE3, 0x9A, 0x3B))
    return im


def synth_audio(path, cut, total, rate=48000):
    """Rising drone and heartbeat under the bait, dead air at the cut, a boom on the switch."""
    n = int(total * rate)
    t = np.arange(n) / rate
    out = np.zeros(n)
    bait = t < cut
    prog = np.clip(t / cut, 0, 1)
    drone = (0.18 + 0.5 * prog ** 2) * (np.sin(2 * np.pi * (55 + 40 * prog ** 2) * t)
                                         + 0.5 * np.sin(2 * np.pi * (82 + 70 * prog ** 3) * t))
    # heartbeat, speeding up towards the cut
    beat = np.zeros(n)
    tt, k = 0.6, 0.0
    while k < cut - 0.2:
        idx = int(k * rate)
        L = int(0.12 * rate)
        env = np.exp(-np.arange(L) / (0.025 * rate))
        seg = env * np.sin(2 * np.pi * 48 * np.arange(L) / rate)
        beat[idx:idx + L] += seg[: max(0, min(L, n - idx))]
        k += max(0.28, tt * (1 - 0.6 * k / cut))
    out[bait] = 0.35 * drone[bait] + 0.9 * beat[bait]
    # fade the last 2 frames of the bait to silence, then 0.12s of dead air
    fade = (t > cut - 0.07) & (t < cut)
    out[fade] *= np.linspace(1, 0, fade.sum())
    hit = int((cut + 0.12) * rate)
    L = int(1.6 * rate)
    k_ = np.arange(L) / rate
    boom = np.exp(-k_ / 0.35) * np.sin(2 * np.pi * (42 + 60 * np.exp(-k_ / 0.05)) * k_)
    end = min(n, hit + L)
    out[hit:end] += 1.2 * boom[: end - hit]
    out = np.clip(out / max(1e-9, np.abs(out).max()) * 0.9, -1, 1)
    pcm = (out * 32767).astype(np.int16)
    with wave.open(path, "wb") as w:
        w.setnchannels(2)
        w.setsampwidth(2)
        w.setframerate(rate)
        w.writeframes(np.repeat(pcm[:, None], 2, axis=1).tobytes())


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("bait")
    ap.add_argument("out")
    ap.add_argument("--cut", type=float, required=True, help="seconds into the bait clip: the peak, just before the reveal")
    ap.add_argument("--bait-start", type=float, default=0)
    ap.add_argument("--hook", required=True)
    ap.add_argument("--switch", required=True)
    ap.add_argument("--shot", action="append", required=True, help="real bake photo; add 3 to 5")
    ap.add_argument("--shot-s", type=float, default=1.6)
    ap.add_argument("--hud", choices=["none", "doorbell"], default="none")
    ap.add_argument("--stamp", default="31/10/2026  21:47:12")
    ap.add_argument("--end", default="halloween treats from our family kitchen")
    ap.add_argument("--cta", default="ORDER at the link in bio")
    ap.add_argument("--end-s", type=float, default=2.0)
    ap.add_argument("--cam", default="FRONT DOOR", help="camera name in the HUD for the first bait shot")
    ap.add_argument("--then", action="append", default=[], metavar="FILE|START|END|CAM[|STAMP]",
                    help="further bait shots, hard-cut in order; the switch happens at the END of the last one")
    a = ap.parse_args()

    segs = [(a.bait, a.bait_start, a.cut, a.cam, a.stamp)]
    for spec in a.then:
        f, st, en, cam, *stamp = spec.split("|")
        segs.append((f, float(st), float(en), cam, stamp[0] if stamp else a.stamp))
    cut = sum(seg[2] - seg[1] for seg in segs)
    with tempfile.TemporaryDirectory() as tmp:
        parts = []
        for si, (src, st, en, cam, stamp) in enumerate(segs):
            # Overlays: hook (meme box style, held across every bait shot), KB label, optional HUD per camera.
            ovl, _ = text_box(a.hook, FRAUNCES, 54, 26, 390 if a.hud == "doorbell" else 300)
            if a.hud == "doorbell":
                hud = hud_doorbell(stamp, cam)
                hud.alpha_composite(ovl)
                ovl = hud
            lg = logo(96)
            ovl.alpha_composite(lg, (SAFE_X0 + 10, SAFE_Y1 - lg.height - 10))
            ovl_path = os.path.join(tmp, f"bait_ovl{si}.png")
            ovl.save(ovl_path)
            dur = en - st
            last = si == len(segs) - 1
            # 4-frame glitch only at the end of the last bait shot: the switch.
            g0 = dur - 4 / FPS if last else dur + 1
            part = os.path.join(tmp, f"bait{si}.mp4")
            subprocess.run([
                "ffmpeg", "-nostdin", "-v", "error", "-y", "-ss", str(st), "-t", str(dur), "-i", src,
                "-loop", "1", "-i", ovl_path, "-filter_complex",
                f"[0:v]fps={FPS},scale={W}:{H}:force_original_aspect_ratio=increase,crop={W}:{H},setsar=1,"
                f"rgbashift=rh=-18:bh=18:enable='gte(t,{g0})',noise=alls=60:allf=t:enable='gte(t,{g0})',"
                f"format=rgba[b];[b][1:v]overlay=0:0:shortest=1,format=yuv420p[v]",
                "-map", "[v]", "-t", str(dur), "-an", "-c:v", "libx264", "-crf", "16", "-preset", "fast", part],
                check=True)
            parts.append(part)
        bait = os.path.join(tmp, "bait.mp4")
        ins = sum((["-i", p_] for p_ in parts), [])
        subprocess.run(["ffmpeg", "-nostdin", "-v", "error", "-y", *ins, "-filter_complex",
                        "".join(f"[{i}:v]" for i in range(len(parts))) + f"concat=n={len(parts)}:v=1:a=0[v]",
                        "-map", "[v]", "-c:v", "libx264", "-crf", "16", "-preset", "fast", bait], check=True)

        # 2. Product segment and end card rendered with PIL.
        card = switch_card(a.switch)
        prod = os.path.join(tmp, "prod.mp4")
        p = subprocess.Popen(["ffmpeg", "-v", "error", "-y", "-f", "rawvideo", "-pix_fmt", "rgb24", "-s", f"{W}x{H}",
                              "-r", str(FPS), "-i", "-", "-c:v", "libx264", "-crf", "16", "-preset", "fast",
                              "-pix_fmt", "yuv420p", prod], stdin=subprocess.PIPE)
        per = int(a.shot_s * FPS)
        for si, shot in enumerate(a.shot):
            im = ImageOps.exif_transpose(Image.open(shot)).convert("RGB")
            base = cover_crop(im, int(W * 1.06), int(H * 1.06))
            for i in range(per):
                z = 1 + 0.05 * i / per
                cw, ch = base.width / z, base.height / z
                # alternate push direction so consecutive shots feel like a sequence, not a slideshow
                dx = (base.width - cw) * (0.5 + (0.3 if si % 2 else -0.3) * i / per)
                fr = base.resize((W, H), Image.BICUBIC, box=(dx, (base.height - ch) / 2, dx + cw, (base.height + ch) / 2))
                fr = fr.convert("RGBA")
                fr.alpha_composite(card)
                p.stdin.write(fr.convert("RGB").tobytes())
        ec = end_card(a.end, a.cta).tobytes()
        for _ in range(int(a.end_s * FPS)):
            p.stdin.write(ec)
        p.stdin.close()
        if p.wait():
            raise SystemExit("product render failed")

        total = cut + len(a.shot) * a.shot_s + a.end_s
        wav = os.path.join(tmp, "sfx.wav")
        synth_audio(wav, cut, total)

        out = a.out + "_captioned.mp4"
        subprocess.run(["ffmpeg", "-nostdin", "-v", "error", "-y", "-i", bait, "-i", prod, "-i", wav,
                        "-filter_complex", "[0:v][1:v]concat=n=2:v=1:a=0[v]", "-map", "[v]", "-map", "2:a",
                        "-af", "loudnorm=I=-14:TP=-1.5:LRA=11", "-c:v", "libx264", "-profile:v", "high",
                        "-pix_fmt", "yuv420p", "-crf", "18", "-preset", "slow", "-c:a", "aac", "-b:a", "320k",
                        "-movflags", "+faststart", "-t", f"{total:.3f}", out], check=True)
    subprocess.run(["ffmpeg", "-nostdin", "-v", "error", "-y", "-i", out, "-frames:v", "1", "-q:v", "2",
                    a.out + "_cover.jpg"], check=True)
    print(f"wrote {out} ({total:.2f}s, switch at {cut:.2f}s)")


if __name__ == "__main__":
    main()
