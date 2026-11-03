#!/bin/bash
# cPanel cron: pull latest and copy built site into the connected2country.au docroot.
REPO="$HOME/repositories/connected2country-site"
DEST="$HOME/public_html/connected2country.au"
LOG="$REPO/deploy.log"
cd "$REPO" || exit 1
git pull -q origin main >>"$LOG" 2>&1 || { echo "$(date) pull failed" >>"$LOG"; exit 1; }
if command -v rsync >/dev/null 2>&1; then
  rsync -a --delete --exclude='.well-known' --exclude='cgi-bin' out/ "$DEST/" >>"$LOG" 2>&1
else
  cp -R out/. "$DEST/" >>"$LOG" 2>&1
fi
echo "$(date) deployed $(git rev-parse --short HEAD)" >>"$LOG"
