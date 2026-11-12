# Quality Gates

A task cannot be marked complete unless all applicable gates pass.
"Applicable" is determined by the project stack — do not run tooling
from a foreign stack.

| Gate | Check | Evidence required |
|---|---|---|
| Build | Compilation / build succeeds | Real command output |
| Tests | Relevant unit/integration/API/E2E tests pass | Execution output, per-suite results |
| Static analysis | Linter, type checker, project's configured analyzers | Tool output, zero unexplained critical warnings |
| Security | No unresolved critical/high findings from audit or SAST/SCA | Findings list or clean scan |
| Code quality | Review findings resolved or explicitly documented | Review verdict |
| Documentation | Affected docs updated | Diff of docs |
| Release | Version + changelog + rollback plan present | Checklist |

Rules:

- Evidence is mandatory: "passed" without execution output is a failure of process.
- A failed gate blocks completion; a skipped gate must be reported as skipped with a reason.
- Hooks only nudge; CI is the enforcement layer. Configure CI per project in `/sdlc-start`.
- Pre-commit speeds local iteration, CI gates each PR, staging verifies the assembled build — none replaces the others.
