#!/usr/bin/env bash
# TradeLift production deploy to https://tradelift.surge.sh
# Requires: surge CLI logged in (email: tradelift056411@uberip.com, token stored in ~/.config/surge)
# NOTE: surge.sh does not serve .pdf files (404) — the lead-magnet PDF is deployed under an
# extensionless name (assets/careers.guide, served as application/octet-stream). js/main.js
# points the exit-modal download/_next to that path with download="TradeLift-Career-Fit-Guide.pdf".
set -euo pipefail

REPO_DIR="$(cd "$(dirname "${BASH_SOURCE[0]}")/.." && pwd)"
BUILD_DIR="$(mktemp -d /tmp/tradelift-deploy.XXXXXX)"
DOMAIN="tradelift.surge.sh"

trap 'rm -rf "$BUILD_DIR"' EXIT

# Regenerate the sitemap first so the fresh sitemap.xml is rsync'd into the build.
node "$REPO_DIR/scripts/generate-sitemap.js"

# Internal files stay off the public site; paid premium product + orphan PDF must not ship.
rsync -a --delete \
  --exclude '.git' \
  --exclude 'docs/' \
  --exclude 'scripts/' \
  --exclude '__pycache__/' \
  --exclude 'PROGRESS.md' \
  --exclude 'AGENTS.md' \
  --exclude 'CLAUDE.md' \
  --exclude '.pa11yci.json' \
  --exclude 'node_modules/' \
  --exclude 'package.json' \
  --exclude 'package-lock.json' \
  --exclude '/*.py' \
  --exclude '/*.md' \
  --exclude 'assets/premium/' \
  --exclude 'assets/trade-lift-5-trades.pdf' \
  "$REPO_DIR/" "$BUILD_DIR/"

# Surge serves .pdf as 404, so every roadmap PDF is also deployed under its
# extensionless name (served as application/octet-stream, same pattern as careers.guide).
for pdf in "$REPO_DIR"/assets/roadmaps/*-roadmap.pdf; do
  if [ -f "$pdf" ]; then
    cp "$pdf" "$BUILD_DIR/assets/roadmaps/$(basename "$pdf" .pdf)"
  fi
done

# Feed a newline so surge doesn't wait on TTY prompts (account already authenticated).
printf '\n' | script -qec "surge $BUILD_DIR $DOMAIN" /dev/null

echo "Deployed: https://$DOMAIN"