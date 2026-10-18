#!/usr/bin/env bash
# Pause challenge assembly (brief section 7.3).
# One static real shot, 5 to 7 s, honey outline at the "perfect" position,
# hook text burned in from frame 1, KB label from frame 1, no cuts, loop-friendly.
#
# Usage:
#   templates/pause-challenge.sh IN.mov OUT_BASENAME [options]
# Options (env vars):
#   START=0          seconds into the source to start
#   DUR=6            clip length in seconds (5 to 7)
#   HOOK="only 2% can PAUSE it on the perfect slice"
#   BOX="430:760:220:520"   outline x:y:w:h on the 1080x1920 frame
#   OUTLINE=0xe39a3b        honey
#   THICK=6
#   LOGO=assets/brand/kb-monogram.png   optional, top-right, from frame 1
#   FONT=/usr/share/fonts/opentype/inter/Inter-Bold.otf
#   WRAP=20          max characters per hook line
#   LOOPFADE=0.25    seconds of end-to-start crossfade so the loop is seamless (0 to disable)
# Writes OUT_BASENAME_master.mp4 (no text, no outline) and OUT_BASENAME_captioned.mp4.
set -euo pipefail

IN="$1"; OUT="$2"
START="${START:-0}"; DUR="${DUR:-6}"
HOOK="${HOOK:-only 2% can PAUSE it on the perfect slice}"
BOX="${BOX:-430:760:220:520}"
OUTLINE="${OUTLINE:-0xe39a3b}"; THICK="${THICK:-6}"
LOGO="${LOGO:-}"
FONT="${FONT:-/usr/share/fonts/opentype/inter/Inter-Bold.otf}"
LOOPFADE="${LOOPFADE:-0.25}"

IFS=: read -r BX BY BW BH <<<"$BOX"
TMP="$(mktemp -d)"; trap 'rm -rf "$TMP"' EXIT

# Hook text goes through a file so quotes and % never break the filter graph.
# Wrapped to WRAP chars per line so it stays inside the TikTok/Reels safe zone.
WRAP="${WRAP:-20}"
python3 -c 'import sys,textwrap; sys.stdout.write("\n".join(textwrap.wrap(sys.argv[1], int(sys.argv[2]))))' "$HOOK" "$WRAP" > "$TMP/hook.txt"

HAS_AUDIO=$(ffprobe -v error -select_streams a -show_entries stream=index -of csv=p=0 "$IN" | head -1)

# 1. Trim, cover-crop to 9:16, 30 fps. Take LOOPFADE extra so the tail can blend into the head.
EXTRA=$(python3 -c "print($DUR + $LOOPFADE)")
VF="scale=1080:1920:force_original_aspect_ratio=increase,crop=1080:1920,fps=30,setsar=1,format=yuv420p"
if [ -n "$HAS_AUDIO" ]; then
  ffmpeg -v error -y -ss "$START" -t "$EXTRA" -i "$IN" -vf "$VF" -c:v libx264 -crf 14 -preset fast -c:a pcm_s16le "$TMP/base.mov"
else
  ffmpeg -v error -y -ss "$START" -t "$EXTRA" -i "$IN" -f lavfi -t "$EXTRA" -i anullsrc=r=48000:cl=stereo \
    -vf "$VF" -map 0:v -map 1:a -c:v libx264 -crf 14 -preset fast -c:a pcm_s16le -shortest "$TMP/base.mov"
fi

# 2. Seamless loop: crossfade the last LOOPFADE seconds onto the first frames.
if python3 -c "import sys; sys.exit(0 if $LOOPFADE > 0 else 1)"; then
  OFF=$(python3 -c "print($DUR - $LOOPFADE)")
  ffmpeg -v error -y -i "$TMP/base.mov" -i "$TMP/base.mov" -filter_complex \
    "[0:v]trim=start=$LOOPFADE:end=$EXTRA,setpts=PTS-STARTPTS[a];[1:v]trim=0:$LOOPFADE,setpts=PTS-STARTPTS[b];\
     [a][b]xfade=transition=fade:duration=$LOOPFADE:offset=$OFF,format=yuv420p[v];\
     [0:a]atrim=start=$LOOPFADE:end=$EXTRA,asetpts=PTS-STARTPTS[aa];[1:a]atrim=0:$LOOPFADE,asetpts=PTS-STARTPTS[ab];\
     [aa][ab]acrossfade=d=$LOOPFADE[au]" \
    -map "[v]" -map "[au]" -c:v libx264 -crf 14 -preset fast -c:a pcm_s16le "$TMP/loop.mov"
else
  cp "$TMP/base.mov" "$TMP/loop.mov"
fi

ENC="-c:v libx264 -profile:v high -pix_fmt yuv420p -r 30 -crf 18 -preset slow -movflags +faststart -c:a aac -b:a 192k -ar 48000"
AF="loudnorm=I=-14:TP=-1:LRA=11"

# 3. Clean master.
ffmpeg -v error -y -i "$TMP/loop.mov" -af "$AF" $ENC -t "$DUR" "${OUT}_master.mp4"

# 4. Captioned: outline, hook, optional KB label, all from frame 1.
GRAPH="[0:v]drawbox=x=$BX:y=$BY:w=$BW:h=$BH:color=$OUTLINE:t=$THICK,\
drawtext=fontfile=$FONT:textfile=$TMP/hook.txt:expansion=none:fontsize=64:fontcolor=white:\
x=(w-text_w)/2:y=260:box=1:boxcolor=black@0.45:boxborderw=28:line_spacing=12[t]"
if [ -n "$LOGO" ] && [ -f "$LOGO" ]; then
  GRAPH="$GRAPH;[1:v]scale=150:-1[l];[t][l]overlay=W-w-60:90[v]"
  ffmpeg -v error -y -i "$TMP/loop.mov" -i "$LOGO" -filter_complex "$GRAPH" -map "[v]" -map 0:a -af "$AF" $ENC -t "$DUR" "${OUT}_captioned.mp4"
else
  ffmpeg -v error -y -i "$TMP/loop.mov" -filter_complex "$GRAPH" -map "[t]" -map 0:a -af "$AF" $ENC -t "$DUR" "${OUT}_captioned.mp4"
fi

echo "wrote ${OUT}_master.mp4 and ${OUT}_captioned.mp4"
