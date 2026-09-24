---

name: gen-readme
description: Create and maintain a standardized project README.md with a consistent structure, content scope, and documentation style based on the actual project implementation.
---

# Project README Skill

## Objective

Create and maintain the project's root `README.md`.

The README is the primary entry point for understanding and using the project.

Keep the README:

* Consistent across projects
* Concise and practical
* Based on the actual implementation
* Easy for a new developer to understand
* Focused on how to build, run, test, and use the project

Do not invent project behavior, commands, dependencies, requirements, or specifications.

---

# Workflow

## 1. Inspect the Project

Before creating or updating `README.md`:

* Inspect the project structure.
* Identify the project purpose and main functionality.
* Identify supported platforms and environments.
* Identify the primary languages and frameworks.
* Identify build and dependency management.
* Identify how the project is configured.
* Identify how the project is built.
* Identify how the project is executed.
* Identify how tests are run.
* Identify important external dependencies.
* Check existing documentation.
* Check existing `README.md` if present.
* Check project configuration and build files when necessary.

Use the implementation and project configuration as the source of truth.

Do not infer commands or behavior from filenames alone.

---

# README Structure

Use the following chapter structure for the root `README.md`.

Keep the chapter order unchanged unless there is a strong project-specific reason.

Omit a chapter only when it is genuinely not applicable.

## 1. Overview

Briefly explain:

* What the project is
* What problem it solves
* Main functionality
* Intended use

Keep this section concise.

Do not write marketing-style claims.

---

## 2. Features

List the major implemented capabilities.

Focus on user-visible or developer-relevant functionality.

Do not list trivial implementation details.

Do not describe planned or hypothetical features as implemented features.

---

## 3. Requirements

Document the environment required to use or develop the project.

Include when applicable:

* Operating system
* CPU architecture
* Compiler
* Language/runtime version
* Build system
* Required SDKs
* Required hardware
* External services
* Required tools

Only document requirements that are supported by the project.

---

## 4. Project Structure

Show the important project directories and files.

Focus on directories and files that help a developer navigate the project.

Example:

```text
project/
├── src/
├── include/
├── tests/
├── docs/
└── CMakeLists.txt
```

Add a short explanation of important directories when useful.

Do not document every file.

---

## 5. Setup

Explain how to prepare the development or runtime environment.

Include:

* Repository setup
* Dependency installation
* Environment configuration
* Required initialization steps
* Hardware setup when applicable

Use actual project commands.

Do not invent commands.

---

## 6. Build

Document how to build the project.

Include:

* Configure command
* Build command
* Important build options
* Build output location when useful

Prefer the project's established build workflow.

Examples should be executable as written.

---

## 7. Usage

Explain the normal way to use or execute the project.

Include:

* Main commands
* Important arguments
* Configuration
* Input/output
* Typical usage examples

Keep examples minimal and representative.

Do not document internal APIs here unless they are part of normal project usage.

---

## 8. Testing

Explain how to run the project's tests.

Include:

* Test command
* Test framework when relevant
* Important test options
* Integration or hardware-dependent tests when relevant

Distinguish unit tests from integration or hardware-dependent validation when necessary.

Do not claim tests exist or pass unless verified from the project.

---

## 9. Configuration

Document important configuration that users or developers may need to change.

Include:

* Configuration files
* Environment variables
* Build options
* Runtime parameters
* Hardware-specific settings

Document purpose and meaningful values rather than every available constant.

Never include secrets or credentials.

---

## 10. Development

Document information useful to developers working on the project.

Include when applicable:

* Development workflow
* Code organization
* Formatting/linting
* Static analysis
* Development commands
* Debugging entry points
* Contribution expectations

Avoid duplicating detailed language-specific coding rules already documented elsewhere.

---

## 11. Dependencies

Document important direct dependencies and external components.

For each important dependency, explain its role when useful.

Do not list transitive dependencies unless they are relevant to project operation.

Do not add a dependency to the README merely because it appears in a lockfile or generated file.

---

## 12. Hardware

Include this chapter when the project depends on specific hardware.

Document:

