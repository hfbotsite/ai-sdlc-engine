# Git Policy

- Work on dedicated feature branches: `feature/<task-id>-<slug>` or the project's convention.
- Link every commit to a task ID in the message.
- Never commit secrets, credentials, tokens, or private data.
- Never rewrite shared history (force-push to shared branches) without explicit user approval.
- Do not merge unverified changes: merge requires passing quality gates and review verdict.
- Keep commits small and single-purpose; no unrelated changes in one commit.
- The main branch must always be releasable; broken builds are fixed or reverted immediately.
