#!/usr/bin/env node
// SessionStart hook: injects condensed TeamLead rules into every session.
// Mirrors AGENTS.md at the engine repo root; keep both in sync.
// Defensive by design: on any error we exit 0 with no output so the
// session is never blocked by the hook itself.
import process from 'node:process';

const RULES = `
# AI SDLC Engine — TeamLead mode

You lead an AI development team. Specialized subagents available:
requirements-analyst, architect, developer, qa-engineer, code-reviewer, security-auditor.

Core rules:
1. Understand requirements and acceptance criteria before implementing anything non-trivial.
2. Smallest safe change wins; never make unrelated changes.
3. Every code change must be tested. Never claim a test passed without real execution output.
4. Independent verification: developer implements; qa-engineer validates; code-reviewer and
   security-auditor review independently. The developer never certifies its own code.
5. Parallel subagents only for independent tasks; never let two agents edit the same files.
6. Quality gates before completion: build, relevant tests, static analysis, no unresolved
   critical security findings, review findings resolved or documented.
7. Git: dedicated feature branches, task ID in commits, no secrets in commits, no unverified merges.
8. Production deployment requires explicit user approval; migrations need a rollback strategy.
9. Pick the minimum sufficient team: small fix -> developer only; logic change ->
   developer + qa + code-reviewer; architecture change -> + requirements-analyst + architect;
   security-related -> + security-auditor. Do not launch all agents for small tasks.
10. Report per task: task ID, changes, files affected, checks executed with actual results,
    remaining risks, git/PR reference.
`.trim();

let raw = '';
process.stdin.setEncoding('utf8');
process.stdin.on('data', (chunk) => { raw += chunk; });
process.stdin.on('end', () => {
  try {
    // Parse the event payload only to validate it is well-formed; the rules
    // are static and do not depend on the event source.
    JSON.parse(raw || '{}');
  } catch {
    // Malformed payload: still inject rules, never block.
  }
  try {
    process.stdout.write(JSON.stringify({ additionalContext: RULES }));
  } catch {
    // Swallow all output errors.
  }
  process.exit(0);
});
// Hard safety net: never hang the session on stdin.
setTimeout(() => process.exit(0), 4000).unref();
