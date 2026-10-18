#!/usr/bin/env bash
# Fails if any tracked text file contains an em-dash (U+2014).
# The brief's `grep -rnP "\x{2014}"` errors in a non-UTF-8 locale, so force UTF-8 mode.
set -u
if grep -rnP '(*UTF8)\x{2014}' --exclude-dir=.git --exclude-dir=node_modules --exclude-dir=references/videos . ; then
  echo "em-dash found" >&2
  exit 1
fi
echo "no em-dashes"
