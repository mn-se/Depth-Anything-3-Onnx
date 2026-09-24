---

name: gen-code-doc
description: Analyze existing code and create maintainable technical documentation with structured explanations and Mermaid diagrams for architecture, data flow, processing flow, and component interactions.
---

# Code Documentation Skill

## Objective

Create technical documentation from the existing implementation.

The documentation should help another developer understand:

* What the code does
* Why it exists
* How the major components are structured
* How data flows through the system
* How processing proceeds
* How components interact
* Important assumptions and constraints
* How the implementation is validated

Documentation must describe behavior that can be established from the implementation and related project information.

Do not invent requirements, specifications, intended behavior, or implementation details.

---

# Workflow

## 1. Understand the Code

Before writing documentation:

* Read the relevant implementation.
* Identify the main entry points.
* Identify public interfaces and important internal components.
* Trace important data and control flow.
* Inspect important callers and callees when necessary.
* Inspect related tests.
* Check existing documentation and comments.
* Identify assumptions, constraints, dependencies, and non-obvious behavior.

Do not document behavior based only on function or variable names.

---

## 2. Determine the Documentation Scope

Determine the appropriate documentation scope before writing.

The scope may be:

* A function
* A class
* A module
* A subsystem
* A complete application or library

Prioritize:

1. Public APIs
2. Main components
3. Architecture
4. Data flow
5. Processing flow
6. Component interactions
7. Non-trivial algorithms
8. Important data structures
9. Configuration and parameters
10. External interfaces
11. Constraints and limitations
12. Testing and validation

Do not document every line or every trivial function.

---

# Documentation Structure

Use the following chapter structure as the standard template.

Not every document must contain every chapter.

Include a chapter when it provides meaningful information for the target scope. Omit chapters that are not applicable.

## 1. Overview

Explain:

* Purpose
* Problem being solved
* Main functionality
* Scope

Keep this section concise.

---

## 2. Architecture

Describe the overall structure of the system.

Include:

* Major components
* Responsibilities
* Relationships between components
* Important dependencies
* System boundaries

Use a Mermaid `flowchart` when the architecture contains multiple interacting components.

Architecture describes **what the system is composed of**.

---

## 3. Data Flow

Describe how important data moves through the system.

Include:

* Data sources
* Major transformations
* Intermediate representations
* Data destinations
* Important data dependencies
* Data ownership where relevant

Use a Mermaid `flowchart` when the data flow is non-trivial.

Data Flow describes **what data moves where**.

---

## 4. Processing Flow

Describe the execution and processing sequence.

Include:

* Main processing stages
* Important branches
* Conditions affecting execution
* Major transformations
* Error or fallback paths when relevant

Use a Mermaid `flowchart` when it improves understanding.

Processing Flow describes **what operations are performed and in what order**.

---

## 5. Sequence

Describe time-ordered interactions between components.

Include:

* Function calls
* Messages
* Events
* Callbacks
* Important responses
* Error paths when relevant

Use a Mermaid `sequenceDiagram` when multiple components interact over time.

Sequence describes **who interacts with whom and when**.

---

## 6. Components

Describe the important classes, modules, or subsystems.

Use a concise table when appropriate:

| Component    | Responsibility |
| ------------ | -------------- |
| `ComponentA` | ...            |
| `ComponentB` | ...            |

Do not create detailed descriptions for trivial implementation details.

---

## 7. Interfaces

Document interfaces exposed to or used by other components.

Include relevant information such as:

* Public APIs
* Inputs
* Outputs
* Parameters
* Return values
* Data formats
* Units
* Coordinate systems
* Preconditions
* Side effects
* Failure conditions

For APIs, document behavior rather than merely reproducing the function signature.

---

## 8. Data Structures

Describe important data structures and their relationships.

Include:

* Important classes
* Structures
* Data ownership
* Important fields
* Units
* Coordinate conventions
* Relationships between data structures

Use a Mermaid `classDiagram` when relationships between multiple classes or structures are important.

Do not create diagrams for simple or obvious structures.

---

## 9. Algorithms

Document non-trivial algorithms and mathematical processing.

For each important algorithm, explain:

* Purpose
* Inputs
* Outputs
* High-level processing
* Important assumptions
* Important parameters
* Mathematical model or equations when necessary
* Limitations

Examples include:

* Coordinate transformation
* Plane estimation
* RANSAC
* Filtering
* Interpolation
* Optimization
* Sensor fusion

Explain the algorithm conceptually rather than reproducing the source code.

Use Mermaid diagrams when they improve understanding.

---

## 10. Configuration

Document meaningful configuration parameters.

Include:

* Parameter name
* Meaning
* Units
* Valid range when known
* Default value when applicable
* Effect on behavior

