---
name: code-quality-engineering
description: Use when reviewing, inspecting or validating code quality: static analysis, AST/structure, complexity, duplication, dead code, architecture boundary violations, coding standards compliance.
---

# CODE QUALITY ENGINEERING

## Objective

Ensure changed code is maintainable, consistent and compliant with
project standards — without introducing regressions.

## Workflow

1. Inspect the changed files, their callers and their dependencies.
2. Identify the language and the project's configured tooling.
3. Run configured linters, formatters and static analyzers; capture real output.
4. Analyze structural issues: duplication, dead code, unused exports.
5. Assess complexity of changed functions (cyclomatic / nesting depth);
   flag functions that are hard to test.
6. Check architectural boundaries: layering, dependency direction, module contracts.
7. Identify code smells that matter (hidden coupling, shotgun surgery,
   primitive obsession where it hurts).
8. Recommend or implement justified refactoring only within the task scope.
9. Re-run tests after any modification.

## Quality criteria

- No unexplained critical warnings from the project's own tooling.
- No new high-severity quality issues introduced by the change.
- No duplicated business logic added by the change.
- No violations of project architecture introduced by the change.
- Refactoring stays inside the task scope; larger debt is reported, not fixed silently.

## Output

1. Tools executed (name, scope, result)
2. Findings (severity, file:line, explanation)
3. Recommended corrections
4. Verification results after fixes
5. Remaining technical debt (explicit, with location)
