# TROUBLESHOOTING

## Skill nazar nahi aa rahi
- Check karo `~/.claude/skills/webdev/SKILL.md` maujood hai ya nahi.
- Dobara `bash install.sh` chalao, phir Muse restart karo.

## `webdev doctor` ready false de
- Python 3.11 ya upar chahiye: `python3 --version` check karo.

## Script URL fetch nahi kar raha
- URL `http://` ya `https://` se shuru hona chahiye, public host hona chahiye.
- Private/localhost URL block hota hai (SSRF guard) — ye jaan boojh kar hai.

## Agent baar baar sawal poochhe
- Brief mein business, services, phone/WhatsApp aur color de do; jo missing
  hoga skill ek dafa poochhegi, phir aage badhegi.

## Koi cheez invent hui lage
- Report karo: skill ko sirf aapki di hui maloomat use karni hai. Missing
  cheez `[TO CONFIRM]` honi chahiye, guess nahi.
