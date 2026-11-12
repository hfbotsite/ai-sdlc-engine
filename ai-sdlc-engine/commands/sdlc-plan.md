---
description: Design architecture and decompose an analyzed task into a plan
argument-hint: "[constraints or preferences]"
---

Act as TeamLead.

Build the implementation plan for the current analyzed task.

Constraints: $ARGUMENTS

Steps:

1. If architectural decisions are involved, delegate design to the
   architect agent (contracts, data model, trade-offs, impact on existing modules).
2. Decompose the task into independent subtasks with IDs.
3. For each subtask define: objective, scope, files/modules, constraints,
   acceptance criteria, required tests.
4. Mark which subtasks can run in parallel (no shared files) and which are sequential.
5. Assign the minimal agent team per subtask.

Output the plan as a numbered list of subtasks with the fields above,
plus: total estimated scope, risks, and points requiring user decisions.

Do not start implementation. Wait for plan approval.
