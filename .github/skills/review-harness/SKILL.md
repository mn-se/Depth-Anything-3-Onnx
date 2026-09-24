---

name: review-harness
description: Review a development session for evidence-based improvements to AGENTS.md, instructions, and skills. Use when evaluating whether the AI harness should be changed based on observed development behavior, user feedback, or repeated issues.
---

# Harness Review Skill

## Objective

Analyze a development session and identify opportunities to improve the AI development harness.

The harness consists primarily of:

* `AGENTS.md`
* `.github/copilot-instructions.md`
* `.github/instructions/*.instructions.md`
* `.github/skills/*/SKILL.md`

The goal is not to judge the AI response in isolation.

Instead, examine the interaction between:

* User requirements
* AI reasoning and actions
* Project rules
* Instructions
* Skills
* Implementation results
* Validation results
* User corrections or follow-up instructions

Use these observations to identify improvements that could make future development sessions more accurate, efficient, consistent, and autonomous.

Do not modify the harness automatically unless explicitly requested.

---

# Review Principles

## Evidence Over Opinion

Base improvement proposals on observable evidence.

Distinguish clearly between:

* Observed behavior
* User feedback or correction
* Existing harness rules
* Inferred cause
* Proposed improvement

Do not propose changes merely because a different wording might be preferable.

A useful improvement should have a concrete reason connected to the observed session.

---

## Improve the Harness, Not the Individual Response

Focus on changes that can prevent or improve similar problems in future sessions.

Examples of useful findings:

* A rule was missing.
* An existing rule was ambiguous.
* Two rules conflict.
* A rule exists but is difficult to discover or apply.
* A Skill should exist for a repeated workflow.
* An existing Skill has insufficient guidance.
* A project-specific instruction belongs in a language/framework instruction file.
* The workflow in `AGENTS.md` does not adequately cover the observed situation.

Do not recommend harness changes merely to accommodate a one-off mistake.

If the existing harness already provides sufficient guidance, identify the issue as an execution issue rather than proposing an unnecessary harness change.

---

## Preserve Simplicity

Do not add rules, Skills, or agents unless they provide meaningful recurring value.

Prefer:

1. Clarifying an existing rule
2. Removing ambiguity or conflict
3. Improving an existing Skill
4. Adding a new instruction
5. Adding a new Skill

Only introduce additional architectural mechanisms when simpler changes are insufficient.

Avoid turning the harness into an unnecessarily large collection of rules.

---

# Review Scope

Review the following available evidence, in order of relevance:

* Current conversation
* Executed commands and their results
* Files changed during the session
* User corrections, feedback, or follow-up instructions
* Build and test results
* Relevant project and harness configuration

Focus on evidence that is directly relevant to the observed development behavior.

Do not assume that unavailable information exists.

---

## Unavailable Context

If relevant session history or development context is unavailable:

* State the limitation explicitly.
* Do not infer missing evidence.
* Do not treat assumptions as observations.
* Limit improvement proposals to evidence that is actually available.

If the available evidence is insufficient to determine whether the harness contributed to an issue, report the uncertainty and recommend no harness change unless further evidence is available.

---

# Review Workflow

## 1. Understand the Session

Review the available conversation and development context.

Identify:

* User's original objective
* Important constraints
* Decisions made during the session
* AI actions and responses
* Files changed
* Tests and validation performed
* User corrections
* Repeated clarification or rework
* Points where the workflow deviated from expectations

Do not infer information that is not available.

---

## 2. Identify Friction and Failure Patterns

Look for evidence such as:

### Requirement Understanding

* Misunderstood requirements
* Repeated clarification
* Important constraints being forgotten
* Unnecessary assumptions
* Failure to distinguish requirements from hypotheses

### Workflow

* Implementation started before sufficient research
* Plan was skipped for a non-trivial change
* User approval was requested unnecessarily
* AI stopped repeatedly for implementation details after approval
* Significant design changes were made without returning to the planning stage

### Code Changes

* Unrelated files modified
* Existing functionality unnecessarily rewritten
* Existing utilities or abstractions ignored
* Unnecessary dependencies introduced
* Excessive refactoring

### Validation

* Tests omitted
* Incorrect test framework used
* Build or tests not run
* Validation performed too late
* Verification claims not supported by actual execution

### Skill Usage

* An existing Skill should have been used but was not
* A Skill was triggered inappropriately
* A repeated workflow lacks a Skill
* A Skill contains insufficient or conflicting guidance

### Instructions

* A language/framework rule was missing
* An instruction was too vague
* Instructions conflict
* The rule exists in the wrong layer

---

## 3. Determine the Root Cause

For each significant issue, determine why it occurred.

Consider:

* Missing rule
* Ambiguous rule
* Conflicting rules
* Incorrect rule placement
* Missing Skill
* Incomplete Skill
* Poor workflow definition
* Project-specific information missing
* AI execution error that does not justify a harness change

Do not automatically attribute every mistake to the harness.

