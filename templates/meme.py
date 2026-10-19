#!/usr/bin/env python3
"""Meme template: real bake photo, meme text in a white rounded box, optional green-screen character on top.

Matches the reference format (POV text box over a loaf photo with a dancing animal in front), with our own
character clip, our real bakes, and a small KB label for brand pulsing (Teixeira 2010).

Usage:
  templates/meme.py PHOTO OUT_BASENAME --text "POV: ..." [--character clip.mp4] [options]
Coordinates are on the 1080x1920 grid. Output is 1080x1920 (character clips are 720p to 1080p,
so 4K would only upscale them).
"""
import argparse
import math
import os
import subprocess
import sys
import tempfile
import textwrap

from PIL import Image, ImageDraw, ImageFont

sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from photo_pause import BRAND, cover  # noqa: E402

W, H = 1080, 1920
SAFE_X0, SAFE_X1, SAFE_Y0, SAFE_Y1 = 70, 900, 250, 1530


def text_box(text, font_path, size, wrap, y):
    """Black text on white rounded boxes, one box per line, centred: the native meme caption look."""
    im = Image.new("RGBA", (W, H), (0, 0, 0, 0))
    d = ImageDraw.Draw(im)
    f = ImageFont.truetype(font_path, size)
    lines = textwrap.wrap(text, wrap)
    lh = int(size * 1.28)
    cx = (SAFE_X0 + SAFE_X1) / 2
    widths = [d.textlength(l, font=f) for l in lines]
    if max(widths) + 44 > SAFE_X1 - SAFE_X0:
        raise SystemExit("meme text too wide for the safe zone; lower --wrap or --size")
    # One merged white shape: a rounded rect per line, overlapping vertically so it reads as one block.
    for i, (line, w) in enumerate(zip(lines, widths)):
        top = y + i * lh
        d.rounded_rectangle([cx - w / 2 - 22, top - 8, cx + w / 2 + 22, top + lh + 6], radius=22,
                            fill=(255, 255, 255, 255))
    for i, (line, w) in enumerate(zip(lines, widths)):
        d.text((cx - w / 2, y + i * lh + (lh - size) / 2 - size * 0.08), line, font=f, fill=(0, 0, 0, 255))
    return im, y + len(lines) * lh


def draw_eyes(img, spec, t, look, scale):
    """Googly eyes drawn on the photo itself, so they ride the push-in. Pupils drift and the eyes blink once."""
    x1, y1, x2, y2, r = (float(v) * scale for v in spec.split(":"))
    d = ImageDraw.Draw(img)
    blink = 2.6 < (t % 4.0) < 2.75
    for cx, cy in ((x1, y1), (x2, y2)):
        if blink:
            d.line([cx - r, cy, cx + r, cy], fill=(20, 14, 10), width=max(2, int(r * 0.18)))
            continue
        d.ellipse([cx - r, cy - r, cx + r, cy + r], fill=(255, 255, 255), outline=(20, 14, 10), width=max(2, int(r * 0.08)))
        if look == "side":
            ox, oy = 0.42 * r * math.sin(t * 1.6), 0.15 * r
        elif look == "up":
            ox, oy = 0.1 * r * math.sin(t * 2), -0.42 * r
        else:
            ox, oy = 0.08 * r * math.sin(t * 3), 0.05 * r
        pr = r * 0.48
        d.ellipse([cx + ox - pr, cy + oy - pr, cx + ox + pr, cy + oy + pr], fill=(20, 14, 10))
        d.ellipse([cx + ox - pr * 0.45, cy + oy - pr * 0.6, cx + ox - pr * 0.05, cy + oy - pr * 0.2],
                  fill=(255, 255, 255))


