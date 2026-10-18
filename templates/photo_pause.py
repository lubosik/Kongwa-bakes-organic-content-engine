#!/usr/bin/env python3
"""Photo pause challenge: one real photo, slow push-in, a honey ring sweeping across the bakes.

The viewer tries to pause when the ring sits exactly on the target outline.
The ring path is periodic over the clip length, so the loop is seamless.
Frames are rendered with PIL (sub-pixel smooth push, no zoompan jitter) and piped to ffmpeg.

Usage:
  templates/photo_pause.py PHOTO OUT_BASENAME --target X:Y:R [options]
Target and path coordinates are in the 1080x1920 grid of the final frame (before the push-in).
The overlay (KB label, hook card, order chip) comes from overlay.py so all templates match.
"""
import argparse
import math
import os
import subprocess
import sys
import tempfile

from PIL import Image, ImageDraw, ImageFilter

HERE = os.path.dirname(os.path.abspath(__file__))
BRAND = os.path.join(HERE, "..", "assets", "brand")


def cover(img, w, h):
    """Scale and centre-crop to fill w x h."""
    r = max(w / img.width, h / img.height)
    img = img.resize((math.ceil(img.width * r), math.ceil(img.height * r)), Image.LANCZOS)
    x, y = (img.width - w) // 2, (img.height - h) // 2
    return img.crop((x, y, x + w, y + h))


