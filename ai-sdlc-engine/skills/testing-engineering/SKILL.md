---
name: testing-engineering
description: Use when designing, writing or running tests: test matrix, unit, integration, API, E2E, regression coverage, boundary and negative scenarios, coverage reporting.
---

# TESTING ENGINEERING

## Objective

Validate behavior with evidence: every claim of correctness must come
from an actually executed check.

## Workflow

1. Identify the project's existing test framework and conventions; use them.
2. Analyze existing coverage for the affected area before writing new tests.
3. Build a test matrix before writing code:
   - positive scenarios (expected usage)
   - negative scenarios (invalid input, error paths)
   - boundary values, empty/null states
   - failure and recovery scenarios
4. Choose the right test level per scenario: unit < integration < API < E2E.
   Do not write an E2E test for something a unit test proves.
5. Write tests with meaningful assertions; never weaken an assertion
   to make a test pass.
6. Run the affected tests first, then the relevant suite; capture real output.
7. Run regression checks on functionality adjacent to the change.
8. Report coverage and remaining untested risks honestly.

## Quality criteria

- Every acceptance criterion is mapped to at least one test.
- Real execution output exists for every reported result.
- No skipped/disabled tests introduced by the change.
- Flaky tests are reported, not ignored.

## Output

1. Test matrix (scenario → level → status)
2. Tests executed with actual results
3. Defects found (severity, reproduction)
4. Coverage summary
5. Untested risks and recommended follow-ups
