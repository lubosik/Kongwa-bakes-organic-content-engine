#!/usr/bin/env bash
# Pause challenge assembly (brief section 7.3, house standards 1.3 to 1.8).
# One static real shot, 5 to 7 s, honey outline at the "perfect" position, hook card and
# KB label from frame 1, order chip on screen the whole time, no cuts, seamless loop.
#
# Usage:
#   templates/pause-challenge.sh IN.mov OUT_BASENAME
# Options (env vars):
#   START=0            seconds into the source to start
#   DUR=6              clip length in seconds (5 to 7)
#   HOOK="only 2% can *pause* it on the PERFECT slice"   *italic*, strategic caps as written
#   WRAP=18            max characters per hook line
#   BOX="430:760:220:520"   target outline x:y:w:h on the 1080x1920 grid ("" for none)
#   CHIP="orders close Thursday 5pm"
#   LOGO=assets/brand/kb-monogram-1024-transparent.png   ("" for none)
#   FONT, FONT_ITALIC, CHIP_FONT        default to brand Fraunces and Mulish
#   SCALE=2            2 = 4K 2160x3840 master (house standard), 1 = 1080x1920
#   MUSIC=             optional licensed bed (TikTok CML or our own Suno), sits MUSIC_DB under the clip
#   MUSIC_DB=-16
#   LOOPFADE=0.25      end-to-start crossfade so the loop is seamless (0 to disable)
# Writes:
#   OUT_master.mp4              clean, no overlay, no music, at SCALE
#   OUT_captioned.mp4           overlay (plus music if MUSIC), at SCALE
#   OUT_captioned-nomusic.mp4   only when MUSIC is set (creators add trending audio in-app)
#   OUT_captioned-1080.mp4      phone copy of the captioned version
#   OUT_cover.jpg               frame 0 of the captioned version (doubles as the cover)
set -euo pipefail

HERE="$(cd "$(dirname "$0")" && pwd)"
IN="$1"; OUT="$2"
START="${START:-0}"; DUR="${DUR:-6}"
HOOK="${HOOK:-only 2% can *pause* it on the PERFECT slice}"
WRAP="${WRAP:-18}"
BOX="${BOX-430:760:220:520}"
CHIP="${CHIP-orders close Thursday 5pm}"
LOGO="${LOGO-$HERE/../assets/brand/kb-monogram-1024-transparent.png}"
FONT="${FONT:-$HERE/../assets/brand/fonts/Fraunces-SemiBold.ttf}"
FONT_ITALIC="${FONT_ITALIC:-$HERE/../assets/brand/fonts/Fraunces-SemiBoldItalic.ttf}"
CHIP_FONT="${CHIP_FONT:-$HERE/../assets/brand/fonts/Mulish-SemiBold.ttf}"
SCALE="${SCALE:-2}"
MUSIC="${MUSIC:-}"; MUSIC_DB="${MUSIC_DB:--16}"
LOOPFADE="${LOOPFADE:-0.25}"

W=$(python3 -c "print(int(1080*$SCALE))"); H=$(python3 -c "print(int(1920*$SCALE))")
TMP="$(mktemp -d)"; trap 'rm -rf "$TMP"' EXIT

# 0. Overlay PNG (fails loudly if the hook spills out of the safe zone).
OVL_ARGS=(--scale "$SCALE" --hook "$HOOK" --wrap "$WRAP" --font "$FONT" --font-italic "$FONT_ITALIC" --chip "$CHIP" --chip-font "$CHIP_FONT" --box "$BOX")
[ -n "$LOGO" ] && OVL_ARGS+=(--logo "$LOGO")
python3 "$HERE/overlay.py" "$TMP/overlay.png" "${OVL_ARGS[@]}"

# 1. Trim, cover-crop to 9:16, 30 fps. Take LOOPFADE extra so the tail can blend into the head.
EXTRA=$(python3 -c "print($DUR + $LOOPFADE)")
VF="scale=$W:$H:force_original_aspect_ratio=increase:flags=lanczos,crop=$W:$H,fps=30,setsar=1,format=yuv420p"
HAS_AUDIO=$(ffprobe -v error -select_streams a -show_entries stream=index -of csv=p=0 "$IN" | head -1)
if [ -n "$HAS_AUDIO" ]; then
  ffmpeg -nostdin -v error -y -ss "$START" -t "$EXTRA" -i "$IN" -vf "$VF" -c:v libx264 -crf 12 -preset fast -c:a pcm_s16le -ar 48000 -ac 2 "$TMP/base.mov"
