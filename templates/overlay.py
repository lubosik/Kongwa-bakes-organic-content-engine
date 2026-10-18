#!/usr/bin/env python3
"""Render a transparent 9:16 overlay PNG: KB label, hook card, honey target outline, order chip.

Layout is designed on a 1080x1920 grid and multiplied by --scale (2 = 4K 2160x3840).
Everything stays inside the house safe zone: x 70 to 900, y 250 to 1530 (docs/house-standards.md 1.8).

Hook text uses strategic capitalisation from the caller as-is. Words wrapped in *asterisks*
are set in the italic font (house type rule: serif hero with one or two italic words).
"""
import argparse
import textwrap

from PIL import Image, ImageDraw, ImageFilter, ImageFont

SAFE_X0, SAFE_X1, SAFE_Y0, SAFE_Y1 = 70, 900, 250, 1530


def parse_runs(line):
    """Split 'only 2% can *pause* it' into [(text, italic), ...] keeping spaces."""
    runs, italic, buf = [], False, ""
    for ch in line:
        if ch == "*":
            if buf:
                runs.append((buf, italic))
            buf, italic = "", not italic
        else:
            buf += ch
    if buf:
        runs.append((buf, italic))
    return runs


def run_width(draw, runs, fonts):
    return sum(draw.textlength(t, font=fonts[i]) for t, i in runs)


def draw_runs(draw, x, y, runs, fonts, fill):
    for t, i in runs:
        draw.text((x, y), t, font=fonts[i], fill=fill)
        x += draw.textlength(t, font=fonts[i])


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("out")
    ap.add_argument("--scale", type=float, default=2)
    ap.add_argument("--hook", required=True)
    ap.add_argument("--wrap", type=int, default=18)
    ap.add_argument("--hook-y", type=int, default=260, help="top of hook block, 1080 grid (pushed down under the logo)")
    ap.add_argument("--hook-size", type=int, default=78)
    ap.add_argument("--font", required=True)
    ap.add_argument("--font-italic", default=None)
    ap.add_argument("--chip", default="", help="small order line near the bottom of the safe zone")
    ap.add_argument("--chip-font", default=None)
    ap.add_argument("--box", default="", help="target outline x:y:w:h on the 1080 grid")
    ap.add_argument("--box-color", default="#e39a3b")
    ap.add_argument("--box-thick", type=int, default=5)
    ap.add_argument("--box-radius", type=int, default=24)
    ap.add_argument("--logo", default="")
    ap.add_argument("--logo-w", type=int, default=120)
    a = ap.parse_args()

    s = a.scale
    W, H = int(1080 * s), int(1920 * s)
    img = Image.new("RGBA", (W, H), (0, 0, 0, 0))

    # Target outline.
    if a.box:
        x, y, w, h = (int(v) for v in a.box.split(":"))
        ImageDraw.Draw(img).rounded_rectangle(
            [x * s, y * s, (x + w) * s, (y + h) * s],
            radius=a.box_radius * s, outline=a.box_color, width=max(1, int(a.box_thick * s)))

    # KB label, centred at the top of the safe zone, from frame 1 (brand pulsing).
    # The hook block starts underneath it.
    hook_top = a.hook_y * s
    cx = (SAFE_X0 + SAFE_X1) / 2 * s
    if a.logo:
        logo = Image.open(a.logo).convert("RGBA")
        lw = int(a.logo_w * s)
        logo = logo.resize((lw, int(logo.height * lw / logo.width)), Image.LANCZOS)
        img.alpha_composite(logo, (int(cx - lw / 2), int(SAFE_Y0 * s)))
        hook_top = max(hook_top, SAFE_Y0 * s + logo.height + 28 * s)

    # Hook: white type with a soft shadow, centred lines, never re-centred mid-sentence.
    size = int(a.hook_size * s)
    fonts = {False: ImageFont.truetype(a.font, size),
             True: ImageFont.truetype(a.font_italic or a.font, size)}
    lines = textwrap.wrap(a.hook, a.wrap)
    shadow = Image.new("RGBA", (W, H), (0, 0, 0, 0))
    text = Image.new("RGBA", (W, H), (0, 0, 0, 0))
    sd, td = ImageDraw.Draw(shadow), ImageDraw.Draw(text)
    y = hook_top
    lh = int(size * 1.12)
    for line in lines:
        runs = parse_runs(line)
        lw = run_width(td, runs, fonts)
        if lw > (SAFE_X1 - SAFE_X0) * s:
            raise SystemExit(f"hook line too wide for safe zone: {line!r}; lower --wrap or --hook-size")
        x = cx - lw / 2
        draw_runs(sd, x, y + 3 * s, runs, fonts, (0, 0, 0, 150))
        draw_runs(td, x, y, runs, fonts, (255, 255, 255, 255))
        y += lh
    if y > SAFE_Y1 * s:
        raise SystemExit("hook runs past the safe zone")
    img.alpha_composite(shadow.filter(ImageFilter.GaussianBlur(10 * s)))
    img.alpha_composite(text)

    # Order chip: small pill, bottom of the safe zone.
    if a.chip:
        cf = ImageFont.truetype(a.chip_font or a.font, int(34 * s))
        d = ImageDraw.Draw(img)
        tw = d.textlength(a.chip, font=cf)
        pad_x, pad_y = 28 * s, 16 * s
        bh = cf.size + 2 * pad_y
        x0 = cx - tw / 2 - pad_x
        y0 = (SAFE_Y1 - 30) * s - bh
        d.rounded_rectangle([x0, y0, x0 + tw + 2 * pad_x, y0 + bh], radius=bh / 2, fill=(20, 14, 10, 150))
        d.text((x0 + pad_x, y0 + pad_y - cf.size * 0.1), a.chip, font=cf, fill=(255, 255, 255, 255))

    img.save(a.out)


if __name__ == "__main__":
    main()
