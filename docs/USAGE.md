# USAGE — How to use this skill in Muse AI

by Usman Syed — Complete web development skill for Muse AI

> Just say "build a website" — agents work in the background: design, build,
> check, polish — while you keep talking.

## First: install (once)
```bash
git clone https://github.com/Gillani77556/muse-webdev.git
cd muse-webdev
bash install.sh
```
Then open Muse and write one of the lines below.

## MAIN USE CASE — A new website from scratch (first)
Give only the topic — for example `/webdev auto a bakery website in Lahore` —
and the skill builds the complete website itself, with no questions first.
It applies sensible defaults for anything missing: a descriptive name marked
`[TO CONFIRM]`, sample prices labelled "Sample price", a contact form instead
of an invented phone number, and a professional colour palette from the topic.
It only asks when a fact truly blocks the build, for example a live domain to
deploy to. Give more detail if you want and the skill uses your real details
instead of the defaults.

### Example 0 — Topic only (AUTO MODE)
```
/webdev auto a bakery website in Lahore
```
That is the whole brief. The skill plans, designs, builds and checks in the
background — no questions first.

### Example 1 — Home cleaning business
```
Use the webdev skill to build a website from scratch for my home cleaning business.
Business: home cleaning, Karachi. Services: deep cleaning,
sofa cleaning, kitchen cleaning. Phone/WhatsApp: [your number here].
Colours: blue and white, clean and premium look.
```

### Example 2 — Shop
```
Use the webdev skill to build a website from scratch for my clothing shop.
Shop: [shop name], Lahore. Products: men's and women's
clothing. I will give the price list later. WhatsApp order button needed.
```

### Example 3 — Service (plumber / electrician / salon)
```
Use the webdev skill to build a website from scratch for my plumbing service.
Service: home plumbing, 24 hours. Area: Islamabad.
Phone: [your number here]. Customers should be able to call or WhatsApp straight away.
```

In the background the skill will: Step 1 take the topic and apply the AUTO
defaults for anything missing (no questions first), Step 2 plan,
Step 3 build the design system, Step 4 build, Step 5 live-check + senior review +
client-ready gate. You do not have to answer all the time.

## Other commands (copy-paste)
0. AUTO (topic only): `/webdev auto a bakery website in Lahore` — the skill
   builds the complete website itself, no questions first.
1. Audit: `/webdev audit https://[your-site].com`
2. Redesign: `/webdev redesign https://[your-site].com` — make the old site
   beautiful, keep the content as it is unless I say otherwise.
3. Fix: `/webdev fix https://[your-site].com` — find the fault and fix it.
4. One page: `/webdev page https://[your-site].com/services`
5. Speed: `/webdev speed https://[your-site].com`
6. Launch: `/webdev launch https://[your-site].com` — final check before sending to the client.
7. Senior review: `/webdev senior-review https://[your-site].com`
8. In plain words: `use the webdev skill to audit my site: https://[your-site].com`
9. In plain words: `use the webdev skill to check my site on mobile — is anything cut off?`
10. In plain words: `use the webdev skill to test my site's speed and forms`

## Rules
- AUTO MODE is the default: give only the topic and the skill builds the
  complete website itself, no questions first. Missing name → descriptive name
  from the topic, marked `[TO CONFIRM]`. Missing phone → omitted, contact form
  instead; never invent a real-looking number. Missing prices → sample prices
  labelled "Sample price". Missing colours → professional palette from the topic.
- Real business information (name, number, price, reviews) comes only from you
  when you give it — the skill never guesses a real-looking fact. Reviews are
  never invented; the section is omitted.
- Back up first; live changes only after your approval.
- Live check + screenshot proof after every task.
