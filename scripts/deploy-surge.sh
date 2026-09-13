#!/usr/bin/env bash
# TradeLift production deploy to https://tradelift.surge.sh
# Requires: surge CLI logged in (email: tradelift056411@uberip.com, token stored in ~/.config/surge)
# NOTE: surge.sh does not serve .pdf files (404) — the lead-magnet PDF is deployed under an
# extensionless name (assets/careers.guide, served as application/octet-stream). js/main.js
# points the exit-modal download/_next to that path with download="trade-lift-5-trades.pdf".
set -euo pipefail

REPO_DIR="$(cd "$(dirname "${BASH_SOURCE[0]}")/.." && pwd)"
BUILD_DIR="$(mktemp -d /tmp/tradelift-deploy.XXXXXX)"
DOMAIN="tradelift.surge.sh"

trap 'rm -rf "$BUILD_DIR"' EXIT

rsync -a --delete --exclude '.git' "$REPO_DIR/" "$BUILD_DIR/"
cp "$REPO_DIR/assets/trade-lift-5-trades.pdf" "$BUILD_DIR/assets/careers.guide"

node "$REPO_DIR/scripts/generate-sitemap.js"

# Feed a newline so surge doesn't wait on TTY prompts (account already authenticated).
printf '\n' | script -qec "surge $BUILD_DIR $DOMAIN" /dev/null

echo "Deployed: https://$DOMAIN"