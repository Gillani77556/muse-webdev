# INSTALLATION

> Ye file sirf repo mein hai taake jo download kare wo install kar sake.
> Repo banane wale ko install karna lazmi nahi — repo local bhi complete hai.

## Muse AI (manual install, claude-seo jaisa)
```bash
git clone https://github.com/Gillani77556/muse-webdev.git
cd muse-webdev
bash install.sh
```
`install.sh` skills ko `~/.claude/skills/` aur agents ko
`~/.claude/agents/` mein copy karta hai, version v0.1.0 par pin karta hai.

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
`{"ready": true, ...}` aana chahiye.
