---
name: webdev
description: "Hub for full web development in Muse AI. Full site audits, new builds, redesigns, fixes, speed, security and client-ready launch. Use this hub when the web-dev task is clear but the sub-skill is not; otherwise use the specific webdev-* skill."
user-invocable: true
argument-hint: "[command] [url or brief]"
license: MIT
metadata:
  author: Usman Syed
  version: "0.1.0"
  category: webdev
---

# WebDev: Full Web Development Hub

**Invocation:** `/webdev $ARGUMENTS` — first word is the command, the rest is
the URL or brief. Run checks through
`"$HOME/.claude/skills/webdev/scripts/webdev" run <script.py> <url>`.

## Commands

| Command | What it does | Skill |
|---|---|---|
| `/webdev build <brief>` | **New website from scratch — MAIN use case** | webdev-plan, webdev-brief, webdev-architecture |
| `/webdev audit <url>` | Full site audit, scored, prioritised fix list | webdev-audit |
| `/webdev build <brief>` | New site: plan + architecture + build | webdev-plan, webdev-brief, webdev-architecture |
| `/webdev redesign <url>` | Old site made beautiful, same content unless approved | webdev-design, webdev-layout, webdev-design-polish |
| `/webdev fix <url>` | Find the fault, fix it, re-check live | webdev-fix |
| `/webdev page <url>` | Deep single-page check | webdev-page |
| `/webdev speed <url>` | Speed and Core Web Vitals | webdev-performance |
| `/webdev launch <url>` | Deploy-ready final check | webdev-deploy, webdev-client-ready |
| `/webdev plan <brief>` | Build plan from a brief | webdev-plan |
| `/webdev design <url>` | Design system review | webdev-design |
| `/webdev responsive <url>` | Mobile/tablet/desktop check | webdev-responsive |
| `/webdev forms <url>` | Forms tested end to end | webdev-forms |
| `/webdev security <url>` | HTTPS, headers, safe forms | webdev-security |
| `/webdev drift baseline <url>` | Save baseline | webdev-drift |
| `/webdev drift compare <url>` | Compare with baseline | webdev-drift |
| `/webdev senior-review <url>` | Senior-developer final review | webdev-senior-review |
| `/webdev client-ready <url>` | Final gate before sending to a client | webdev-client-ready |

## MAIN USE CASE — A new website from scratch (first priority)
This is the skill's biggest job: whatever the business — home services, a shop,
a service, anything — the user installs the skill, starts work in Muse, just
says "build a website", gives their brief, and the skill runs in the background.

### Scratch flow — 5 steps
1. **Take the brief** — what the business is, what it sells, who it is for, which pages
   are needed, preferred colours/style. The skill asks about anything missing itself.
2. **Make the plan** — pages, sections, CTAs, integrations, timeline.
3. **Design system** — colors, fonts, spacing, layout — senior standard.
4. **Build** — frontend + backend + forms + content, with agents working in the background.
5. **Live check + senior review + client-ready gate** — speed, links, forms,
   screenshots — only then say "ready".

The user only has to give their brief. The skill asks about anything missing itself and never
invents anything. If the user has only said "build a website", first ask 5–6 questions
(see webdev-plan / webdev-brief), then move on.

## How the hub works
1. Read the command and route to the matching sub-skill above.
2. Run ONE agent per task — agents never run all at once.
3. Collect findings into one prioritised fix list with evidence.
4. Run the Pro gates (senior-review, pixel-perfect, client-ready) before
   calling anything ready.

## Background agents — working in the background while you talk
Just say "build a website" — the agents work in the background: design, build,
check, polish. You keep talking while the agents do their part in the background.
Just as agents worked in parallel in a claude-seo audit, here in a
scratch build: the design agent designs, the frontend agent writes the code, the
performance agent checks speed, the visual agent takes screenshots, and the senior-review
agent checks everything at the end — each on its own part, together, in the background.
The hub breaks the work down and sends it to the right agents in the background; the user does not
have to answer all the time. An agent reports back when its work is done and does not keep asking
questions — it only asks about what is missing.

## Senior standard (25-30 years)
A visitor must understand in 5 seconds what the site does and what to do
next. Few colours, clean fonts, generous whitespace, one style everywhere,
nothing cut off, nothing invented. If it looks AI-made, it is not finished.

## Rules
- Back up first; live changes only after the user approves.
- Title, URL and content changes need an explicit yes.
- Never invent names, phones, prices, reviews or addresses — `[TO CONFIRM]`.
- After every fix, re-check live and show evidence. Never say done without it.
