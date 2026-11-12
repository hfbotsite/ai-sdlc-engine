---
description: Design and run testing for the current change or area
argument-hint: "[scope: module, feature, or 'full']"
skills: testing-engineering
---

Act as TeamLead.

Run testing for the specified scope.

Scope: $ARGUMENTS (default: current changes)

Use the testing-engineering skill.

Steps:

1. Identify the project's test framework and conventions; use them as-is.
2. Delegate test design and execution to the qa-engineer agent, or run
   directly for small scopes.
3. Cover: positive, negative, boundary and failure scenarios at the
   appropriate level (unit / integration / API / E2E).
4. Run affected tests first, then the relevant suite, then regression.
5. Never report a test as passed without actual execution output.

Report:

1. Test matrix (scenario → level → status)
2. Tests executed with real results
3. Defects found (severity, reproduction)
4. Coverage summary
5. Untested risks and recommended follow-ups
