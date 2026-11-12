---
description: Show current state: tasks, quality, risks, next steps
argument-hint: "[area: tasks, quality, all]"
---

Act as TeamLead.

Report the current state of work.

Area: $ARGUMENTS (default: all)

Gather from the current session and project state:

1. Tasks: active, completed, blocked (with IDs and status)
2. Changes in flight (branches, uncommitted work)
3. Last validation results actually executed (tests, lint, security)
4. Open review or security findings
5. Known risks and technical debt
6. Recommended next steps

Only report facts you can verify from the session or the repository.
If a check has not been run, report it as "not run", never as passed.
