# TROUBLESHOOTING

## The skill is not showing up
- Check whether `~/.claude/skills/webdev/SKILL.md` exists.
- Run `bash install.sh` again, then restart Muse.

## `webdev doctor` returns ready: false
- Python 3.11 or higher is required: check with `python3 --version`.

## A script is not fetching a URL
- The URL must start with `http://` or `https://` and be a public host.
- Private/localhost URLs are blocked (SSRF guard) — this is deliberate.

## The agent keeps asking questions
- Put the business, services, phone/WhatsApp and colours in the brief; the skill will ask once
  about anything missing, then move on.

## Something looks invented
- Report it: the skill must only use the information you gave. Anything missing
  should be `[TO CONFIRM]`, never guessed.
