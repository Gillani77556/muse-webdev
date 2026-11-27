# ARCHITECTURE

```
muse-webdev/
  skills/        36 skills, each with a SKILL.md (frontmatter + instructions)
  agents/        20 agents, each a .md file (name, description, model, tools)
  scripts/       Python checks, stdlib only, with URL validation
  schema/        JSON-LD templates (placeholders only)
  docs/          COMMANDS, ARCHITECTURE, INSTALLATION, USAGE, TROUBLESHOOTING
  extensions/    11 optional extensions (README only, v0.2.0)
  tests/         manifest consistency + script smoke tests
  .claude-plugin/ plugin.json + marketplace.json
```

## Flow — scratch build (main use case)
1. User: "build a website" + brief.
2. The `webdev` hub takes the topic and applies the AUTO defaults for anything missing — it never asks questions first.
3. The hub breaks the work down and sends agents to work in the background — design, frontend,
   performance, visual, senior-review — in parallel.
4. Each agent reports back; the hub joins them into one fix list.
5. Quality gates: visual, order, speed, function, trust, senior.
6. "Ready" is only said once the client-ready gate passes.

## PREMIUM BUILD STANDARD (v0.2.0) — every site, no exceptions
A plain page with text and one button is NOT a finished site. Every build
must ship all of this:
- **Design system first:** CSS tokens in `:root` — palette (max 3 colours +
  neutrals), type scale (display/H1/H2/H3/body/small), spacing scale
  8/16/24/32/48/64/96, radius 12/16/24, soft shadows. Max 2 font families.
- **Large photographic hero:** min-height 78vh, REAL photo, gradient overlay,
  headline + subhead + 2 CTAs + trust strip.
- **REAL photos everywhere:** hero + every card/section. Every image URL is
  verified HTTP 200 before use (`images.unsplash.com` with
  `?auto=format&fit=crop&w=1600&q=80`). No placeholder images, no lorem ipsum.
- **Interactive component:** working planner/calculator/filter in vanilla JS
  on every site (e.g. trip planner with live totals + WhatsApp message).
- **Full architecture:** sticky header, hero, trust bar, services grid,
  how-it-works, why-choose-us, places, planner, FAQ accordion, final CTA,
  footer.
- **Subtle motion:** IntersectionObserver reveals, card hover lift, 200-300ms,
  transform/opacity only, `prefers-reduced-motion` respected.
- **Mobile-first:** breakpoints 640/900/1200, no overflow at 360px, tap
  targets 44px+.
- **Senior-review premium gate:** photos verified, planner works, no lorem,
  no placeholders — one fail = not ready.

## Models
- Sonnet: most agents. Opus (heavy): design, content, ux, drift,
  visual. The plan agent does the architecture skill's work.