def write_steps(path, dur, step_s, rate=48000):
    """Soft low thud on every step: our own sound, nothing to license."""
    import struct
    import wave
    n = int(dur * rate)
    period = int(step_s * rate)
    buf = bytearray()
    for i in range(n):
        k = i % period
        v = 0.0
        if k < 4000:
            env = math.exp(-k / 700)
            v = 0.7 * env * math.sin(2 * math.pi * (70 + 40 * math.exp(-k / 300)) * k / rate)
        s = int(max(-1, min(1, v)) * 32767)
        buf += struct.pack("<hh", s, s)
    with wave.open(path, "wb") as w:
        w.setnchannels(2)
        w.setsampwidth(2)
        w.setframerate(rate)
        w.writeframes(bytes(buf))


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("photo")
    ap.add_argument("out")
    ap.add_argument("--text", required=True)
    ap.add_argument("--wrap", type=int, default=24)
    ap.add_argument("--size", type=int, default=58)
    ap.add_argument("--text-y", type=int, default=280)
    ap.add_argument("--font", default=os.path.join(BRAND, "fonts", "Fraunces-SemiBold.ttf"))
    ap.add_argument("--character", default="", help="pre-keyed .webm with alpha (preferred) or a green-screen clip")
    ap.add_argument("--char-h", type=int, default=1050, help="character height on the 1080 grid")
    ap.add_argument("--char-x", type=int, default=560, help="character centre x")
    ap.add_argument("--char-bottom", type=int, default=1860, help="character feet y")
    ap.add_argument("--key", default="0x00ff00", help="chroma key colour")
    ap.add_argument("--similarity", type=float, default=0.13, help="chromakey similarity (chroma only, so whites stay solid)")
    ap.add_argument("--dur", type=float, default=6)
    ap.add_argument("--push", type=float, default=0.04)
    ap.add_argument("--steps", type=float, default=0, help="seconds between footstep thuds (0 = none)")
    ap.add_argument("--logo", default=os.path.join(BRAND, "kb-monogram-1024-transparent.png"))
    ap.add_argument("--photo2", default="", help="second beat: hard cut to this photo at --cut seconds")
    ap.add_argument("--text2", default="", help="second beat text (two-beat memes: nobody / me)")
    ap.add_argument("--cut", type=float, default=0, help="time of the hard cut (default: half way)")
    ap.add_argument("--eyes", default="", help="googly eyes on the bake: x1:y1:x2:y2:r on the 1080 grid (beat 1)")
    ap.add_argument("--look", default="side", choices=["side", "up", "camera"],
                    help="where the pupils drift: side to side, up (towards the text), or at the viewer")
    a = ap.parse_args()
    cut = a.cut or a.dur / 2

    def overlay_png(text, path):
        ovl, _ = text_box(text, a.font, a.size, a.wrap, a.text_y)
        if a.logo:
            logo = Image.open(a.logo).convert("RGBA")
            logo = logo.resize((96, int(logo.height * 96 / logo.width)), Image.LANCZOS)
            # Bottom-left of the safe zone, small: brand pulsing without making the meme look like an ad.
            ovl.alpha_composite(logo, (SAFE_X0 + 10, SAFE_Y1 - logo.height - 10))
        ovl.save(path)

    def oversized(path):
        return cover(Image.open(path).convert("RGB"), int(W * (1 + a.push)) + 2, int(H * (1 + a.push)) + 2)

    with tempfile.TemporaryDirectory() as tmp:
        beats = [(oversized(a.photo), os.path.join(tmp, "o1.png"), a.text)]
        two = bool(a.photo2 or a.text2)
        if two:
            beats.append((oversized(a.photo2) if a.photo2 else beats[0][0], os.path.join(tmp, "o2.png"),
                          a.text2 or a.text))
        for _, path, text in beats:
            overlay_png(text, path)

        # Input 0: the photo push-in rendered with PIL (sub-pixel smooth), cutting to beat 2 at `cut`.
        inputs = ["-f", "rawvideo", "-pix_fmt", "rgb24", "-s", f"{W}x{H}", "-r", "30", "-i", "-"]
        for _, path, _ in beats:
            inputs += ["-loop", "1", "-t", str(a.dur), "-i", path]
        nxt = 1 + len(beats)
        graph, last = [], "0:v"
        if a.character:
            if a.character.endswith(".webm"):
                # Pre-keyed with templates/key_character.py: VP9 with alpha needs the libvpx decoder.
                inputs += ["-stream_loop", "-1", "-t", str(a.dur), "-c:v", "libvpx-vp9", "-i", a.character]
                graph.append(f"[{nxt}:v]fps=30,scale=-2:{a.char_h},format=rgba[ch]")
            else:
                inputs += ["-stream_loop", "-1", "-t", str(a.dur), "-i", a.character]
                graph.append(f"[{nxt}:v]fps=30,scale=-2:{a.char_h},chromakey={a.key}:{a.similarity}:0.06,"
                             f"despill=type=green,format=rgba[ch]")
            graph.append(f"[{last}][ch]overlay=x={a.char_x}-overlay_w/2:y={a.char_bottom}-overlay_h:format=auto[wc]")
            last, nxt = "wc", nxt + 1
        if two:
            graph.append(f"[{last}][1:v]overlay=0:0:format=auto:enable='lt(t,{cut})'[t1]")
            graph.append(f"[t1][2:v]overlay=0:0:format=auto:enable='gte(t,{cut})',format=yuv420p[v]")
        else:
            graph.append(f"[{last}][1:v]overlay=0:0:format=auto,format=yuv420p[v]")
        if a.steps:
            wav = os.path.join(tmp, "steps.wav")
            write_steps(wav, a.dur, a.steps)
            inputs += ["-i", wav]
        else:
            inputs += ["-f", "lavfi", "-t", str(a.dur), "-i", "anullsrc=r=48000:cl=stereo"]
        out = a.out + "_captioned.mp4"
        proc = subprocess.Popen(["ffmpeg", "-v", "error", "-y", *inputs, "-filter_complex", ";".join(graph),
                                 "-map", "[v]", "-map", f"{nxt}:a", "-af", "loudnorm=I=-14:TP=-1.5:LRA=11",
                                 "-c:v", "libx264", "-profile:v", "high", "-pix_fmt", "yuv420p", "-crf", "18",
                                 "-preset", "slow", "-c:a", "aac", "-b:a", "320k", "-ar", "48000",
                                 "-movflags", "+faststart", "-t", str(a.dur), out], stdin=subprocess.PIPE)
        n = int(a.dur * 30)
        for i in range(n):
            t = i / 30
            beat = 1 if two and t >= cut else 0
            bg = beats[beat][0]
            # Each beat pushes in from its own start, so the cut lands on a fresh wide frame.
            t0 = cut if beat else 0
            span = (a.dur - cut) if (two and beat) else (cut if two else a.dur)
            z = 1 + a.push * (t - t0) / span
            cw, ch = W * (1 + a.push) / z, H * (1 + a.push) / z
            cx, cy = bg.width / 2, bg.height / 2
            src = bg
            if a.eyes and beat == 0:
                src = bg.copy()
                draw_eyes(src, a.eyes, t, a.look, bg.width / W)
            fr = src.resize((W, H), Image.BICUBIC, box=(cx - cw / 2, cy - ch / 2, cx + cw / 2, cy + ch / 2))
            proc.stdin.write(fr.tobytes())
        proc.stdin.close()
        if proc.wait():
            raise SystemExit("ffmpeg failed")
    subprocess.run(["ffmpeg", "-nostdin", "-v", "error", "-y", "-i", out, "-frames:v", "1", "-q:v", "2",
                    a.out + "_cover.jpg"], check=True)
    print("wrote", out)


if __name__ == "__main__":
    main()
