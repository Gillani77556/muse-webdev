# INSTALLATION

> This file is only in the repo so that anyone who downloads it can install it.
> The repo author does not have to install it — the repo is complete on its own.

## Muse AI (manual install, like claude-seo)
```bash
git clone https://github.com/Gillani77556/muse-webdev.git
cd muse-webdev
bash install.sh
```
`install.sh` copies skills to `~/.claude/skills/` and agents to
`~/.claude/agents/`, pinned to version v0.1.0.

## Windows
```powershell
.\install.ps1
```

## Uninstall
```bash
bash uninstall.sh
```

## Check
```bash
~/.claude/skills/webdev/scripts/webdev doctor
```
You should see `{"ready": true, ...}`.
