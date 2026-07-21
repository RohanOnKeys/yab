# YAB Architecture Diagram

## Overview

YAB (Yet Another Boilerplate) is a Python library that generates PyTorch boilerplate code through a template-driven system. It provides both in-memory object creation (`yab.use()`) and code injection (`yab.write()`) capabilities.

## High-Level Architecture

```
┌─────────────────────────────────────────────────────────────────┐
│                         USER INTERFACE                           │
├─────────────────────────────────────────────────────────────────┤
│                                                                   │
│  ┌──────────────┐                    ┌──────────────┐            │
│  │  Python API  │                    │     CLI      │            │
│  │              │                    │              │            │
│  │ yab.use()    │                    │ yab use      │            │
│  │ yab.write()  │                    │ yab write    │            │
│  └──────┬───────┘                    └──────┬───────┘            │
│         │                                   │                    │
└─────────┼───────────────────────────────────┼───────────────────┘
          │                                   │
          └───────────────┬───────────────────┘
                          │
                          ▼
┌─────────────────────────────────────────────────────────────────┐
│                        CORE ENGINE                               │
├─────────────────────────────────────────────────────────────────┤
│                                                                   │
│  ┌─────────────────────────────────────────────────────────┐   │
│  │              CALLER RESOLVER                             │   │
│  │  Determines where YAB was called from:                   │   │
│  │  - Python scripts                                        │   │
│  │  - VS Code                                               │   │
│  │  - Jupyter notebooks                                     │   │
│  └────────────────────┬────────────────────────────────────┘   │
│                       │                                          │
│                       ▼                                          │
│  ┌─────────────────────────────────────────────────────────┐   │
│  │            TEMPLATE REGISTRY                             │   │
│  │  Stores available templates with:                        │   │
│  │  - Parameter schemas                                     │   │
│  │  - Supported abstraction levels                         │   │
│  │  - Template versions                                     │   │
│  └────────────────────┬────────────────────────────────────┘   │
│                       │                                          │
│                       ▼                                          │
│  ┌─────────────────────────────────────────────────────────┐   │
│  │                 RENDERER                                 │   │
│  │  Uses Jinja2 to transform templates into PyTorch code:   │   │
│  │  - Parameter substitution                                │   │
│  │  - Validation                                            │   │
│  │  - Code generation                                       │   │
│  └────────────────────┬────────────────────────────────────┘   │
│                       │                                          │
│                       ▼                                          │
│  ┌─────────────────────────────────────────────────────────┐   │
│  │              ABSTRACTION LAYER                           │   │
│  │  Wraps generated code into three levels:                │   │
│  │                                                          │   │
│  │  ┌──────────┐  ┌──────────┐  ┌──────────┐              │   │
│  │  │   FULL   │  │ PARTIAL  │  │   RAW    │              │   │
│  │  │          │  │          │  │          │              │   │
│  │  │ Complete │  │ Major   │  │ Model   │              │   │
│  │  │ trainer  │  │ components│ │ only    │              │   │
│  │  └──────────┘  └──────────┘  └──────────┘              │   │
│  └────────────────────┬────────────────────────────────────┘   │
│                       │                                          │
│                       ▼                                          │
│  ┌─────────────────────────────────────────────────────────┐   │
│  │                 INJECTOR                                  │   │
│  │  Inserts generated code into existing projects:          │   │
│  │                                                          │   │
│  │  ┌──────────────────┐  ┌──────────────────┐            │   │
│  │  │  Script Writer   │  │ Notebook Writer  │            │   │
│  │  │                  │  │                  │            │   │
│  │  │ AST-based        │  │ Notebook model   │            │   │
│  │  │ injection        │  │ manipulation     │            │   │
│  │  └──────────────────┘  └──────────────────┘            │   │
│  └────────────────────┬────────────────────────────────────┘   │
│                       │                                          │
│                       ▼                                          │
│  ┌─────────────────────────────────────────────────────────┐   │
│  │                 FORMATTER                                 │   │
│  │  Auto-formats generated code:                            │   │
│  │  - Black formatting                                      │   │
│  │  - Ruff linting                                          │   │
│  └─────────────────────────────────────────────────────────┘   │
│                                                                   │
└─────────────────────────────────────────────────────────────────┘
                          │
                          ▼
┌─────────────────────────────────────────────────────────────────┐
│                      TEMPLATE LIBRARY                             │
├─────────────────────────────────────────────────────────────────┤
│                                                                   │
│  ┌─────────────────┐  ┌─────────────────┐  ┌─────────────────┐  │
│  │ image_classifier│  │tabular_classifier│ │ text_classifier │  │
│  │                 │  │                 │  │                 │  │
│  │ - metadata.yaml │  │ - metadata.yaml │  │ - metadata.yaml │  │
│  │ - full.py.j2    │  │ - full.py.j2    │  │ - full.py.j2    │  │
│  │ - partial.py.j2 │  │ - partial.py.j2 │  │ - partial.py.j2 │  │
│  │ - raw.py.j2     │  │ - raw.py.j2     │  │ - raw.py.j2     │  │
│  └─────────────────┘  └─────────────────┘  └─────────────────┘  │
│                                                                   │
│  ┌─────────────────┐  ┌─────────────────┐                        │
│  │   autoencoder   │  │       GAN       │                        │
│  │                 │  │                 │                        │
│  │ (Under Dev)     │  │ (Under Dev)     │                        │
│  └─────────────────┘  └─────────────────┘                        │
│                                                                   │
│  ┌─────────────────┐                                             │
│  │transformer_finetune│                                            │
│  │                 │                                             │
│  │ (Under Dev)     │                                             │
│  └─────────────────┘                                             │
│                                                                   │
└─────────────────────────────────────────────────────────────────┘
```

