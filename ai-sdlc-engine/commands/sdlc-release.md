---
description: Prepare a release: final gates, version, changelog, checklist
argument-hint: "[version or release scope]"
---

Act as TeamLead.

Prepare a release.

Target: $ARGUMENTS

Steps:

1. Run all applicable quality gates: build, full test suite, static analysis,
   security audit. Capture real output — no gate may be assumed passed.
2. Verify: no unresolved critical/major findings; documentation updated;
   migrations have rollback strategies.
3. Determine the version (semver; update `plugin.json`, `marketplace.json`
   and `VERSION` together if this is the Engine itself).
4. Update `CHANGELOG.md` with the documented change set.
5. Produce a release checklist: what passed, what was deferred, rollback plan.
6. Production deployment or publishing requires explicit user approval —
   present the checklist and wait. Never deploy unverified code.

Report:

1. Quality gate results (each gate, actual output summary)
2. Version and change set
3. Release checklist
4. Rollback plan
5. Approval request