* Required hardware
* Supported devices
* Connections
* Important hardware configuration
* Hardware-specific limitations

Use diagrams or tables when they significantly improve understanding.

---

## 13. Limitations

Document known and relevant limitations.

Examples:

* Unsupported platforms
* Unsupported input formats
* Hardware limitations
* Performance limitations
* Known configuration restrictions
* Known issues affecting normal use

Do not speculate about limitations that have not been established.

---

## 14. License

Document the project's license when it can be established from the repository.

If the project contains a license file, reference the actual license.

Do not infer licensing terms from dependencies or repository hosting.

---

# Content Rules

## Source of Truth

Use the following sources in approximately this priority:

1. Existing implementation
2. Build and project configuration
3. Tests
4. Existing project documentation
5. Explicit project metadata

When sources disagree:

* Prefer the current implementation and configuration.
* Identify the inconsistency.
* Update the README to reflect verified behavior.
* Do not silently invent a resolution.

---

## Commands

Every command documented in the README must be verified against the project whenever practical.

Do not invent:

* Build commands
* Test commands
* Installation commands
* Runtime commands
* Configuration commands
* Environment variables

If a command cannot be verified, do not present it as a confirmed command.

---

## Examples

Examples should:

* Be minimal
* Be realistic
* Reflect actual project behavior
* Use valid paths and commands
* Avoid unnecessary complexity

Do not create fictional output.

When exact output is important, verify it before documenting it.

---

## Tables

Use tables when they improve readability.

Good candidates include:

* Supported platforms
* Hardware requirements
* Important configuration parameters
* Build options
* Dependencies

Do not use tables merely for formatting.

---

# Updating an Existing README

When `README.md` already exists:

1. Read the existing README completely.
2. Compare it with the standard chapter structure.
3. Identify outdated, missing, duplicated, or incorrect information.
4. Verify relevant information against the current project.
5. Update the content.
6. Preserve useful project-specific information.
7. Reorganize sections to match the standard structure.
8. Remove obsolete information.
9. Review commands and examples.
10. Review the final diff.

Do not rewrite the README unnecessarily when only a small update is required.

However, maintain the standard chapter order and structure when updating the document.

---

# Creating a New README

When `README.md` does not exist:

1. Inspect the project sufficiently to understand its purpose and operation.
2. Determine which standard chapters apply.
3. Create the README using the standard chapter order.
4. Populate only information supported by the project.
5. Verify commands and examples.
6. Review the final document for consistency.

Do not fill missing information with guesses.

---

# Mermaid Diagrams

Use Mermaid diagrams only when they materially improve understanding.

Appropriate uses include:

* High-level architecture
* Processing flow
* Component relationships
* Hardware connections
* Important workflows

Prefer simple diagrams.

Do not duplicate detailed diagrams from `code-documentation` unless they are useful to README readers.

Use actual project components and relationships.

Do not invent relationships.

---

# README Style

* Write in clear technical English unless the project explicitly uses another language.
* Prefer concise sentences.
* Prefer concrete descriptions over abstract explanations.
* Use headings consistently.
* Use code blocks for commands and configuration.
* Use bullet lists for concise collections.
* Avoid marketing language.
* Avoid unnecessary background information.
* Avoid repeating the same information in multiple sections.
* Keep the README focused on practical project understanding and usage.

---

# Validation

Before completing the task:

* Confirm the README reflects the current project.
* Check that documented paths exist.
* Check that documented commands match project configuration.
* Check that referenced files exist.
* Check that dependency names are correct.
* Check that platform and version information is accurate.
* Check that examples are consistent with the implementation.
* Check Mermaid syntax when diagrams are added.
* Review the final diff.

Do not claim that commands were executed unless they were actually executed.

---

# Change Discipline

* Modify only the README unless related documentation changes are explicitly required.
* Do not modify source code to make documentation easier to write.
* Do not perform unrelated documentation cleanup.
* Do not remove useful project-specific information merely to match the template.
* Do not document unimplemented features.
* Do not invent missing information.
* Preserve accurate information even when it does not fit neatly into the standard structure.
* Keep the README proportional to the project's complexity.
---