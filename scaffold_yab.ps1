<#
    scaffold_yab.ps1

    Creates the complete YAB project scaffold.

    Features
    --------
    - Python package layout
    - __init__.py in every package
    - .gitkeep in empty non-package folders
    - .gitignore
    - .env
    - .env.example

    Usage:
        .\scaffold_yab.ps1
        .\scaffold_yab.ps1 -Root "C:\Projects\yab"
#>

param(
    [string]$Root = "yab"
)

# ----------------------------
# Python packages
# ----------------------------

$packages = @(
    "$Root\yab",
    "$Root\yab\core",
    "$Root\yab\core\caller_resolver",
    "$Root\yab\core\template_registry",
    "$Root\yab\core\renderer",
    "$Root\yab\core\abstraction",
    "$Root\yab\core\abstraction\full",
    "$Root\yab\core\abstraction\partial",
    "$Root\yab\core\abstraction\raw",
    "$Root\yab\core\injector",
    "$Root\yab\core\injector\script_writer",
    "$Root\yab\core\injector\notebook_writer",
    "$Root\yab\core\formatter",
    "$Root\yab\templates",
    "$Root\yab\templates\classifier",
    "$Root\yab\templates\autoencoder",
    "$Root\yab\templates\gan",
    "$Root\yab\templates\transformer_finetune",
    "$Root\yab\cli",
    "$Root\tests",
    "$Root\tests\core",
    "$Root\tests\templates"
)

# ----------------------------
# Non-package directories
# ----------------------------

$dirs = @(
    "$Root",
    "$Root\docs",
    "$Root\docs\usage",
    "$Root\.github",
    "$Root\.github\workflows"
)

# ----------------------------
# Create directories
# ----------------------------

foreach ($dir in ($packages + $dirs)) {
    New-Item -ItemType Directory -Force -Path $dir | Out-Null
}

# ----------------------------
# Create __init__.py
# ----------------------------

foreach ($pkg in $packages) {

    $init = Join-Path $pkg "__init__.py"

    if (!(Test-Path $init)) {
        New-Item -ItemType File -Path $init | Out-Null
    }

}

# ----------------------------
# Create .gitkeep
# ----------------------------

foreach ($dir in ($dirs + @(
    "$Root\docs",
    "$Root\docs\usage",
    "$Root\.github",
    "$Root\.github\workflows"
))) {

    $gitkeep = Join-Path $dir ".gitkeep"

    if (!(Test-Path $gitkeep)) {
        New-Item -ItemType File -Path $gitkeep | Out-Null
    }

}

# ----------------------------
# .gitignore
# ----------------------------

@"
# Bytecode
__pycache__/
*.py[cod]

# Virtual environments
.venv/
venv/
env/

# Environment
.env

# IDE
.vscode/
.idea/

# Python
.python-version
.pytest_cache/
.mypy_cache/
.ruff_cache/

# Coverage
.coverage
htmlcov/

# Build
build/
dist/
*.egg-info/

# Jupyter
.ipynb_checkpoints/

# macOS
.DS_Store

# Windows
Thumbs.db
"@ | Set-Content "$Root\.gitignore"

# ----------------------------
# .env.example
# ----------------------------

@"
YAB_ENV=development
YAB_LOG_LEVEL=INFO
"@ | Set-Content "$Root\.env.example"

# ----------------------------
# .env
# ----------------------------

@"
YAB_ENV=development
YAB_LOG_LEVEL=INFO
"@ | Set-Content "$Root\.env"

Write-Host ""
Write-Host "================================="
Write-Host "YAB scaffold created successfully."
Write-Host "Location: $Root"
Write-Host "================================="