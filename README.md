# YAB

> Yet Another Boilerplate

YAB is a Python library that removes repetitive PyTorch boilerplate without taking away control.

It provides two ways to build projects:

- `yab.use()` returns a ready-to-use object in memory.
- `yab.write()` injects clean, editable PyTorch code directly into your Python file or Jupyter notebook.

Unlike frameworks that hide everything behind custom APIs, YAB generates real code that belongs to you.

---

# Features

- Zero-boilerplate PyTorch workflows
- Editable generated source code
- Three abstraction levels
- Python API and CLI
- AST-based code injection
- Jupyter notebook support
- Automatic formatting with Black and Ruff
- Versioned templates
- Extensible template registry

---

# Installation

```bash
pip install yab
```

---

# Quick Start

## Return an object

```python
import yab

model = yab.use(
    "classifier",
    type="full",
    num_classes=10,
)
```

Nothing is written to disk.

---

## Generate boilerplate

```python
import yab

yab.write(
    "classifier",
    num_classes=10,
)
```

YAB inserts formatted PyTorch code at the top of the current file.

---

# Abstraction Levels

## Full

Returns a single object exposing training, prediction, checkpointing, and inference.

Ideal for rapid prototyping.

```python
classifier = yab.use("classifier", type="full")
```

---

## Partial

Returns major components while hiding repetitive training code.

Useful when replacing optimizers, datasets, schedulers, or models.

```python
model, trainer = yab.use(
    "classifier",
    type="partial",
)
```

---

## Raw

Returns only the generated model.

Everything else is left entirely under your control.

```python
model = yab.use(
    "classifier",
    type="raw",
)
```

---

# CLI

```bash
yab use classifier

yab write classifier

yab list

yab types

yab init classifier

yab update

yab version
```

---

# Project Layout

```
yab/
│
├── pyproject.toml
├── README.md
├── .gitignore
├── .env
├── .env.example
│
├── yab/
│   ├── __init__.py
│   │
│   ├── cli/
│   │
│   ├── core/
│   │   ├── caller_resolver/
│   │   ├── template_registry/
│   │   ├── renderer/
│   │   ├── abstraction/
│   │   │   ├── full/
│   │   │   ├── partial/
│   │   │   └── raw/
│   │   ├── injector/
│   │   │   ├── script_writer/
│   │   │   └── notebook_writer/
│   │   └── formatter/
│   │
│   └── templates/
│       ├── classifier/
│       ├── autoencoder/
│       ├── gan/
│       └── transformer_finetune/
│
├── tests/
├── docs/
└── .github/
```

---

# Architecture

YAB is organized into small, independent components.

## Caller Resolver

Determines where YAB was called from.

- Python scripts
- VS Code
- Jupyter notebooks

Responsible for locating the target file or notebook before any generation begins.

---

## Template Registry

Stores every available boilerplate template together with:

- parameter schema
- supported abstraction levels
- template versions

New templates can be added without changing the rendering pipeline.

---

## Renderer

Uses Jinja2 to transform templates into complete PyTorch source code.

Handles parameter substitution and validation before generation.

---

## Abstraction

Wraps generated templates into three levels:

- Full
- Partial
- Raw

Each exposes a different amount of implementation detail while using the same underlying template.

---

## Injector

Safely inserts generated code into existing projects.

Python scripts are modified through AST analysis.

Jupyter notebooks are updated through their notebook model.

Repeated writes update previous YAB blocks instead of creating duplicates.

---

## Formatter

Automatically formats generated code using:

- Black
- Ruff

Generated code is always clean and readable.

---

# Templates

Current planned templates include:

- Classifier
- Autoencoder
- GAN
- Transformer Fine-Tuning

The architecture is intentionally template-driven so additional domains can be added later without modifying the core engine.

---

# Testing

Testing covers much more than syntax.

- Template rendering
- AST injection
- Notebook injection
- Duplicate detection
- Formatting
- Generated code execution
- End-to-end training on toy datasets
- CLI behavior

---

# Continuous Integration

Every push runs:

- Ruff
- Black
- Pytest

Tagged releases publish automatically to PyPI.

---

# Roadmap

## Week 1

Build the core pipeline around a single classifier template.

- Caller Resolver
- Template Registry
- Renderer
- Script injection
- Full abstraction

---

## Week 2

Expand functionality.

- Notebook support
- Partial abstraction
- Raw abstraction
- Automatic formatting
- CLI
- Autoencoder template

---

## Week 3

Scale the template library.

- GAN
- Transformer Fine-Tuning
- Template versioning
- Parser hardening
- Full test suite

---

## Week 4

Prepare the public release.

- Documentation
- Examples
- Landing page
- CI publishing
- PyPI release
- Version 1.0

---

# Philosophy

Most libraries replace boilerplate with another abstraction.

YAB replaces boilerplate with your own code.

You keep complete ownership of what is generated while avoiding hours of repetitive setup.

---

# License

MIT