# Usman Syed WebDev Skill

by Usman Syed — Complete web development skill for Muse AI

**A professional website built from scratch — as if a senior web developer with 25–30 years of experience built it by hand.**

> Just say "build a website" — agents work in the background: design, build,
> check, polish — while you keep talking.

## First, understand this flow (MAIN use case)
1. **Install** — see the install steps below.
2. **Tell Muse "build a website"** — give your brief: what the business is,
   what it sells, who it is for, which pages you need, and your preferred colours/style.
3. **The skill runs in the background** — Step 1 takes the brief (and asks about anything missing),
   Step 2 plans, Step 3 builds the design system, Step 4 builds, Step 5 live-checks +
   senior review + client-ready gate.

Whatever the business — home services, a shop, a service, anything — the flow is the same.

## Install
```bash
git clone https://github.com/Gillani77556/muse-webdev.git
cd muse-webdev
bash install.sh
```

## Use — copy-paste lines
```
Use the webdev skill to build a website from scratch for my home cleaning business.
Business: home cleaning, Karachi. Services: deep cleaning, sofa cleaning, kitchen cleaning.
Phone/WhatsApp: [your number here]. Colours: blue and white, premium look.
```
```
Use the webdev skill to build a website from scratch for my clothing shop.
Shop: [shop name], Lahore. WhatsApp order button needed.
```
```
/webdev audit https://[your-site].com
/webdev redesign https://[your-site].com
/webdev fix https://[your-site].com
/webdev launch https://[your-site].com
```
Full list: [docs/USAGE.md](docs/USAGE.md) — 10 copy-paste examples.

## What it covers — 36 skills, 20 agents
- **Plan/Architecture (5):** plan, brief, architecture (+stack), audit
- **Design/Beauty (7):** design, layout, responsive, typography, animation, images, UX
- **Frontend (5):** page, frontend, forms, accessibility, content
- **Backend/Shop (5):** backend, ecommerce, local, multilang, integrations
- **Speed/Security/Quality (5):** performance, security, testing, drift, fix
- **Launch (3):** deploy, SEO basics, maintain
- **Pro +6:** senior-review, pixel-perfect, design-polish, trust, copy-expert, client-ready

## Background agents
The hub breaks the work down and sends it to the right agents in the background — the design agent designs,
the frontend agent writes the code, the performance agent checks speed, the visual
agent takes screenshots, and the senior-review agent checks everything at the end. Each works on its own
part, together, in the background. The user does not have to answer all the time.

## Quality gates (required on every site)
1. Visual — desktop + mobile screenshot, no overflow
2. Order — header, hero, sections and footer, each in its place
3. Speed — Core Web Vitals pass
4. Function — every button, link, form live-tested
5. Trust — only real information, nothing invented
6. Senior — 25-year checklist; if even one gap remains, it is not "ready"

## Rules
- Back up first; live changes only after your approval.
- Names, numbers, prices and reviews come only from you — the skill never guesses them.
- Live check + screenshot proof after every task.

## GitHub deploy steps
```bash
git init && git add . && git commit -m "muse-webdev v0.1.0"
git remote add origin https://github.com/Gillani77556/muse-webdev.git
git branch -M main && git push -u origin main
git tag v0.1.0 && git push origin v0.1.0
```
Repo name: `muse-webdev`. Branch: `main`. License: MIT. Author: Usman Syed.

## License
MIT — free, open source.
