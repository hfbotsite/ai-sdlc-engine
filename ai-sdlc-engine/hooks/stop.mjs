#!/usr/bin/env node
// Stop hook: soft reminder when a response looks final but contains no
// validation evidence. This is a heuristic nudge, not a gate; real quality
// enforcement belongs in CI. Defensive: always exits 0, never forces
// continuation (avoids reply loops).
import process from 'node:process';

const FINAL_RE = /(task completed|implementation complete|задача выполнена|завершено|done\.?$|all set|ready for)/i;
const EVIDENCE_RE = /(tests? (?:pass|passed|run|executed)|build (?:succeed|passed)|lint|typecheck|static analysis|coverage|test results|execution output|команда выполнена|тесты (?:пройдены|запущены|выполнены)|сборка прошла)/i;

let raw = '';
process.stdin.setEncoding('utf8');
process.stdin.on('data', (chunk) => { raw += chunk; });
process.stdin.on('end', () => {
  try {
    if (FINAL_RE.test(raw) && !EVIDENCE_RE.test(raw)) {
      const context = {
        additionalContext: 'Reminder: this response reports completion but contains no validation evidence. Include what was actually executed (tests, build, lint/static analysis) with real results, or state explicitly that checks were not run.',
      };
      process.stdout.write(JSON.stringify(context));
    }
  } catch {
    // Never block the session on hook errors.
  }
  process.exit(0);
});
setTimeout(() => process.exit(0), 4000).unref();
