---
description: Full independent review of current changes (quality + security)
argument-hint: "[scope: diff, branch, task id]"
skills: code-quality-engineering
---

Act as TeamLead.

Run a full independent review of the current changes.

Scope: $ARGUMENTS (default: current diff / branch against main)

Steps:

1. Run the applicable automated checks yourself: build, tests, lint,
   static analysis (per the project's stack). Capture real output.
2. Delegate code review to the code-reviewer agent (independent, read-only).
3. Delegate security audit to the security-auditor agent if the change
   touches auth, input handling, dependencies, configs, or was not audited before.
4. Triage all findings: critical/major must be fixed before merge;
   minor/nit are documented.
5. Route blocking findings back to the developer; re-run the failed checks
   after fixes.

Use the code-quality-engineering skill for the quality checklist.

Report:

1. Automated checks executed and results
2. Review findings (severity, file:line, explanation)
3. Security findings
4. Verdict: ready to merge / changes required
5. Remaining risks
