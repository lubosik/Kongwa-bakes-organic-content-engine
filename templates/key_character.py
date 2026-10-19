#!/usr/bin/env python3
"""Key a green-screen character clip once into a transparent .mov (PNG codec, alpha) for reuse in memes.

A pixel is background when green clearly beats both red and blue (G - max(R, B) > --lo), fully background
above --hi, with a soft ramp between. This keeps white fur with a green floor bounce solid, which ffmpeg's
colorkey and chromakey could not do on a soft studio green. Spill is removed by clamping G to max(R, B).

Usage: templates/key_character.py IN.mp4 OUT.webm (VP9 with alpha, small) or OUT.mov (PNG codec) [--lo 18] [--hi 45] [--trim-bottom 0]
"""
import argparse
import subprocess

import numpy as np


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("src")
    ap.add_argument("out")
    ap.add_argument("--lo", type=float, default=18)
    ap.add_argument("--hi", type=float, default=45)
    a = ap.parse_args()

    probe = subprocess.run(["ffprobe", "-v", "error", "-select_streams", "v", "-show_entries",
                            "stream=width,height,r_frame_rate", "-of", "csv=p=0", a.src],
                           capture_output=True, text=True, check=True).stdout.strip().split(",")
    w, h, rate = int(probe[0]), int(probe[1]), probe[2]
    dec = subprocess.Popen(["ffmpeg", "-nostdin", "-v", "error", "-i", a.src, "-f", "rawvideo", "-pix_fmt", "rgb24", "-"],
                           stdout=subprocess.PIPE)
    enc = subprocess.Popen(["ffmpeg", "-v", "error", "-y", "-f", "rawvideo", "-pix_fmt", "rgba", "-s", f"{w}x{h}",
                            "-r", rate, "-i", "-", *(["-c:v", "libvpx-vp9", "-pix_fmt", "yuva420p", "-b:v", "0", "-crf", "20", "-auto-alt-ref", "0"] if a.out.endswith(".webm") else ["-c:v", "png", "-pix_fmt", "rgba"]), a.out], stdin=subprocess.PIPE)
    size = w * h * 3
    while True:
        buf = dec.stdout.read(size)
        if len(buf) < size:
            break
        f = np.frombuffer(buf, np.uint8).reshape(h, w, 3).astype(np.float32)
        r, g, b = f[..., 0], f[..., 1], f[..., 2]
        m = np.maximum(r, b)
        excess = g - m
        alpha = 1 - np.clip((excess - a.lo) / (a.hi - a.lo), 0, 1)
        g = np.where(excess > 0, m, g)  # despill
        out = np.dstack([r, g, b, alpha * 255]).clip(0, 255).astype(np.uint8)
        enc.stdin.write(out.tobytes())
    enc.stdin.close()
    dec.wait()
    if enc.wait():
        raise SystemExit("encode failed")
    print("wrote", a.out)


if __name__ == "__main__":
    main()