else
  ffmpeg -nostdin -v error -y -ss "$START" -t "$EXTRA" -i "$IN" -f lavfi -t "$EXTRA" -i anullsrc=r=48000:cl=stereo \
    -vf "$VF" -map 0:v -map 1:a -c:v libx264 -crf 12 -preset fast -c:a pcm_s16le -shortest "$TMP/base.mov"
fi

# 2. Seamless loop: crossfade the last LOOPFADE seconds onto the first frames.
if python3 -c "import sys; sys.exit(0 if $LOOPFADE > 0 else 1)"; then
  OFF=$(python3 -c "print($DUR - $LOOPFADE)")
  ffmpeg -nostdin -v error -y -i "$TMP/base.mov" -i "$TMP/base.mov" -filter_complex \
    "[0:v]trim=start=$LOOPFADE:end=$EXTRA,setpts=PTS-STARTPTS[a];[1:v]trim=0:$LOOPFADE,setpts=PTS-STARTPTS[b];\
     [a][b]xfade=transition=fade:duration=$LOOPFADE:offset=$OFF,format=yuv420p[v];\
     [0:a]atrim=start=$LOOPFADE:end=$EXTRA,asetpts=PTS-STARTPTS[aa];[1:a]atrim=0:$LOOPFADE,asetpts=PTS-STARTPTS[ab];\
     [aa][ab]acrossfade=d=$LOOPFADE[au]" \
    -map "[v]" -map "[au]" -c:v libx264 -crf 12 -preset fast -c:a pcm_s16le "$TMP/loop.mov"
else
  cp "$TMP/base.mov" "$TMP/loop.mov"
fi

ENC=(-c:v libx264 -profile:v high -pix_fmt yuv420p -r 30 -crf 17 -preset slow -movflags +faststart -c:a aac -b:a 320k -ar 48000)
LN="loudnorm=I=-14:TP=-1.5:LRA=11"

# 3. Clean master.
ffmpeg -nostdin -v error -y -i "$TMP/loop.mov" -af "$LN" "${ENC[@]}" -t "$DUR" "${OUT}_master.mp4"

# 4. Captioned, without music.
ffmpeg -nostdin -v error -y -i "$TMP/loop.mov" -i "$TMP/overlay.png" \
  -filter_complex "[0:v][1:v]overlay=0:0:format=auto,format=yuv420p[v]" -map "[v]" -map 0:a -af "$LN" \
  "${ENC[@]}" -t "$DUR" "$TMP/cap_nomusic.mp4"

# 5. Optional music bed: steady level from the top, no ducking pump, MUSIC_DB under the clip.
if [ -n "$MUSIC" ]; then
  cp "$TMP/cap_nomusic.mp4" "${OUT}_captioned-nomusic.mp4"
  ffmpeg -nostdin -v error -y -i "$TMP/cap_nomusic.mp4" -stream_loop -1 -i "$MUSIC" -filter_complex \
    "[1:a]atrim=0:$DUR,loudnorm=I=$(python3 -c "print(-14 + $MUSIC_DB)"):TP=-2:LRA=11,afade=t=out:st=$(python3 -c "print($DUR-0.3)"):d=0.3[m];\
     [0:a][m]amix=inputs=2:duration=first:normalize=0,$LN[a]" \
    -map 0:v -map "[a]" -c:v copy -c:a aac -b:a 320k -ar 48000 -movflags +faststart -t "$DUR" "${OUT}_captioned.mp4"
else
  mv "$TMP/cap_nomusic.mp4" "${OUT}_captioned.mp4"
fi

# 6. Phone copy and cover.
ffmpeg -nostdin -v error -y -i "${OUT}_captioned.mp4" -vf "scale=1080:1920:flags=lanczos" -c:v libx264 -crf 19 -preset slow \
  -maxrate 6M -bufsize 12M -pix_fmt yuv420p -c:a copy -movflags +faststart "${OUT}_captioned-1080.mp4"
ffmpeg -nostdin -v error -y -i "${OUT}_captioned.mp4" -frames:v 1 -q:v 2 "${OUT}_cover.jpg"

echo "wrote ${OUT}_{master,captioned,captioned-1080}.mp4 and ${OUT}_cover.jpg"
