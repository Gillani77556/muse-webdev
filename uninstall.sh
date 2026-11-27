#!/usr/bin/env bash
set -euo pipefail
for d in ~/.claude/skills/webdev*; do [ -d "$d" ] && rm -rf "$d"; done
for f in ~/.claude/agents/webdev-*.md; do [ -f "$f" ] && rm -f "$f"; done
echo "muse-webdev removed."