## Data Flow

### `yab.use()` Flow (In-Memory Object)

```
User calls yab.use()
    │
    ▼
Caller Resolver identifies call context
    │
    ▼
Template Registry validates template name & parameters
    │
    ▼
Renderer generates PyTorch code from Jinja2 template
    │
    ▼
Abstraction Layer wraps code based on type (full/partial/raw)
    │
    ▼
Return Python object to user (no file writing)
```

### `yab.write()` Flow (Code Injection)

```
User calls yab.write()
    │
    ▼
Caller Resolver identifies target file/notebook
    │
    ▼
Template Registry validates template name & parameters
    │
    ▼
Renderer generates PyTorch code from Jinja2 template
    │
    ▼
Abstraction Layer wraps code based on type (full/partial/raw)
    │
    ▼
Injector inserts code into target:
    ├── Script Writer: AST-based injection for .py files
    └── Notebook Writer: Cell manipulation for .ipynb files
    │
    ▼
Formatter applies Black and Ruff formatting
    │
    ▼
Code written to disk (or notebook updated)
```

## Component Details

### 1. Caller Resolver
**Purpose**: Determine execution context
**Inputs**: Stack trace, environment
**Outputs**: File path, execution context (script/notebook)
**Key Logic**:
- Detects if called from Python script, VS Code, or Jupyter
- Locates target file for code injection
- Handles different IDE environments

### 2. Template Registry
**Purpose**: Manage available templates
**Data Structure**: Dictionary of template metadata
**Key Operations**:
- Register new templates
- Validate template names
- Check parameter schemas
- Return template metadata

### 3. Renderer
**Purpose**: Generate code from templates
**Technology**: Jinja2 templating engine
**Key Operations**:
- Load Jinja2 template files (.j2)
- Substitute parameters
- Validate generated code
- Return Python source code

### 4. Abstraction Layer
**Purpose**: Provide different levels of encapsulation
**Three Levels**:
- **Full**: Complete trainer with training, validation, prediction, checkpointing
- **Partial**: Major components (model, trainer) but user controls training loop
- **Raw**: Only the model, everything else user-controlled

### 5. Injector
**Purpose**: Safely insert code into existing projects
**Two Writers**:
- **Script Writer**: Uses Python AST to modify .py files without breaking syntax
- **Notebook Writer**: Manipulates Jupyter notebook cell structure
**Key Feature**: Detects and updates existing YAB blocks instead of duplicating

### 6. Formatter
**Purpose**: Ensure code quality
**Tools**: Black (formatting), Ruff (linting)
**Operation**: Runs on all generated code before writing

## Template Structure

Each template follows this structure:

```
template_name/
├── metadata.yaml       # Template configuration
├── README.md          # Documentation
├── full.py.j2         # Full abstraction template
├── partial.py.j2      # Partial abstraction template
└── raw.py.j2          # Raw abstraction template
```

### metadata.yaml Schema
```yaml
name: template_name
version: 1.0.0
supports: [full, partial, raw]
task:
  domain: domain_name
  type: task_type
parameters:
  parameter_name:
    type: data_type
    required: boolean
    default: default_value
```

## Current Implementation Status

**Completed**:
- Project structure and scaffolding
- Template directory structure
- Metadata schema design
- Jinja2 template placeholders

**Under Development**:
- Core engine implementation (most __init__.py files are empty)
- Caller resolver logic
- Template registry implementation
- Renderer implementation
- Abstraction layer implementation
- Injector implementation
- Formatter integration
- CLI implementation

**Planned**:
- Template implementations (classifier, autoencoder, GAN, transformer)
- Comprehensive test suite
- Documentation and examples
- PyPI publishing

## Key Design Principles

1. **Template-Driven**: Easy to add new templates without modifying core engine
2. **AST-Based Injection**: Safe code modification that preserves syntax
3. **Three Abstraction Levels**: Flexibility from rapid prototyping to full control
4. **Editable Output**: Generated code belongs to the user
5. **Auto-Formatting**: Always produces clean, readable code
6. **Jupyter Support**: Works in both scripts and notebooks
