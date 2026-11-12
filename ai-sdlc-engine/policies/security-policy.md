# Security Policy

- Treat credentials, tokens, private keys, personal data and production data as sensitive; never print or commit them.
- Secrets belong in environment/credential mechanisms, never in code, configs, logs or documentation.
- Every change touching auth, input handling, dependencies, or configuration requires a security audit before merge.
- Findings are classified: critical/high block merge; medium/low are documented with an owner.
- Dependency updates with known critical CVEs are treated as blockers.
- Security verification (SAST, SCA, secrets scanning) runs in CI on every PR; local audits complement, never replace it.
- Read-only auditors (code-reviewer, security-auditor) never fix code directly; findings route through the TeamLead to the developer.
