# Usman Syed WebDev Skill — Structure (like claude-seo, for Web Development)

Name: muse-webdev | Version: 0.2.0 | License: MIT
Template: AgriciDaniel/claude-seo v2.6.3 — 29 skills / 20 agents / 67 scripts
Target: Muse AI — a website that is fully beautiful, well-ordered, fast and secure, with no gaps left

## Repo layout (same pattern, names changed)
```
muse-webdev/
  README.md, LICENSE, CHANGELOG.md, CLAUDE.md / AGENTS.md
  .claude-plugin/plugin.json + marketplace.json
  install.sh / install.ps1 / uninstall.sh
  skills/ (30)  agents/ (20)  scripts/ (Python + Node checks)
  schema/ (templates)  data/  docs/  extensions/ (11)  tests/
  pyproject.toml / requirements.txt
```

## Hub
- `webdev` — main hub, `/webdev [command] [url or brief]`, directs everything

## 30 Skills — no gaps left

### 1. Plan and Architecture — 5
1. `webdev-plan` — plan from business, audience, goal, pages, budget and timeline
2. `webdev-brief` — full blueprint from the client brief: pages, sections, content, CTA
3. `webdev-architecture` — folder structure, routing, components, data flow, stack
4. `webdev-stack` — static / WordPress / Next.js / Shopify / Vercel — choosing the right stack
5. `webdev-audit` — full-site audit, score and priority fix list

### 2. Design and Beauty — 7
6. `webdev-design` — design system: colors, fonts, spacing, buttons, cards
7. `webdev-layout` — hero, header, footer, sections, grid — everything in order, nothing cut off
8. `webdev-responsive` — mobile, tablet, desktop — correct on every screen
9. `webdev-typography` — font pairing, size, line-height, readability
10. `webdev-animation` — smooth animation, hover, scroll — not too much, never slows the site
11. `webdev-images` — images, icons, OG/social images, alt, size, format
12. `webdev-ux` — user flow, forms, buttons, navigation — the user never gets stuck

### 3. Frontend Build — 5
13. `webdev-page` — deep check of one page: HTML, headings, links, forms
14. `webdev-frontend` — HTML/CSS/JS, Tailwind, components, clean code
15. `webdev-forms` — forms, validation, success/error, spam protection, email
16. `webdev-accessibility` — keyboard, screen reader, contrast, focus — for everyone
17. `webdev-content` — writing, headings, CTA copy, trust signals, no wrong information

### 4. Backend, Data and Shop — 5
18. `webdev-backend` — API, database, auth, admin, saving data
19. `webdev-ecommerce` — shop, product page, cart, checkout, payment, orders
20. `webdev-local` — local business: map, phone, WhatsApp, hours, reviews, GBP
21. `webdev-multilang` — Urdu/English, RTL, language switch, hreflang
22. `webdev-integrations` — WhatsApp, Email, GA4, Maps, payment, social

### 5. Speed, Security, Quality — 5
23. `webdev-performance` — Core Web Vitals, speed, caching, lazy load
24. `webdev-security` — HTTPS, headers, safe forms, no leaks, backup
25. `webdev-testing` — every button/link/form tested, mobile test, live verify
26. `webdev-drift` — save a baseline, then catch changes later, before they become problems
27. `webdev-fix` — find the fault, fix it, live-check again

### 6. Launch and Beyond — 3
28. `webdev-deploy` — Vercel/Hostinger deploy, domain, SSL, 404, redirect
29. `webdev-seo-basic` — title, meta, sitemap, schema, robots — basics only; full SEO is a separate skill
30. `webdev-maintain` — update, backup, monitoring, monthly health check

## 20 Agents (workers — not all at once, one per task)
webdev-plan, webdev-design, webdev-layout, webdev-responsive, webdev-frontend, webdev-page, webdev-content, webdev-performance, webdev-visual, webdev-accessibility, webdev-backend, webdev-ecommerce, webdev-local, webdev-security, webdev-testing, webdev-drift, webdev-deploy, webdev-forms, webdev-images, webdev-ux
- 5 heavy ones on Opus: design, content, architecture, ux, drift — the rest on Sonnet

## Scripts (Python, like claude-seo)
fetch_page, render_page, capture_screenshot, parse_html, page_checks, performance_check, accessibility_check, broken_links, image_check, form_check, sitemap_check, schema_check, security_headers, responsive_check, drift_baseline, drift_compare, deploy_check

## Extensions (11, later)
Lighthouse, Playwright, Vercel, WordPress, Shopify, Figma, GA4, WhatsApp, Stripe/Payoneer, Image-gen, Screenshots

## Commands (examples)
- `/webdev audit <url>` — full site check
- `/webdev build <brief>` — plan + build a new site
- `/webdev redesign <url>` — make an old site beautiful
- `/webdev fix <url>` — find and fix faults
- `/webdev page <url>` — ek page
- `/webdev speed <url>` — speed
- `/webdev launch <url>` — final check before deploy

## Rules in this skill
- Back up first, live changes afterwards
- Title/URL/content changes only with your approval
- Never invent anything — names, numbers and prices only as you provide them
- Live verification after every task, with a screenshot

## ENHANCE — 25-30 Saal Expert Level (Pro Layer, 27 Nov)
Goal: looking at the site should feel like a senior web developer with 25–30 years of experience designed and built it by hand — no AI-made feel.

### Naye Pro Skills — +6 (total 36 skills)
31. `webdev-senior-review` — final review through a senior developer's eyes: every section, every gap, every alignment
32. `webdev-pixel-perfect` — pixel-perfect check: spacing, alignment, overflow, cut-off text, nothing hidden on mobile
33. `webdev-design-polish` — premium polish: colour balance, contrast, whitespace, hierarchy — order, everything in its place
34. `webdev-trust` — trust signals: real reviews, real numbers, proof, CTA — no false praise, nothing invented
35. `webdev-copy-expert` — expert copy: headline, sub-headline, CTA — short, clear, easy for the client to understand
36. `webdev-client-ready` — final gate before sending to the client: all pages return 200, all links work, all forms tested, speed passes, screenshot proof

### Pro Quality Gates (required on every site — the skill checks them itself)
1. Visual gate: desktop + mobile screenshots, scroll up and down, no overflow, no cut-off text
2. Order gate: header, hero, sections, footer — everything in its place, even spacing
3. Speed gate: Core Web Vitals pass, images optimised, no overly heavy fonts
4. Function gate: every button, link, form, WhatsApp, phone — tested with a live click
5. Trust gate: only real information — names, numbers, prices, reviews — exactly as you provide them
6. Senior gate: `webdev-senior-review` goes through a 25-year developer's checklist itself — if even one gap remains, it will not say "ready"

### Senior Developer Persona (written into the skill)
- Thinking: first what the user wants, then design, then code — never the other way round
- Design: few colours, clean fonts, generous whitespace, one style on every page
- Code: clean, clear names, no repetition, fast load
- Client view: the moment the site opens it is clear — whose work this is, what it sells, and what to do next

## GitHub Deploy (as AgriciDaniel did it)
1. New public repo on GitHub: `muse-webdev` — README, LICENSE MIT, CHANGELOG
2. Same layout: skills/, agents/, scripts/, docs/, tests/, .claude-plugin/
3. Release tag v0.1.0, then install with install.sh
4. Status: published 27 Nov 2026 as a public repo at `github.com/Gillani77556/muse-webdev`. Install from the v0.1.0 release tag with `bash install.sh`.
