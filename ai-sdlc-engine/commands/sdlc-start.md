---
description: Initialize or inspect a software project (onboarding audit)
argument-hint: "[project path or audit scope]"
skills: project-onboarding
---

Act as TeamLead.

Initialize or inspect the current project.

Scope: $ARGUMENTS

Use the project-onboarding skill. Delegate independent read-only
research to the appropriate agents (architect for structure, security-auditor
for security posture).

Inspect:

- Repository structure
- Tech stack and dependencies
- Architecture and critical modules
- Database and external APIs
- Tests and coverage
- CI/CD
- Security configuration
- Documentation
- Deployment process

Do not make architectural or code changes during initial onboarding.

Create or update the project profile. Propose additions to this project's
`AGENTS.md` (stack rules, module boundaries, common commands) — apply them
only after user approval.

Report:

1. Project overview
2. Technology stack
3. Architecture
4. Critical modules
5. Existing test strategy
6. CI/CD status
7. Security risks
8. Technical debt
9. Missing engineering practices
10. Recommended improvements

Wait for approval before implementing any improvement.
