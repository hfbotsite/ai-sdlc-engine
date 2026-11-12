---
name: security-engineering
description: Use when auditing or verifying security: SAST, dependency scanning, secrets detection, configuration audit, injection and authz checks, with severity classification and remediation advice.
---

# SECURITY ENGINEERING

## Objective

Find real security issues and report them with severity and concrete
remediation — distinguishing confirmed vulnerabilities from theoretical risks.

## Audit classes

Work through each class relevant to the scope:

1. **SAST** (code-level): injection (SQL, command, path traversal), unsafe
   deserialization, XSS, weak crypto, auth flaws, broken access control.
2. **SCA** (dependencies): known vulnerable versions (use the project's
   audit tooling: `npm audit` / `pip-audit` / `cargo audit` / similar),
   suspicious or unmaintained packages.
3. **Secrets**: credentials, keys and tokens in code, logs, configs, history.
4. **Configuration**: debug mode, permissive CORS, insecure TLS defaults,
   exposed admin endpoints, permissive file permissions.
5. **Data exposure**: sensitive data in logs, errors, responses, caches.

## Workflow

1. Determine the stack and pick its native tooling; do not run tooling
   from a foreign stack.
2. Run automated scans first (if configured in the project), then manual
   review of the diff and its trust boundaries.
3. Trace external input to its use; check validation and encoding at each step.
4. For every finding: cite file:line, describe the attack scenario,
   classify severity (critical / high / medium / low), propose remediation.
5. Run available scanners via CI configuration when present rather than
   inventing one-off commands.

## Quality criteria

- Every confirmed finding has a concrete attack scenario, not just a rule name.
- Clean classes are explicitly reported as checked and clean.
- No severity inflation; theoretical concerns are marked as such.

## Output

1. Verdict: security blockers / no blockers
2. Findings (severity, file:line, scenario, remediation)
3. Scans executed (tool, scope, result)
4. Classes checked and clean
5. Residual risks
