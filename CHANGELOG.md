# Changelog

## v0.2.0 — 2026-11-27
- PREMIUM BUILD STANDARD (v0.2.0): every site now ships a real design system
  (CSS tokens: palette, type scale, spacing, radius, shadows), a large
  photographic hero (78vh+, real photo), REAL photos on every card/section
  (each URL verified HTTP 200 before use, Unsplash source URLs, no
  placeholder images, no lorem ipsum), a working interactive component
  (planner/calculator with live totals), full section architecture (hero,
  trust bar, services, how-it-works, why-choose-us, places, planner, FAQ,
  final CTA, footer), subtle animations (reveal on scroll, hover lift,
  200-300ms, reduced-motion respected) and mobile-first responsive. The
  senior-review gate now fails any plain site. Hub, design, design-polish,
  pixel-perfect, senior-review, layout, typography, images, animation, plan
  and brief skills updated, plus ARCHITECTURE.md and COMMANDS.md.
- AUTO MODE (default): `/webdev auto <topic>` builds a complete website from
  just a topic — no questions first. Missing name → descriptive name from the
  topic marked `[TO CONFIRM]`; missing phone → omitted, contact form instead,
  never an invented number; missing prices → sample prices labelled
  "Sample price"; missing colours → professional palette from the topic. Only a
  truly blocking fact (e.g. a live domain to deploy to) is asked. Hub, plan,
  brief, CLAUDE.md, ARCHITECTURE.md, TROUBLESHOOTING.md, README and USAGE
  updated to match.
- Full English translation: all Roman Urdu prose in README, docs, skills and agents rewritten in professional English; no behaviour change.
- Branded as the Usman Syed WebDev Skill (repo and plugin name `muse-webdev` unchanged).
- Install fix: install.sh/install.ps1 now ship the scripts/ launcher, so `webdev doctor` works after install.

## v0.1.0 — 2026-11-27
- First release: 36 skills, 20 agents, 15 Python check scripts.
- Main use case: scratch website builds for any business.
- Pro layer: senior-review, pixel-perfect, design-polish, trust, copy-expert, client-ready.
- Quality gates: visual, order, speed, function, trust, senior.
- Background-agent orchestration in hub and every agent.
