# YAB

> Yet Another Boilerplate

Generate complete PyTorch training pipelines inside your existing project with a single function call or CLI command.

YAB eliminates repetitive PyTorch setup by generating clean, formatted, fully editable code directly into your Python scripts or Jupyter notebooks. The generated code is standard PyTorch that you own and can modify freely.

## Features

- Generate complete PyTorch training pipelines
- Works with Python scripts and Jupyter notebooks
- Produces clean, readable, production ready code
- Updates previously generated code instead of creating duplicates
- Automatically formats generated code
- Versioned templates for reproducible projects
- Simple Python API and CLI
- Easily extensible with additional templates

## Installation

```bash
pip install yab
```

## Quick Start

### Python

```python
import yab

yab.scaffold("classifier")
```

### Command Line

```bash
yab init classifier
```

The generated code is inserted directly into your file. Once generated, it is ordinary PyTorch code that you can edit, extend, and debug.

## Planned Templates

- Classifier
- Autoencoder
- GAN
- Transformer Fine Tune

More templates will be added in future releases.

## Philosophy

YAB does not introduce another deep learning framework.

Instead, it generates clean PyTorch code that feels like it was written by hand. There are no runtime wrappers and no hidden abstractions.

## Tech Stack

- Python
- PyTorch
- Jinja2
- libcst
- black
- ruff
- nbformat
- GitHub Actions
- pytest

## Roadmap

Version 1 includes

- Python script support
- Jupyter notebook support
- Automatic formatting
- Multiple templates
- Stable public API
- PyPI release

## Contributing

Contributions are welcome. Feel free to open an issue or submit a pull request.

## License

This project is licensed under the MIT License.