def ring(radius, thick, color, s):
    size = int((radius + thick * 2) * 2 * s)
    im = Image.new("RGBA", (size, size), (0, 0, 0, 0))
    d = ImageDraw.Draw(im)
    c = size / 2
    r = radius * s
    # soft glow, then the solid ring
    glow = Image.new("RGBA", im.size, (0, 0, 0, 0))
    ImageDraw.Draw(glow).ellipse([c - r, c - r, c + r, c + r], outline=color + (160,), width=int(thick * 2.2 * s))
    im.alpha_composite(glow.filter(ImageFilter.GaussianBlur(6 * s)))
    d.ellipse([c - r, c - r, c + r, c + r], outline=color + (255,), width=int(thick * s))
    return im


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("photo")
    ap.add_argument("out")
    ap.add_argument("--target", required=True, help="x:y:r of the perfect spot, 1080 grid")
    ap.add_argument("--path", default="", help="x0:y0:x1:y1 sweep line through the target (default horizontal)")
    ap.add_argument("--sweeps", type=float, default=3, help="full back-and-forth sweeps per loop")
    ap.add_argument("--dur", type=float, default=6)
    ap.add_argument("--fps", type=int, default=30)
    ap.add_argument("--scale", type=float, default=2)
    ap.add_argument("--push", type=float, default=0.035, help="push-in amount over the clip (house: 3 to 4%%)")
    ap.add_argument("--focus", default="", help="x:y point the push-in centres on, 1080 grid (default target)")
    ap.add_argument("--hook", required=True)
    ap.add_argument("--wrap", type=int, default=18)
    ap.add_argument("--chip", default="orders close Thursday 5pm")
    ap.add_argument("--logo", default=os.path.join(BRAND, "kb-monogram-1024-transparent.png"))
    ap.add_argument("--audio", default="", help="optional licensed bed or SFX track")
    ap.add_argument("--fit", choices=["cover", "card"], default="cover",
                    help="cover fills 9:16; card keeps a square photo whole over a blurred copy of itself")
    ap.add_argument("--card-y", type=int, default=560, help="top of the card in the 1080 grid")
    a = ap.parse_args()

    s = a.scale
    W, H = int(1080 * s), int(1920 * s)
    tx, ty, tr = (float(v) for v in a.target.split(":"))
    fx, fy = (float(v) for v in a.focus.split(":")) if a.focus else (tx, ty)
    if a.path:
        x0, y0, x1, y1 = (float(v) for v in a.path.split(":"))
    else:
        x0, y0, x1, y1 = 120, ty, 960, ty

    # Base photo at slightly over-size so the push-in never shows an edge.
    bw, bh = int(W * (1 + a.push) + 2), int(H * (1 + a.push) + 2)
    photo = Image.open(a.photo).convert("RGB")
    if a.fit == "cover":
        base = cover(photo, bw, bh)
    else:
        # Card: blurred, slightly darkened fill, then the whole photo at frame width.
        base = cover(photo, bw, bh).filter(ImageFilter.GaussianBlur(40 * s))
        base = Image.blend(base, Image.new("RGB", base.size, (20, 14, 10)), 0.35)
        cw_ = int(1080 * s * (1 + a.push))
        card = photo.resize((cw_, int(photo.height * cw_ / photo.width)), Image.LANCZOS)
        # Card top sits at --card-y on the z=1 frame.
        top = int((bh - H * (1 + a.push)) / 2 + a.card_y * s * (1 + a.push))
        base.paste(card, ((bw - cw_) // 2, top))

    with tempfile.TemporaryDirectory() as tmp:
        ovl = os.path.join(tmp, "overlay.png")
        cmd = [sys.executable, os.path.join(HERE, "overlay.py"), ovl, "--scale", str(s), "--hook", a.hook,
               "--wrap", str(a.wrap), "--chip", a.chip,
               "--font", os.path.join(BRAND, "fonts", "Fraunces-SemiBold.ttf"),
               "--font-italic", os.path.join(BRAND, "fonts", "Fraunces-SemiBoldItalic.ttf"),
               "--chip-font", os.path.join(BRAND, "fonts", "Mulish-SemiBold.ttf"),
               # dashed-look target: thin outline square around the perfect spot
               "--box", f"{int(tx - tr)}:{int(ty - tr)}:{int(2 * tr)}:{int(2 * tr)}",
               "--box-radius", str(int(tr)), "--box-thick", "3", "--box-color", "#ffffff"]
        if a.logo:
            cmd += ["--logo", a.logo]
        subprocess.run(cmd, check=True)
        overlay = Image.open(ovl).convert("RGBA")
        rimg = ring(tr * 0.92, 6, (0xE3, 0x9A, 0x3B), s)

        enc = ["ffmpeg", "-nostdin", "-v", "error", "-y", "-f", "rawvideo", "-pix_fmt", "rgb24",
               "-s", f"{W}x{H}", "-r", str(a.fps), "-i", "-"]
        if a.audio:
            enc += ["-stream_loop", "-1", "-i", a.audio, "-af", "loudnorm=I=-14:TP=-1.5:LRA=11", "-shortest"]
        else:
            enc += ["-f", "lavfi", "-t", str(a.dur), "-i", "anullsrc=r=48000:cl=stereo"]
        enc += ["-map", "0:v", "-map", "1:a", "-c:v", "libx264", "-profile:v", "high", "-pix_fmt", "yuv420p",
                "-crf", "17", "-preset", "slow", "-c:a", "aac", "-b:a", "320k", "-ar", "48000",
                "-movflags", "+faststart", "-t", str(a.dur), a.out + "_captioned.mp4"]
        p = subprocess.Popen(enc, stdin=subprocess.PIPE)

        n = int(a.dur * a.fps)
        for i in range(n):
            t = i / n
            # Push-in eases in and back out so frame n wraps onto frame 0.
            z = 1 + a.push * (0.5 - 0.5 * math.cos(2 * math.pi * t))
            cw, ch = W * (1 + a.push) / z, H * (1 + a.push) / z
            # Zoom about the focus point so the target stays under its outline.
            cx = base.width / 2 + (fx * s - W / 2) * (1 + a.push) * (1 - 1 / z)
            cy = base.height / 2 + (fy * s - H / 2) * (1 + a.push) * (1 - 1 / z)
            frame = base.resize((W, H), Image.BICUBIC,
                                box=(cx - cw / 2, cy - ch / 2, cx + cw / 2, cy + ch / 2)).convert("RGBA")
            # Ring: eased back-and-forth along the path; sits on the target only for a moment.
            u = 0.5 - 0.5 * math.cos(2 * math.pi * a.sweeps * t)
            rx, ry = x0 + (x1 - x0) * u, y0 + (y1 - y0) * u
            frame.alpha_composite(rimg, (int(rx * s - rimg.width / 2), int(ry * s - rimg.height / 2)))
            frame.alpha_composite(overlay)
            p.stdin.write(frame.convert("RGB").tobytes())
        p.stdin.close()
        if p.wait():
            raise SystemExit("ffmpeg failed")

    subprocess.run(["ffmpeg", "-nostdin", "-v", "error", "-y", "-i", a.out + "_captioned.mp4", "-vf",
                    "scale=1080:1920:flags=lanczos", "-c:v", "libx264", "-crf", "19", "-preset", "slow",
                    "-maxrate", "6M", "-bufsize", "12M", "-pix_fmt", "yuv420p", "-c:a", "copy",
                    "-movflags", "+faststart", a.out + "_captioned-1080.mp4"], check=True)
    subprocess.run(["ffmpeg", "-nostdin", "-v", "error", "-y", "-i", a.out + "_captioned.mp4",
                    "-frames:v", "1", "-q:v", "2", a.out + "_cover.jpg"], check=True)
    print("wrote", a.out + "_captioned.mp4", a.out + "_captioned-1080.mp4", a.out + "_cover.jpg")


if __name__ == "__main__":
    main()
