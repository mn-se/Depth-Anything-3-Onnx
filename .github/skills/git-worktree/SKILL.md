---
name: git-worktree
description: Create and manage isolated Git worktrees for Issue-based development. Use when beginning implementation work associated with a GitHub Issue.
---

# Git Worktree Management

Use this skill when implementation work must be isolated from the default
branch.

## 1. Inspect Current State

Before creating a worktree:

1. Check the current Git branch.
2. Check `git status`.
3. Check existing worktrees.
4. Identify uncommitted changes.
5. Preserve all unrelated user changes.

Never discard or overwrite existing work.

## 2. Branch Naming

Use a task-category prefix and the Issue number:

    <category>/<issue-number>-<short-description>

Use `feature` for feature development, `bugfix` for bug fixes, `refactor` for
refactoring, `docs` for documentation-only changes, and `test` for test
development.

Examples:

    feature/123-add-amplitude-filter
    bugfix/124-fix-amplitude-filter
    refactor/125-simplify-filter

Use lowercase kebab-case for the short description.

## 3. Create the Worktree

Create a dedicated worktree for the Issue branch.

The default branch must remain untouched.

The worktree should be separate from the user's existing working directory.

Before creation, verify that:

- the branch name does not conflict with an existing branch;
- the worktree path does not already exist;
- an existing worktree is not already associated with the Issue.

## 4. Existing Worktrees

If a worktree already exists for the Issue:

- inspect its status;
- reuse it when appropriate;
- do not create a duplicate worktree.

Never delete an existing worktree without explicit approval.

## 5. Development

Once created, all implementation, testing, and commits for the Issue should
take place inside the Issue worktree.

Do not switch the user's existing working directory to another branch merely
to perform the Issue work.

## 6. Cleanup

After the Pull Request has been merged, the worktree may be removed only
when:

- there are no uncommitted changes;
- the user has not indicated that the worktree should be retained;
- removing it will not destroy useful local work.

Never remove a worktree containing uncommitted changes.