If the existing harness already provides sufficient guidance, report the issue as an execution issue and recommend no harness change.

If there is insufficient evidence to determine whether the harness contributed to the issue, report the uncertainty and do not recommend a harness change unless further evidence is available.

---

## 4. Evaluate Whether a Harness Change Is Justified

For each candidate improvement, consider:

### Recurrence

Could this issue reasonably occur again?

### Generality

Would the improvement help multiple projects or development sessions?

### Simplicity

Can the issue be addressed by a small change to an existing rule?

### Layer

Which harness layer is the appropriate place?

Use this general preference:

```text
AGENTS.md
    ↓
Project-wide instructions
    ↓
Language/framework instructions
    ↓
Specialized Skill
```

Do not place specialized workflow rules in `AGENTS.md` when they belong in a Skill.

Do not place project-specific behavior in the reusable harness unless it is broadly applicable.

If the existing harness already addresses the observed issue, report it as an execution issue and recommend no harness change.

Do not propose a harness change merely because the AI made a mistake.

---

## 5. Propose Improvements

For each justified improvement, provide:

* **Issue**
* **Evidence**
* **Likely Cause**
* **Affected Harness Component**
* **Proposed Change**
* **Expected Benefit**
* **Confidence**

Example:

```text
Issue:
The agent repeatedly asked for confirmation of implementation details
after the overall plan had already been approved.

Evidence:
The user explicitly stated that implementation details should be handled
autonomously within the approved scope.

Likely Cause:
The implementation autonomy rule in AGENTS.md is not sufficiently explicit.

Affected Harness Component:
AGENTS.md

Proposed Change:
Clarify that implementation details within the approved scope do not
require additional user confirmation.

Expected Benefit:
Reduce unnecessary interruptions during implementation.

Confidence:
High
```

---

# Improvement Categories

Classify proposals when useful.

## Rule Clarification

An existing rule should be made more explicit.

## Rule Addition

A recurring behavior is insufficiently constrained.

## Rule Removal

A rule is unnecessary, redundant, or causes undesirable behavior.

## Rule Conflict

Two rules produce conflicting guidance.

## Skill Improvement

An existing Skill needs additional workflow or decision guidance.

## New Skill

A recurring specialized workflow does not have an appropriate Skill.

## Harness Architecture

The current structure or mechanism is insufficient.

Only recommend architectural changes when changes to existing rules or Skills are not sufficient.

Do not introduce Agents or Hooks unless simpler harness mechanisms are insufficient.

---

# Avoid Overfitting

Do not modify the harness because of:

* A single unusual mistake
* A one-off user preference
* An isolated implementation failure
* A project-specific requirement that does not generalize
* A problem better solved by normal project documentation

Look for repeated or structurally significant patterns.

When evidence is weak, label the proposal as low confidence or do not recommend a change.

---

# Prioritization

Prioritize improvement proposals using:

* **High** — A recurring or significant issue that the harness can reasonably prevent.
* **Medium** — A useful improvement with moderate recurrence or impact.
* **Low** — A minor optimization or usability improvement.

Priorities describe improvement urgency, not overall harness quality.

Do not assign an overall score, rating, or ranking to the harness.

---

# Harness Change Proposal

When a concrete change is justified, provide the smallest practical modification.

Prefer showing:

* File to modify
* Relevant section
* Proposed wording or structural change
* Reason for the change

Do not rewrite an entire file when a small change is sufficient.

If multiple files are affected, explain the dependency between the changes.

Do not modify files unless explicitly requested.

---

# Validation of Proposed Improvements

Before recommending a change:

* Check the current harness content.
* Confirm that the proposed rule does not already exist.
* Check for conflicting instructions.
* Check whether the proposed location is appropriate.
* Consider whether the change could create unintended behavior.

Do not claim that a proposed improvement has been validated through future sessions.

---

# Output

For a normal review, use the following structure:

## Session Summary

Briefly summarize the relevant development session.

## Observed Issues

List only issues supported by evidence.

## Harness Improvement Opportunities

For each justified opportunity:

* Priority
* Issue
* Evidence
* Likely Cause
* Affected Component
* Proposed Change
* Expected Benefit
* Confidence

## No Change Recommended

If an observed issue does not justify a harness change, explain briefly why.

If no harness improvements are justified, state that explicitly.

## Proposed Changes

Provide the concrete file-level changes that should be considered.

Do not modify files unless explicitly requested.

---

# Change Discipline

* Do not modify the harness automatically.
* Do not modify project source code as part of this Skill.
* Do not invent evidence from unavailable conversation history.
* Do not treat hypotheses as verified causes.
* Do not add rules merely to explain a single failure.
* Do not duplicate existing rules unnecessarily.
* Do not create a new Skill when an existing Skill can be improved.
* Do not introduce Agents or Hooks unless simpler harness mechanisms are insufficient.
* Preserve the existing harness architecture unless there is evidence that it is inadequate.
* Preserve unrelated user changes in the working tree.
