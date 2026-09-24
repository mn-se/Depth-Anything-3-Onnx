---
name: gen-issue
description: Create, inspect, update, and manage GitHub Issues for development work. Use when a development task needs an Issue, when checking whether an existing Issue already covers a request, or when requirements change during implementation.
---

# GitHub Issue Management

Use this skill whenever development work needs to be associated with a
GitHub Issue.

## 1. Search Existing Issues

Before creating an Issue:

1. Inspect the repository.
2. Search existing open Issues.
3. Look for Issues describing the same or substantially similar work.
4. Prefer reusing an existing Issue when appropriate.
5. Avoid creating duplicate Issues.

When an existing Issue is used, read the complete Issue before proceeding.

## 2. Create an Issue

If no suitable Issue exists, create one.

The Issue should contain:

### Problem

Describe the problem or motivation.

### Goal

Describe the desired outcome.

### Scope

Describe what is included and excluded.

### Acceptance Criteria

Define concrete conditions that determine completion.

### Technical Constraints

Record known technical constraints, compatibility requirements,
performance requirements, or implementation restrictions.

Do not invent requirements.

If important information is missing and materially affects the implementation,
ask the user instead.

## 3. Issue Quality

The Issue should be understandable without the original conversation.

Avoid:

- vague requirements;
- implementation details that have not been established;
- speculative requirements;
- unrelated cleanup;
- unnecessary scope.

## 4. Updating an Issue

If implementation reveals that the requirements or scope have materially
changed:

1. Stop implementation if necessary.
2. Explain the change.
3. Update the Issue.
4. Update the implementation plan.
5. Obtain user approval when the change is significant.

Keep the Issue synchronized with the actual development scope.

## 5. Completion

When development is complete:

- Ensure the Pull Request references the Issue.
- Use GitHub-supported closing syntax when appropriate.
- Do not manually close the Issue if the Pull Request workflow will
  automatically close it.