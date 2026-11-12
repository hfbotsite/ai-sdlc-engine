# AI SDLC Engine

Reusable AI-native software development lifecycle system for ZCode, packaged as a plugin: a TeamLead orchestration layer plus specialized engineering subagents, skills, commands, hooks and policies.

## Components (MVP 0.1.0)

| Component | Count | Location | Notes |
|---|---|---|---|
| TeamLead rules | 1 | `AGENTS.md` | Injected into every session by the SessionStart hook |
| Subagents | 6 | `ai-sdlc-engine/agents/` | All inherit the session model |
| Skills | 4 | `ai-sdlc-engine/skills/` | Only procedural knowledge not already in agent prompts |
| Commands | 8 | `ai-sdlc-engine/commands/` | Workflow entry points |
| Hooks | 3 events | `ai-sdlc-engine/hooks/` | SessionStart, PostToolUseFailure, Stop; need `node` on PATH |
| Policies | 4 | `ai-sdlc-engine/policies/` | Reference docs for the engine itself |

Deliberately deferred to 0.2.x: `performance-engineer` and `devops-release` agents, performance/devops skills, hard access-control hooks (production config, secrets, critical paths).

## Design principles

- Skills exist only where they carry procedure not already in an agent prompt: onboarding audit, test matrix, security audit classes, code-quality review checklist.
- TeamLead rules reach target projects automatically via the SessionStart hook (`additionalContext`), not via copying files; `/sdlc-start` only adds project-specific rules to the project's `AGENTS.md`.
- Independent verification: the Developer never certifies its own code; QA, Code Reviewer and Security Auditor are read-only.
- Hooks are defensive: any internal error exits 0 and never blocks the session. Real quality enforcement belongs in CI, not in hooks.

## Agents

`requirements-analyst`, `architect`, `developer`, `qa-engineer`, `code-reviewer`, `security-auditor`.

## Commands

`/sdlc-start` `/sdlc-analyze` `/sdlc-plan` `/sdlc-implement` `/sdlc-review` `/sdlc-test` `/sdlc-release` `/sdlc-status`

## Repository layout

```
ai-sdlc-engine/
├── AGENTS.md                  # TeamLead rules (source of truth)
├── marketplace.json           # local marketplace catalog (source: ./ai-sdlc-engine)
├── ai-sdlc-engine/            # the installable plugin (name = manifest name)
│   ├── .zcode-plugin/plugin.json
│   ├── agents/  skills/  commands/  hooks/  policies/
├── docs/
└── tests/                     # structural validator (stdlib Python)
```

## Installation (local marketplace)

1. ZCode → **Plugin Marketplace → Add → Add Plugin Marketplace**, paste this repository's root directory.
2. Find **AI SDLC Engine** → **Install** → enable the plugin.
3. Verify Skills, Commands and Subagents appear in Settings.

Details and update procedure: `docs/installation.md`.

## Validation

```
python tests/validate.py
```

## Versioning

Version lives in `ai-sdlc-engine/.zcode-plugin/plugin.json` and must be mirrored in `marketplace.json` and `VERSION`. Update all three on every release; document changes in `CHANGELOG.md`.
