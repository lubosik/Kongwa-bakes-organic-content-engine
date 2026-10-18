#!/usr/bin/env bash
# Fails if any tracked text file contains an em-dash (U+2014).
# The brief's `grep -rnP "\x{2014}"` errors in a non-UTF-8 locale, so force UTF-8 mode.
# research/raw/ holds verbatim third-party scrapes, so it is excluded; binaries are skipped (-I).
set -u
if grep -rnIP '(*UTF8)\x{2014}' --exclude-dir=.git --exclude-dir=raw --exclude-dir=node_modules --exclude-dir=references/videos . ; then
  echo "em-dash found" >&2
  exit 1
fi
echo "no em-dashes"
