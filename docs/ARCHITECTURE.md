# ARCHITECTURE

```
muse-webdev/
  skills/        36 skills, har ek SKILL.md (frontmatter + instructions)
  agents/        20 agents, har ek .md (name, description, model, tools)
  scripts/       Python checks, stdlib only, URL validation ke saath
  schema/        JSON-LD templates (placeholders only)
  docs/          COMMANDS, ARCHITECTURE, INSTALLATION, USAGE, TROUBLESHOOTING
  extensions/    11 optional extensions (README only, v0.1.0)
  tests/         manifest consistency + script smoke tests
  .claude-plugin/ plugin.json + marketplace.json
```

## Flow — scratch build (main use case)
1. User: "website banao" + brief.
2. Hub `webdev` brief leta hai, missing sawal poochhta hai.
3. Hub kaam todta hai aur agents ko peeche bhejta hai — design, frontend,
   performance, visual, senior-review — parallel, background mein.
4. Har agent apni report deta hai; hub unhe jod kar ek fix list banata hai.
5. Quality gates: visual, tartib, speed, function, trust, senior.
6. Client-ready gate pass ho to hi "ready" kaha jata hai.

## Models
- Sonnet: zyada tar agents. Opus (heavy): design, content, ux, drift,
  visual. Architecture skill ka kaam plan agent karta hai.
