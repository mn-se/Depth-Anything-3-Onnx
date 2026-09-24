# AGENTS.md

## Development Workflow

For non-trivial development tasks, follow this workflow:

Issue → Worktree → Research → Plan → Implement → Validate → Pull Request → Merge

The Issue is the source of truth for the development task.

The Pull Request must not be merged unless explicitly requested by the user.

### Task Classification

First determine whether the request is:

- Question or investigation
- Documentation-only change
- Bug fix
- Feature development
- Refactoring
- Test development

Questions and investigations do not require the Issue/Worktree workflow unless
they result in implementation work.

For non-trivial development tasks, the Issue/Worktree workflow is mandatory.

---

## Issue

Before making implementation changes:

1. Search existing GitHub Issues for a relevant Issue.
2. Reuse an existing Issue when it accurately represents the requested work.
3. If no suitable Issue exists, create a new GitHub Issue.
4. Ensure the Issue describes:
   - Problem
   - Goal
   - Scope
   - Acceptance criteria
   - Relevant technical constraints

Do not begin implementation before a suitable Issue exists.

Treat the Issue as the source of truth.

If the user's request materially changes during development, update the Issue
before continuing.

---

## Worktree

Implementation must be performed in a dedicated Git worktree.

Use an Issue-specific branch:

    issue/<issue-number>-<short-description>

Example:

    issue/123-tof-amplitude-filter

Do not implement Issue-based work directly on the default branch.

Before creating a worktree:

- Check the current Git status.
- Preserve unrelated working-tree changes.
- Check existing worktrees.
- Avoid overwriting or deleting existing work.

The worktree is the working environment for the entire Issue.

Research, implementation, testing, and commits for the Issue should be
performed in the Issue worktree.

---

## Research

Before making implementation changes:

- Inspect the relevant code, architecture, interfaces, dependencies, and tests.
- Identify constraints, assumptions, and unknowns.
- Understand the existing behavior and likely impact of the change.
- Inspect the Issue and verify that the requested behavior is understood.

Do not modify implementation code during research.

---

## Plan

Before implementation:

- Define the proposed approach.
- Identify the affected files and components.
- Explain important design decisions and trade-offs.
- Define how the change will be validated.
- Confirm that the proposed implementation satisfies the Issue acceptance criteria.

For non-trivial changes, the plan should be reviewed by the user before
implementation begins.

After the plan is approved, implementation may proceed autonomously within
the approved scope.

---

## Implement

After the plan is approved:

- Implement the agreed approach.
- Work autonomously within the approved scope.
- Reuse existing functionality where appropriate.
- Avoid unrelated changes.
- Keep implementation changes traceable to the Issue.

Do not stop for user confirmation for every implementation detail.

If implementation reveals a significant issue that changes the design or scope:

1. Stop implementation.
2. Explain the issue.
3. Update the Issue and plan as necessary.
4. Obtain user approval when the change is materially different.
5. Continue implementation only after the updated plan is approved.

---

## Validate

After implementation:

- Build the affected components.
- Run relevant tests or validation procedures.
- Review the resulting diff.
- Check for unintended changes.
- Verify the Issue acceptance criteria one by one.

Never claim that something was built, tested, or verified unless it was actually
done.

If validation cannot be performed, explicitly state why.

---

## Commit

After validation:

- Create focused commits for the Issue.
- Do not include unrelated changes.
- Preserve unrelated working-tree changes.
- Do not reset, rebase, or discard user changes without explicit approval.

Commit messages should clearly describe the change.

---

## Pull Request

After implementation and validation:

1. Push the Issue branch.
2. Create a Pull Request associated with the Issue.
3. Reference the Issue from the Pull Request.
4. Include:
   - Summary of the implementation
   - Validation performed
   - Known limitations
   - Any deviations from the original plan

Before creating the Pull Request:

- Review the complete diff.
- Confirm that the acceptance criteria are satisfied.
- Confirm that no unrelated changes are included.

Do not merge the Pull Request unless explicitly requested by the user.

---

## General Principles

- Understand before modifying.
- Prefer the smallest change that solves the problem.
- Preserve existing behavior unless a change is required.
- Avoid unnecessary dependencies and architectural changes.
- Do not modify unrelated files.
- Reuse existing functionality instead of duplicating it.
- Distinguish facts, assumptions, and hypotheses.
- Do not invent specifications, APIs, behavior, or test results.
- When requirements are ambiguous and the ambiguity materially affects the
  implementation, ask the user rather than making a significant assumption.
- Preserve unrelated user changes.

