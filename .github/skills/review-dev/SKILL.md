---
name: review-dev
description: Review completed Issue-based development work against its requirements, acceptance criteria, implementation plan, tests, and final Git diff. Use before creating or finalizing a Pull Request.
---

# Development Review

Use this skill before creating a Pull Request or declaring an Issue complete.

## 1. Issue Review

Read the Issue and identify:

- Problem
- Goal
- Scope
- Acceptance Criteria
- Technical Constraints

## 2. Implementation Review

Review the implementation against the Issue.

Check:

- Is the requested behavior implemented?
- Are acceptance criteria satisfied?
- Are unrelated changes present?
- Was existing functionality reused where appropriate?
- Were unnecessary dependencies introduced?
- Were existing behaviors preserved?

## 3. Plan Review

Compare the implementation with the approved plan.

Identify:

- deviations;
- additional changes;
- removed planned changes;
- changes caused by implementation discoveries.

Significant deviations must be explained.

## 4. Validation Review

Confirm that validation was actually performed.

Record:

- build result;
- test result;
- static analysis result when applicable;
- manual validation when applicable.

Never infer successful validation from code inspection alone.

## 5. Diff Review

Inspect the complete Git diff.

Look for:

- unintended files;
- debug code;
- temporary files;
- generated artifacts;
- accidental formatting changes;
- secrets or credentials;
- unrelated refactoring.

## 6. Final Assessment

Produce a concise report:

- Issue
- Scope implemented
- Acceptance criteria status
- Tests performed
- Build result
- Known limitations
- Remaining concerns
- PR readiness