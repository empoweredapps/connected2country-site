#!/bin/bash
# cPanel cron: pull latest and sync built site into public_html
cd "$HOME/repositories/connected2country-site" || exit 1
git pull -q origin main || exit 1
rsync -a --delete --exclude='.well-known' --exclude='cgi-bin' out/ "$HOME/public_html/"
