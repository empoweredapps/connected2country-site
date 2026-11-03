#!/bin/bash
# cPanel cron: pull latest and copy built site into the connected2country.au docroot.
REPO="/home11/mytriibc/repositories/connected2country-site"
DEST="/home11/mytriibc/public_html/connected2country.au"
LOG="$REPO/deploy.log"
cd "$REPO" || exit 1
BEFORE=$(git rev-parse HEAD)
git pull -q origin main >>"$LOG" 2>&1 || { echo "$(date) pull failed" >>"$LOG"; exit 1; }
[ "$BEFORE" = "$(git rev-parse HEAD)" ] && exit 0   # nothing new: skip the copy
if command -v rsync >/dev/null 2>&1; then
  rsync -a --delete --exclude='.well-known' --exclude='cgi-bin' out/ "$DEST/" >>"$LOG" 2>&1
else
  cp -R out/. "$DEST/" >>"$LOG" 2>&1
fi
echo "$(date) deployed $(git rev-parse --short HEAD)" >>"$LOG"
