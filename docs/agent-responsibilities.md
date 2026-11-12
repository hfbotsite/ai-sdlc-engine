# Agent Responsibilities

All agents inherit the session model. Boundaries matter more than capabilities:
each agent has a mandate and explicit prohibitions.

| Agent | Mandate | Read-only? | Key prohibitions |
|---|---|---|---|
| `requirements-analyst` | FR/NFR, acceptance criteria, edge cases, open questions | yes | Do not invent requirements; do not hide gaps as assumptions |
| `architect` | Design, contracts, data model, ADRs, trade-offs | yes | Do not redesign without justifying against existing patterns |
| `developer` | Implement within scope, with tests, honest reporting | no | No scope creep; no disabling tests/checks; no fabricated results |
| `qa-engineer` | Independent validation, test matrix, defect reports | writes test code only | No product-code fixes; no weakened assertions; evidence mandatory |
| `code-reviewer` | Independent correctness/quality review with file:line findings | yes | Not a rubber stamp; zero-findings verdicts are valid |
| `security-auditor` | Security audit by classes with severity and remediation | yes | No severity inflation; clean classes reported explicitly |

## Coordination rules

- Only the main agent (TeamLead) spawns subagents; subagents never nest.
- Parallel execution only for independent tasks; never two agents editing
  the same files simultaneously.
- Every delegation includes: task ID, objective, context, scope, files,
  constraints, expected result, acceptance criteria, required tests.
- Defects found by QA/reviewers route back through the TeamLead to the
  developer; the developer fixes or explains why a finding is not applicable.
- Minimal team selection per task type:

| Task type | Team |
|---|---|
| Formatting / typo | developer |
| Business logic | developer + qa-engineer + code-reviewer |
| Architecture | requirements-analyst + architect + developer + qa-engineer |
| Auth / security-related | architect + developer + qa-engineer + security-auditor |
| Release | qa-engineer + security-auditor |
