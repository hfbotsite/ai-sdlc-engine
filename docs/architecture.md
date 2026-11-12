# Architecture

## Purpose

AI SDLC Engine is an engineering add-on over ZCode, not a replacement for it.
It turns the ZCode agent into a managed development team: a TeamLead layer
coordinating specialized subagents, with skills carrying procedural knowledge
and commands as workflow entry points.

## Layers

```
User
  │
  ▼
ZCode main agent ── TeamLead role (rules injected by SessionStart hook,
  │                  refined per project by /sdlc-start → project AGENTS.md)
  │
  ├── Subagents (agents/): requirements-analyst, architect, developer,
  │        qa-engineer, code-reviewer, security-auditor
  │        All inherit the session model; reviewers are read-only by contract.
  │
  ├── Skills (skills/): only procedural knowledge not present in agent prompts:
  │        project-onboarding, testing-engineering, security-engineering,
  │        code-quality-engineering
  │
  ├── Commands (commands/): /sdlc-* workflow entry points; thin scripts,
  │        not agents; may auto-mount skills.
  │
  ├── Hooks (hooks/): session-start (injects TeamLead rules),
  │        tool-failure (diagnostic hint), stop (evidence reminder).
  │        Defensive: never block the session.
  │
  └── CI/CD (external): the real enforcement layer for quality gates.
```

## Key decisions

1. **TeamLead is the main agent, not a subagent.** Subagents cannot spawn
   other subagents; only the main agent coordinates the team.
2. **Rules reach projects via hook injection**, not via file copying:
   the engine's root `AGENTS.md` is not read in target projects.
   `/sdlc-start` adds project-specific rules to the project's own `AGENTS.md`.
3. **Skills are minimal (4).** Every candidate skill that duplicated an
   agent prompt or a command was folded into that agent/command instead.
   Rationale: skill metadata loads into every turn's context; fewer,
   sharper skills improve recognition and save tokens (GLM-5.3-Flash).
4. **Independent verification by contract.** The developer never certifies
   its own code; qa/code-reviewer/security-auditor validate and review.
   Enforced via prompts now; tool-level permissions later.
5. **Hooks nudge, CI enforces.** Hooks inject context and reminders with
   defensive exit-0 semantics; blocking access control (production config,
   secrets, critical paths) is deferred to 0.2.x after base validation.
6. **Minimal team selection.** TeamLead must choose the smallest sufficient
   set of agents per task; launching the full team for small work is a
   process violation.

## Deferred (0.2.x)

- `performance-engineer`, `devops-release` agents
- performance / devops-release skills
- PreToolUse access-control hooks (secrets, production config, critical paths)
- Project Knowledge Base, Task Registry, Cost Tracker, Evaluation Agent

## Repository vs distribution

`ai-sdlc-engine` is the development repository. The installable unit is
`ai-sdlc-engine/`, distributed via `marketplace.json` (source `./plugin`).
Version is synchronized across `plugin.json`, `marketplace.json`, `VERSION`.
