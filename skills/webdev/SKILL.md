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
| `/webdev auto <topic>` | **Build a complete website from just a topic — AUTO MODE (default)** | webdev-plan, webdev-brief, webdev-architecture |
| `/webdev build <brief>` | New website from scratch — same as `auto`, builds immediately with defaults | webdev-plan, webdev-brief, webdev-architecture |
| `/webdev audit <url>` | Full site audit, scored, prioritised fix list | webdev-audit |
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

## AUTO MODE — the default (no questions first)
The user only gives a topic, for example "a bakery website in Lahore" or
"a travel website in Sharjah". That is enough. **Build immediately — do not
ask questions first.** The skill fills every gap itself with the defaults
below and builds the complete website in one go. The user only has to say
the topic; the system automates everything else.

### AUTO defaults — apply whenever a fact is missing
| Missing fact | Default — do this, do not ask |
|---|---|
| Business name | Use a descriptive name from the topic (e.g. topic "bakery in Lahore" → "Lahore Bakery"), marked `[TO CONFIRM]` on the site so the user can replace it. |
| Phone / WhatsApp | Omit the number entirely. Use a contact form and a `[TO CONFIRM]` placeholder for the number. Never invent a real-looking phone number. |
| Prices | Use sample prices, clearly labelled "Sample price" on every price, with one note on the page saying prices are samples. |
| Colours / style | Pick a professional palette from the topic (bakery → warm cream/brown; travel → teal/sand; cleaning → blue/white). |
| Pages | Home, Services/Tours/Products, About, FAQ, Contact. Add a shop/order page only if the topic is a shop. |
| Language | English, unless the user says otherwise. |
| Images | Use real photos of the topic/place where available; otherwise clean CSS/gradient visuals — never a fake photo of the business. |
| Reviews / testimonials | Never invent them. Omit the section entirely. |

### When to ask — only when truly blocking
Ask the user only when a fact blocks the build itself, for example a live
domain to deploy to, or a real payment/checkout account to connect. A missing
business name, phone, price or colour is **never** blocking — use the default
above and keep building. List every default used in the final report so the
user can correct it in one message.

## MAIN USE CASE — A new website from scratch (first priority)
This is the skill's biggest job: whatever the business — home services, a shop,
a service, anything — the user installs the skill, starts work in Muse, just
says "build a website", gives their topic, and the skill runs in the background.

### Scratch flow — 5 steps
1. **Take the topic** — the user only says the topic (e.g. "a bakery website
   in Lahore"). Apply the AUTO defaults above for anything missing — do not
   ask questions.
2. **Make the plan** — pages, sections, CTAs, integrations, timeline.
3. **Design system** — colors, fonts, spacing, layout — senior standard.
4. **Build** — frontend + backend + forms + content, with agents working in the background.
5. **Live check + senior review + client-ready gate** — speed, links, forms,
   screenshots — only then say "ready".

The user only has to give their topic. The skill builds the complete website
itself and automates everything. It never asks questions first.

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
have to answer all the time. An agent reports back when its work is done and does not ask
questions first — it uses the AUTO defaults in the hub skill and only stops for a
fact that truly blocks the build.

## Senior standard (25-30 years)
A visitor must understand in 5 seconds what the site does and what to do
next. Few colours, clean fonts, generous whitespace, one style everywhere,
nothing cut off, nothing invented. If it looks AI-made, it is not finished.

## Rules
- Back up first; live changes only after the user approves.
- Title, URL and content changes need an explicit yes.
- AUTO MODE is the default: never ask questions first. Missing name → descriptive
  name from the topic, marked `[TO CONFIRM]`. Missing phone → omit it, use a
  contact form / `[TO CONFIRM]` placeholder, never invent a real-looking number.
  Missing prices → sample prices labelled "Sample price". Missing colours →
  pick a professional palette from the topic. Never invent reviews or addresses.
- After every fix, re-check live and show evidence. Never say done without it.
