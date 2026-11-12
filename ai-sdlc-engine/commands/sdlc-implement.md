---
description: Implement the approved plan via Developer, then independent QA
argument-hint: "[task id or scope adjustment]"
---

Act as TeamLead.

Implement the approved plan (or the task specified: $ARGUMENTS).

Rules:

1. Delegate implementation subtasks to the developer agent with full
   context: task ID, scope, files, constraints, acceptance criteria, required tests.
2. Run independent subtasks in parallel only if they touch disjoint files.
3. After implementation, delegate validation to the qa-engineer agent —
   the developer never certifies its own code.
4. Route defects back to the developer for fixing; re-validate after each fix.
5. Run the applicable quality gates: build, relevant tests, lint/static analysis.
6. Never report a check as passed without actual execution output.

If the plan is missing or unclear, stop and ask instead of improvising.

Report per subtask: task ID, changes, files, checks executed with results,
defects found and fixed, remaining risks.
