#!/usr/bin/env node
// PostToolUseFailure hook: surfaces a short diagnostic hint after a tool fails.
// The error text itself is already visible to the model; this hook adds a
// process hint (diagnose before retry). Defensive: always exits 0.
import process from 'node:process';

let raw = '';
process.stdin.setEncoding('utf8');
process.stdin.on('data', (chunk) => { raw += chunk; });
process.stdin.on('end', () => {
  try {
    const event = JSON.parse(raw || '{}');
    const tool = event.tool_name || event.toolName || event.tool || 'the tool';
    const context = { additionalContext: `${tool} failed. Diagnose the cause before retrying; do not retry the identical call unchanged. If the failure repeats, change the approach or report the blocker.` };
    process.stdout.write(JSON.stringify(context));
  } catch {
    // Never block the session on hook errors.
  }
  process.exit(0);
});
setTimeout(() => process.exit(0), 4000).unref();
