# Configuration

## What is configurable

### Per-project (via project `AGENTS.md`)

The TeamLead rules are generic. Project-specific configuration lives in the
target project's own `AGENTS.md`, created/updated by `/sdlc-start`:

- stack and tooling conventions (test runner, linter, build commands);
- module boundaries and architecture rules;
- branch naming and commit conventions;
- quality-gate commands for this project;
- anything the project must always do or never do.

### Engine rules

The global TeamLead rules live in two places that must stay in sync:

- `AGENTS.md` (repository root) — the readable source of truth;
- `ai-sdlc-engine/hooks/session-start.mjs` — the condensed version injected per session.

Edit the root `AGENTS.md` first, then mirror the condensed form in the hook.

### Hooks

`ai-sdlc-engine/hooks/hooks.json` registers three events (SessionStart,
PostToolUseFailure, Stop). Each hook is defensive: any error exits 0.
Timeouts are 5 s; the scripts self-terminate at 4 s regardless of stdin.

Hard access-control hooks (blocking writes to secrets, production config,
critical paths via PreToolUse) are deliberately deferred to 0.2.x; enable
them only after the base system is validated.

### Model

All agents declare `model: inherit` — they run on the session model
(e.g. GLM-5.3-Flash) with no separate per-agent model cost. Change per-agent
models only if a role demonstrably needs it; inherited models keep token
cost predictable.

### MCP

No MCP servers are bundled. Add integrations (GitHub, Jira, Database) per
project only when a real need appears; each server costs context and setup.
Local STDIO and remote HTTP/SSE servers are supported by ZCode.

## CI/CD

CI remains an external, independent system (e.g. GitHub Actions). During
`/sdlc-start`, the TeamLead determines the project's gates and wires them
into the existing CI configuration. ZCode and the Engine manage CI; they do
not replace it.
