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
- It should not: AUTO MODE is the default. The skill builds from the topic
  alone and only asks when a fact truly blocks the build (for example a live
  domain to deploy to). If it still asks first, check that the installed copy
  is the latest: run `bash install.sh` again, then restart Muse.

## Something looks invented
- Report it: the skill must only use the information you gave. Anything missing
  should be `[TO CONFIRM]`, never guessed.
