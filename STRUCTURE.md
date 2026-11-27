# Muse WebDev — Dhancha (claude-seo jaisa, Web Development ke liye)

Naam: muse-webdev | Version: 0.1.0 draft | License: MIT
Template: AgriciDaniel/claude-seo v2.6.3 — 29 skills / 20 agents / 67 scripts
Target: Muse AI — website poori tarah beautiful, tartib wali, fast, secure, koi kami na rahe

## Repo layout (waisa hi, naam badal kar)
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
- `webdev` — main hub, `/webdev [command] [url ya brief]`, sab ko order deta hai

## 30 Skills — koi kami na rahe

### 1. Plan aur Architecture — 5
1. `webdev-plan` — business, audience, goal, pages, budget, timeline se plan
2. `webdev-brief` — client brief se poora blueprint: pages, sections, content, CTA
3. `webdev-architecture` — folder structure, routing, components, data flow, stack
4. `webdev-stack` — static / WordPress / Next.js / Shopify / Vercel — sahi stack chunna
5. `webdev-audit` — poori site ka audit, score aur priority fix list

### 2. Design aur Beauty — 7
6. `webdev-design` — design system: colors, fonts, spacing, buttons, cards
7. `webdev-layout` — hero, header, footer, sections, grid — tartib, kuch kata hua na ho
8. `webdev-responsive` — mobile, tablet, desktop — har screen par sahi
9. `webdev-typography` — font pairing, size, line-height, readability
10. `webdev-animation` — smooth animation, hover, scroll — zyada na ho, slow na kare
11. `webdev-images` — images, icons, OG/social images, alt, size, format
12. `webdev-ux` — user flow, forms, buttons, navigation — user atke nahi

### 3. Frontend Build — 5
13. `webdev-page` — ek page ki gehri checking: HTML, headings, links, forms
14. `webdev-frontend` — HTML/CSS/JS, Tailwind, components, clean code
15. `webdev-forms` — forms, validation, success/error, spam protection, email
16. `webdev-accessibility` — keyboard, screen reader, contrast, focus — sab ke liye
17. `webdev-content` — likhai, headings, CTA copy, trust signals, koi ghalat info nahi

### 4. Backend, Data aur Shop — 5
18. `webdev-backend` — API, database, auth, admin, data save karna
19. `webdev-ecommerce` — shop, product page, cart, checkout, payment, orders
20. `webdev-local` — local business: map, phone, WhatsApp, hours, reviews, GBP
21. `webdev-multilang` — Urdu/English, RTL, language switch, hreflang
22. `webdev-integrations` — WhatsApp, Email, GA4, Maps, payment, social

### 5. Speed, Security, Quality — 5
23. `webdev-performance` — Core Web Vitals, speed, caching, lazy load
24. `webdev-security` — HTTPS, headers, forms safe, koi leak nahi, backup
25. `webdev-testing` — har button/link/form test, mobile test, live verify
26. `webdev-drift` — baseline save karke bad mein change pakadna, kharabi se pehle
27. `webdev-fix` — kharabi dhoondhna, fix karna, dobara live check karna

### 6. Launch aur Aage — 3
28. `webdev-deploy` — Vercel/Hostinger deploy, domain, SSL, 404, redirect
29. `webdev-seo-basic` — title, meta, sitemap, schema, robots — sirf basic, poora SEO alag skill hai
30. `webdev-maintain` — update, backup, monitoring, monthly health check

## 20 Agents (worker, ek saath nahi, kaam ke hisab se ek)
webdev-plan, webdev-design, webdev-layout, webdev-responsive, webdev-frontend, webdev-page, webdev-content, webdev-performance, webdev-visual, webdev-accessibility, webdev-backend, webdev-ecommerce, webdev-local, webdev-security, webdev-testing, webdev-drift, webdev-deploy, webdev-forms, webdev-images, webdev-ux
- 5 heavy Opus par: design, content, architecture, ux, drift — baaki Sonnet par

