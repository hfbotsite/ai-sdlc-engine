# Release Policy

- Every release has a traceable version (semver) and a documented change set (`CHANGELOG.md`).
- Version is updated consistently in all versioned locations in one change.
- All applicable quality gates must pass with recorded evidence before a release candidate is declared.
- Database migrations must have a tested rollback strategy before inclusion in a release.
- Production deployment requires explicit user approval; present the release checklist and wait.
- Rollback plan is part of every release: what to revert, how, and how to verify recovery.
- Deferred findings and known limitations are documented in the release checklist, not hidden.
- Releases of the Engine itself update `plugin.json`, `marketplace.json` and `VERSION` together, so ZCode detects the update.
