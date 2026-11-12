---
name: project-onboarding
description: Use when starting work on an unfamiliar project or auditing its current state: repository structure, tech stack, dependencies, architecture, tests, CI/CD, security posture and documentation gaps.
---

# PROJECT ONBOARDING

## Objective

Produce a project profile that the TeamLead uses in all subsequent
tasks, without making any changes to the project.

## Workflow

1. Inspect repository structure and identify the project type.
2. Determine language, frameworks, key dependencies and their versions.
3. Locate configuration: package manifests, build config, environments, Docker.
4. Check Git state: remotes, branches, current branch, uncommitted work.
5. Find existing documentation (README, AGENTS.md, docs/, ADRs).
6. Map the architecture: entry points, key modules, external integrations.
7. Find tests and estimate what they cover.
8. Check CI/CD presence and what it runs.
9. Check security configuration: secrets handling, .gitignore, env files.
10. Identify missing engineering practices (no tests, no CI, no lint, etc.).
11. Create or update the project profile document; propose additions to the
    project's `AGENTS.md` (stack rules, boundaries, commands) for user approval.

## Constraints

- Read-only during onboarding; no code or configuration changes.
- Tooling detection is per-stack: do not assume Python tooling in a JS
  project or vice versa; use what the project already has.
- Do not install anything.

## Output

1. Project overview
2. Technology stack (with versions)
3. Architecture and critical modules
4. Existing test strategy
5. CI/CD status
6. Security risks
7. Technical debt
8. Missing engineering practices
9. Recommended improvements (ordered, with effort estimate)

Wait for user approval before implementing any improvement.
