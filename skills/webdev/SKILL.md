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
| `/webdev build <brief>` | **Scratch se nayi website — MAIN use case** | webdev-plan, webdev-brief, webdev-architecture |
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

## MAIN USE CASE — Scratch se nayi website (pehle number par)
Ye skill ka sab se bara kaam hai: koi bhi business ho — home, dukaan,
service, koi bhi — banda skill install karke Muse mein kaam shuru kare, bas
bole "website banao", apna program/brief de, aur peeche ye skill chale.

### Scratch flow — 5 steps
1. **Brief lo** — business kya hai, kya bechta hai, kiske liye hai, pages
   kaunse, color/style pasand hai. Jo missing ho, skill khud poochhe.
2. **Plan banao** — pages, sections, CTAs, integrations, timeline.
3. **Design system** — colors, fonts, spacing, layout — senior standard.
4. **Build** — frontend + backend + forms + content, agents peeche kaam karein.
5. **Live check + senior review + client-ready gate** — speed, links, forms,
   screenshots, phir hi "ready" kaho.

User ko sirf apna brief dena hai. Skill khud poochhe jo missing ho, invent
na kare. Agar user ne sirf "website banao" kaha ho, to pehle 5-6 sawal poochho
(webdev-plan / webdev-brief dekho), phir aage badho.

## How the hub works
1. Read the command and route to the matching sub-skill above.
2. Run ONE agent per task — agents never run all at once.
3. Collect findings into one prioritised fix list with evidence.
4. Run the Pro gates (senior-review, pixel-perfect, client-ready) before
   calling anything ready.

## Background agents — peeche kaam, aap baat karte raho
Aap bas "website banao" bolo — peeche agents kaam karenge: design, build,
check, polish. Aap baat karte raho, agents peeche apna hissa karte rahen.
Jaise claude-seo audit mein agents parallel kaam karte the, waise hi yahan
scratch build mein: design agent design kare, frontend agent code likhe,
performance agent speed check kare, visual agent screenshot le, senior-review
agent aakhir mein check kare — sab apne apne hisse par, ek saath, peeche.
Hub kaam ko tod kar sahi agents ko peeche bhejta hai; user ko har waqt jawab
nahi dena parta. Agent apna kaam karke report deta hai, user se baar baar
sawal nahi poochhta — sirf jo missing ho, wohi poochhta hai.

## Senior standard (25-30 years)
A visitor must understand in 5 seconds what the site does and what to do
next. Few colours, clean fonts, generous whitespace, one style everywhere,
nothing cut off, nothing invented. If it looks AI-made, it is not finished.

## Rules
- Back up first; live changes only after the user approves.
- Title, URL and content changes need an explicit yes.
- Never invent names, phones, prices, reviews or addresses — `[TO CONFIRM]`.
- After every fix, re-check live and show evidence. Never say done without it.