## Scripts (Python, claude-seo jaisa)
fetch_page, render_page, capture_screenshot, parse_html, page_checks, performance_check, accessibility_check, broken_links, image_check, form_check, sitemap_check, schema_check, security_headers, responsive_check, drift_baseline, drift_compare, deploy_check

## Extensions (11, baad mein)
Lighthouse, Playwright, Vercel, WordPress, Shopify, Figma, GA4, WhatsApp, Stripe/Payoneer, Image-gen, Screenshots

## Commands (misal)
- `/webdev audit <url>` — poori site check
- `/webdev build <brief>` — nayi site ka plan + build
- `/webdev redesign <url>` — purani site ko beautiful karna
- `/webdev fix <url>` — kharabi dhoondhna aur fix
- `/webdev page <url>` — ek page
- `/webdev speed <url>` — speed
- `/webdev launch <url>` — deploy se pehle final check

## Rule jo isme hoga
- Backup pehle, live change baad mein
- Title/URL/content change sirf aapki haan se
- Koi cheez invent nahi — naam, number, price sirf wohi jo aap dein
- Har kaam ke baad live verify, screenshot ke sath

## ENHANCE — 25-30 Saal Expert Level (Pro Layer, 27 Nov)
Maqsad: site dekh kar lage ke 25-30 saal ke senior web developer ne khud design aur build ki hai, AI wali feel na aaye.

### Naye Pro Skills — +6 (total 36 skills)
31. `webdev-senior-review` — senior developer ki nazar se final review: har section, har gap, har alignment
32. `webdev-pixel-perfect` — pixel-perfect check: spacing, alignment, overflow, kata hua text, mobile par kuch chhupa hua na ho
33. `webdev-design-polish` — premium polish: color balance, contrast, whitespace, hierarchy — tartib, sab kuch apni jagah
34. `webdev-trust` — trust signals: real reviews, real numbers, proof, CTA — koi jhoothi taareef, koi invent ki hui cheez nahi
35. `webdev-copy-expert` — expert copy: headline, sub-headline, CTA — chhota, saaf, client ko samajh aaye
36. `webdev-client-ready` — client ko bhejne se pehle final gate: sab pages 200, sab links kaam karein, sab forms test, speed pass, screenshot proof

### Pro Quality Gates (har site par lazmi, skill khud check karegi)
1. Visual gate: desktop + mobile screenshot, upar-neeche scroll, koi overflow nahi, koi text kata nahi
2. Tartib gate: header, hero, sections, footer — har cheez apni jagah, gap barabar
3. Speed gate: Core Web Vitals pass, images optimize, font zyada heavy nahi
4. Function gate: har button, link, form, WhatsApp, phone — live click karke test
5. Trust gate: sirf real info — naam, number, price, review — jo aap dein wohi
6. Senior gate: `webdev-senior-review` khud 25 saal ke developer ki checklist se guzre — agar ek bhi kami ho to "ready" nahi kahega

### Senior Developer Persona (skill ke andar likha hoga)
- Soch: pehle user kya chahta hai, phir design, phir code — ulta nahi
- Design: kam color, saaf font, zyada whitespace, ek hi style har page par
- Code: clean, naam saaf, repeat nahi, fast load
- Client nazar: site kholte hi samajh aaye — ye kis ka kaam hai, kya bechta hai, ab kya karein

## GitHub Deploy (jaisa AgriciDaniel ne kiya tha)
1. GitHub par naya public repo: `muse-webdev` — README, LICENSE MIT, CHANGELOG
2. Waisa hi layout: skills/, agents/, scripts/, docs/, tests/, .claude-plugin/
3. Release tag v0.1.0, phir install.sh se install
4. Blocker (sach): GitHub par repo banane/push karne ke liye aapko pehle Muse ko repo access dena hoga — 5 Nov ko connection hua tha, repo choose karna abhi baaki hai. Is liye pehle poori skill local banegi, phir aapki haan aur repo access ke baad GitHub par jayegi.
