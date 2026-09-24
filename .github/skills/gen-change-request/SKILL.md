---
name: gen-change-request
description: Create, inspect, validate, and manage GitHub Change Requests associated with Issue-based development.
---

# GitHub Change Request Management

Use this skill after implementation and validation are complete.

## 1. Pre-Change Request Checks

Before creating a Pull Request:

1. Confirm the current branch is the Issue branch.
2. Confirm the branch is associated with the intended Issue.
3. Check Git status.
4. Review the complete diff.
5. Run relevant tests and validation.
6. Confirm the Issue acceptance criteria are satisfied.
7. Confirm there are no unrelated changes.

Do not create a Pull Request when validation has not been performed unless
the user explicitly requests an exception.

## 2. Commit

Create focused commits containing only changes related to the Issue.

Do not include unrelated user changes.

## 3. Push

Push the Issue branch to the remote repository.

Do not force-push unless explicitly requested.

## 4. Create Change Request

Create a Change Request associated with the Issue.

The Pull Request should include:

- Summary
- Implementation details
- Validation performed
- Known limitations
- Deviations from the original plan

Reference the Issue using GitHub-supported syntax.

Example:

    Closes #123

## 5. Review Change Request

Before considering the Change Request ready:

- inspect the final diff;
- inspect changed files;
- verify tests;
- verify acceptance criteria;
- check for unrelated changes.

## 6. Merge Change Request

Do not merge the Change Request unless explicitly requested by the user.

If the user requests a merge of the Change Request:

1. Check the PR status.
2. Check required CI checks.
3. Check unresolved review comments.
4. Report any blocking conditions.
5. Merge only after confirming the requested Change Request is the intended target.

Never merge a different Change Request based only on similarity.