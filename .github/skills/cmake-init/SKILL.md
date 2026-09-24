---

name: cmake-init
description: Initialize and configure CMake-based C++ projects, including CMakeLists.txt creation, target configuration, dependencies, build directories, and build/test validation.
---

# CMake Init Skill

## Objective

Initialize and configure C++ projects using CMake.

The goal is to create a simple, maintainable, reproducible CMake build configuration that reflects the actual project structure and requirements.

Use this Skill when:

* Creating a new CMake-based C++ project
* Creating a `CMakeLists.txt`
* Adding CMake build support to an existing C++ project
* Adding a library or executable target
* Adding test targets
* Configuring dependencies
* Setting up a CMake build directory
* Validating a CMake project

Do not use this Skill for general CMake coding style. CMake-specific implementation rules are defined in `cmake.instructions.md`.

---

# Workflow

## 1. Inspect the Project

Before creating or modifying CMake configuration:

* Inspect the repository structure.
* Identify C++ source and header files.
* Check whether `CMakeLists.txt` already exists.
* Check for existing CMake configuration.
* Check existing build systems such as:

  * Makefiles
  * Visual Studio projects
  * Ninja configuration
  * custom build scripts
* Identify the required C++ standard.
* Identify existing libraries and dependencies.
* Check existing tests.
* Check toolchain or cross-compilation requirements.
* Check existing build documentation.

Do not create a new build structure without first understanding the existing project.

If an existing CMake configuration is usable, modify it rather than replacing it.

---

# 2. Determine the Build Structure

Determine the appropriate CMake structure from the actual project.

Identify:

* Executable targets
* Library targets
* Test targets
* Public and private dependencies
* Include directories
* Generated files
* External dependencies
* Install requirements when applicable

Prefer a target-oriented structure.

Do not create unnecessary subdirectories or CMake files.

For a small project, a single root `CMakeLists.txt` may be sufficient.

For a larger project, use subdirectory `CMakeLists.txt` files when they provide a clear separation of components.

---

# 3. Create the Root CMakeLists.txt

For a new project, create a minimal root `CMakeLists.txt`.

The root configuration should normally define:

* Minimum required CMake version
* Project name
* Project language
* Project targets or subdirectories
* Relevant project-wide configuration

Example:

```cmake
cmake_minimum_required(VERSION 3.20)

project(example_project
    LANGUAGES CXX
)

add_executable(example
    src/main.cpp
)
```

Use a CMake version compatible with the project and target environment.

Do not raise the minimum CMake version without a reason.

---

# 4. Configure Targets

Use CMake targets to represent build artifacts.

Typical targets include:

* Executables
* Static libraries
* Shared libraries
* Interface libraries
* Test executables

Prefer:

```text id="h3qk0j"
target_include_directories()
target_compile_features()
target_compile_definitions()
target_compile_options()
target_link_libraries()
```

over global configuration such as:

```text id="v2g8hm"
include_directories()
add_definitions()
link_libraries()
```

Keep configuration attached to the target it affects.

---

# 5. Configure the C++ Standard

Determine the C++ standard from the project requirements.

Prefer target-specific configuration.

For example:

```text id="6o0bti"
target_compile_features(example
    PRIVATE
    cxx_std_17
)
```

If the project explicitly requires another C++ standard, preserve that requirement.

Do not upgrade the C++ standard merely to use newer language features.

---

# 6. Configure Include Directories

Add include directories according to actual dependency relationships.

Use:

```text id="z7j7a1"
target_include_directories()
```

Prefer the appropriate visibility:

* `PRIVATE` — implementation-only headers
* `PUBLIC` — required by both implementation and consumers
* `INTERFACE` — required only by consumers

Do not add the entire repository as a global include directory unless required by the project.

Avoid include paths that hide incorrect include statements.

---

# 7. Configure Dependencies

Before adding a dependency:

* Check whether the project already provides the required functionality.
* Check whether the dependency is already available.
* Reuse existing project infrastructure.
* Check target-platform compatibility.
* Consider cross-compilation requirements.
* Consider binary size and runtime dependencies for embedded targets.

Prefer existing dependency-management mechanisms.

Do not introduce `FetchContent`, `ExternalProject`, package managers, or new third-party dependencies unless there is a clear project requirement.

For Windows projects in this Harness environment, GoogleTest is provided by the shared vcpkg installation:

* vcpkg root: the `VCPKG_ROOT` environment variable
* package: `gtest:x64-windows`
* toolchain: `$env:VCPKG_ROOT\scripts\buildsystems\vcpkg.cmake`

When a project uses GoogleTest, configure it with:

```powershell
cmake -S . -B build -DCMAKE_TOOLCHAIN_FILE="$env:VCPKG_ROOT\scripts\buildsystems\vcpkg.cmake" -DVCPKG_TARGET_TRIPLET=x64-windows
```

Use `find_package(GTest CONFIG REQUIRED)` and link `GTest::gtest` or `GTest::gtest_main`.
Do not use `FetchContent`, `ExternalProject`, or copy GoogleTest into the project.

When linking dependencies, prefer:

```text id="z8j3g4"
target_link_libraries()
```

with explicit visibility.

