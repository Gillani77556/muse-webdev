#!/usr/bin/env bash
set -euo pipefail
# Muse WebDev installer (mirrors claude-seo install.sh pattern).
# Copies skills to ~/.claude/skills and agents to ~/.claude/agents.
# Run ONLY after you have cloned this repo yourself.
REPO_TAG="${MUSE_WEBDEV_TAG:-v0.1.0}"
SKILL_DIR="${HOME}/.claude/skills/webdev"
AGENT_DIR="${HOME}/.claude/agents"
echo "Installing muse-webdev ${REPO_TAG} ..."
mkdir -p "${SKILL_DIR}" "${AGENT_DIR}"
cp -r skills/webdev/* "${SKILL_DIR}/"
for d in skills/*/; do
  name=$(basename "${d}")
  mkdir -p "${HOME}/.claude/skills/${name}"
  cp -r "${d}"* "${HOME}/.claude/skills/${name}/"
done
cp agents/*.md "${AGENT_DIR}/"
# Copy shared scripts + launcher (CRITICAL: hub SKILL.md runs checks via
# "$HOME/.claude/skills/webdev/scripts/webdev" — without this, doctor and
# every check command fail after install. Same pattern as claude-seo.)
mkdir -p "${SKILL_DIR}/scripts"
cp -r scripts/* "${SKILL_DIR}/scripts/"
chmod +x "${SKILL_DIR}/scripts/webdev" 2>/dev/null || true
# Copy deterministic data files consumed by bundled scripts.
if [ -d data ]; then
  mkdir -p "${SKILL_DIR}/data"
  cp -r data/* "${SKILL_DIR}/data/" 2>/dev/null || true
fi
mkdir -p "${SKILL_DIR}/schema"
cp -r schema/* "${SKILL_DIR}/schema/" 2>/dev/null || true
echo "Done. Check: ${SKILL_DIR}/scripts/webdev doctor"
