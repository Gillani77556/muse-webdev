# ARCHITECTURE

```
muse-webdev/
  skills/        36 skills, each with a SKILL.md (frontmatter + instructions)
  agents/        20 agents, each a .md file (name, description, model, tools)
  scripts/       Python checks, stdlib only, with URL validation
  schema/        JSON-LD templates (placeholders only)
  docs/          COMMANDS, ARCHITECTURE, INSTALLATION, USAGE, TROUBLESHOOTING
  extensions/    11 optional extensions (README only, v0.1.0)
  tests/         manifest consistency + script smoke tests
  .claude-plugin/ plugin.json + marketplace.json
```

## Flow — scratch build (main use case)
1. User: "build a website" + brief.
2. The `webdev` hub takes the brief and asks about anything missing.
3. The hub breaks the work down and sends agents to work in the background — design, frontend,
   performance, visual, senior-review — in parallel.
4. Each agent reports back; the hub joins them into one fix list.
5. Quality gates: visual, order, speed, function, trust, senior.
6. "Ready" is only said once the client-ready gate passes.

## Models
- Sonnet: most agents. Opus (heavy): design, content, ux, drift,
  visual. The plan agent does the architecture skill's work.