Do not use global linker configuration when target-specific configuration is sufficient.

---

# 8. Source Files

Explicitly list source files when practical.

Prefer:

```text id="4z7t3h"
add_library(core
    src/foo.cpp
    src/bar.cpp
)
```

over:

```text id="j1c0xk"
file(GLOB SOURCES ...)
```

Do not introduce `file(GLOB)` into a project unless it is already an established project convention or there is a specific reason to use it.

Do not automatically include every source file in the repository.

---

# 9. Tests

When tests are part of the project:

* Identify the existing test framework.
* Preserve the existing framework.
* Add test targets separately from production targets.
* Avoid linking test-only dependencies into production targets.
* Register tests with CTest when appropriate.

For GoogleTest projects, follow the project's `cpp-test.instructions.md`.

A typical structure may be:

```text id="w5i5j5"
project/
├── CMakeLists.txt
├── src/
│   ├── ...
│   └── ...
├── include/
│   └── ...
└── tests/
    ├── CMakeLists.txt
    └── ...
```

Do not introduce a test framework solely because CMake initialization is being performed.

---

# 10. Build Directory

Use an out-of-source build.

Typical configuration:

```text id="xkdb4d"
cmake -S . -B build
cmake --build build
```

Keep generated build files outside the source tree when possible.

Do not commit generated build artifacts.

If the project already uses a different build directory convention, follow it.

---

# 11. Toolchains and Cross Compilation

Before configuring a project, check whether it targets:

* Desktop Linux
* Windows
* macOS
* Embedded Linux
* Android
* Other embedded platforms
* Custom SDKs
* Cross-compilers

Respect existing:

* Toolchain files
* SDK environment variables
* Compiler selection
* Sysroots
* Architecture settings
* Platform-specific configuration

Do not hard-code compiler paths, SDK paths, or machine-specific directories.

For cross-compilation, use the project's established toolchain mechanism.

---

# 12. Build Configuration

Keep build configuration explicit and minimal.

Use CMake options only when a feature genuinely needs to be selectable.

For example:

```text id="n0q3h1"
option(BUILD_TESTING "Build tests" ON)
```

Do not create options for every configuration value.

Avoid globally overriding:

* Compiler flags
* Linker flags
* Optimization settings
* Warning settings

unless required by the project's build architecture.

Prefer target-specific settings where possible.

---

# 13. Installation and Packaging

If the project is a library or distributable package:

* Inspect existing installation requirements.
* Preserve existing install rules.
* Configure targets for installation when required.
* Preserve package/export configuration when present.

Do not add installation or packaging support to a project that does not require it.

Do not remove existing packaging configuration during CMake cleanup.

---

# 14. Configure and Build

After creating or modifying CMake configuration:

Configure the project:

```text id="z1y6b0"
cmake -S . -B build
```

Build the affected targets:

```text id="2n0x5h"
cmake --build build
```

When appropriate, build with the project's expected configuration, for example:

```text id="7j7j9c"
cmake --build build --config Release
```

For cross-compilation, use the project's required toolchain and build procedure.

Do not claim that the project builds successfully unless the build was actually executed.

---

# 15. Test

When tests are configured:

```text id="6f6n7v"
ctest --test-dir build --output-on-failure
```

or use the project's established test command.

Run relevant tests after changing build configuration.

If tests cannot be run because of unavailable hardware, SDKs, dependencies, or environment requirements, report the limitation explicitly.

---

# 16. Validation

After CMake initialization or modification:

* Confirm CMake configuration succeeds.
* Confirm the intended targets are generated.
* Build affected targets.
* Run relevant tests.
* Check compiler and linker errors.
* Check warnings when relevant.
* Verify include and library dependencies.
* Verify generated files are in the build directory.
* Review the CMake diff.
* Confirm no unrelated files were modified.

When appropriate, inspect the generated build configuration to ensure the expected compiler, architecture, definitions, and dependencies are being used.

---

# CMake Project Structure

Use the simplest structure appropriate for the project.

### Small executable

```text id="x9y6u2"
project/
├── CMakeLists.txt
└── src/
    └── main.cpp
```

### Library

```text id="h4m4x8"
project/
├── CMakeLists.txt
├── include/
│   └── ...
├── src/
│   └── ...
└── tests/
    └── ...
```

### Larger project

```text id="b7r8c2"
project/
├── CMakeLists.txt
├── cmake/
├── src/
│   ├── component_a/
│   │   └── CMakeLists.txt
│   └── component_b/
│       └── CMakeLists.txt
├── include/
├── tests/
│   └── CMakeLists.txt
└── build/
```

Do not impose these layouts when an existing project already has an established structure.

---

# Change Discipline

* Inspect before modifying.
* Prefer the smallest CMake change that solves the problem.
* Preserve existing build behavior unless a change is required.
* Do not rewrite an existing CMake project unnecessarily.
* Do not introduce unnecessary dependencies.
* Do not introduce unnecessary CMake features.
* Do not modernize CMake merely for stylistic reasons.
* Do not mix unrelated source-code refactoring with build-system changes.
* Do not hard-code machine-specific paths.
* Do not modify unrelated files.

The resulting CMake configuration should be understandable, reproducible, and appropriate for the target environment.