Do not simply list every constant in the source code.

Only document parameters relevant to understanding or operating the system.

---

## 11. Error Handling

Describe important failure conditions and how they are handled.

Include:

* Input validation
* Error detection
* Error propagation
* Recovery
* Fallback behavior
* Timeout behavior
* Invalid-data handling

Include error paths in Mermaid diagrams when they are important to understanding the behavior.

---

## 12. Dependencies

Describe important dependencies.

Include relevant:

* Libraries
* Frameworks
* SDKs
* Operating-system dependencies
* Hardware dependencies
* Runtime requirements
* External services

Do not list every transitive dependency.

---

## 13. Constraints & Limitations

Document known limitations and constraints.

Examples:

* Supported input ranges
* Accuracy limitations
* Performance constraints
* Memory limitations
* Hardware restrictions
* Platform restrictions
* Unsupported cases
* Known issues

---

## 14. Testing

Describe how the implementation is validated.

Include relevant:

* Unit tests
* Integration tests
* Hardware-dependent tests
* Important test scenarios
* Boundary conditions
* Regression tests
* Known test gaps

Focus on **what behavior is validated and how**, rather than documenting every individual test case.

---

## 15. Future Considerations

Include this chapter only when there are concrete items supported by the project, such as:

* Existing TODOs
* Explicitly identified technical debt
* Known limitations requiring future work
* Documented planned changes

Do not generate speculative improvement proposals.

---

# Mermaid Diagram Guidelines

Use **Mermaid** for diagrams in technical documentation.

Choose the diagram type based on the information being described:

| Purpose                            | Mermaid           |
| ---------------------------------- | ----------------- |
| Architecture                       | `flowchart`       |
| Data Flow                          | `flowchart`       |
| Processing Flow                    | `flowchart`       |
| Component interaction              | `sequenceDiagram` |
| Class/data structure relationships | `classDiagram`    |
| State transitions                  | `stateDiagram-v2` |

### Diagram Rules

* Create diagrams only when they improve understanding.
* Do not create diagrams merely to satisfy the template.
* Keep diagrams focused on the relevant scope.
* Prefer several small diagrams over one excessively large diagram.
* Use actual component, class, function, and data names from the implementation.
* Do not invent relationships or interactions.
* Keep labels concise.
* Ensure every diagram matches the documented behavior.
* Ensure Mermaid syntax is valid.
* Do not use ASCII diagrams when Mermaid can represent the information clearly.

---

# Documentation Principles

## Describe Facts

Clearly distinguish:

* Implemented behavior
* Explicit requirements
* Assumptions
* Hypotheses
* Unknown behavior

If behavior cannot be determined reliably, state that it is unknown.

Do not present assumptions as facts.

## Explain Why

For non-obvious code, explain the reason for the behavior when it can be established.

Prefer:

> Measurements below the confidence threshold are rejected to prevent unstable plane estimation.

over:

> Check whether confidence is below the threshold.

## Prefer Stable Information

Document behavior and interfaces that are likely to remain meaningful as the implementation changes.

Avoid excessive documentation of:

* Local implementation details
* Temporary variables
* Obvious control flow
* Details that merely repeat the source code

## Keep Documentation Maintainable

* Keep explanations concise.
* Avoid unnecessary repetition.
* Use tables and diagrams when they improve clarity.
* Do not duplicate the same information across multiple chapters.
* Keep documentation proportional to the complexity of the code.

---

# Code Comments and API Documentation

When documentation is added directly to source code:

* Follow the language-specific documentation conventions defined by the project's instructions.
* Document public APIs and non-obvious behavior.
* Explain intent, constraints, and assumptions.
* Do not add comments that merely restate the code.
* Do not introduce functional changes while documenting code.

For C++ projects, follow the project's Doxygen conventions.

For Python projects, follow the project's docstring conventions.

---

# Validation

After creating or modifying documentation:

* Verify that documented behavior matches the implementation.
* Verify function names, class names, parameters, and interfaces.
* Check units and coordinate conventions.
* Check referenced files and components.
* Verify examples against the current implementation.
* Verify Mermaid diagrams against the actual architecture and processing flow.
* Ensure Mermaid diagrams are syntactically valid.
* Ensure documentation does not claim behavior that is not implemented.

If documentation reveals an ambiguity in the implementation, report the ambiguity rather than silently resolving it through an assumption.

---

# Change Discipline

* Documentation changes must not alter program behavior.
* Avoid unrelated refactoring.
* Do not rewrite useful existing documentation unnecessarily.
* Correct outdated or misleading documentation when it is within the affected scope.
* Keep documentation proportional to the complexity of the code.

When documenting a large system, prefer incremental documentation of the most important components rather than generating a large amount of low-value documentation.
