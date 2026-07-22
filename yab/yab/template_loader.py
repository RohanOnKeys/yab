"""
Template Loader for YAB.

This module provides TemplateLoader class for locating template files.
"""

from pathlib import Path
from typing import TYPE_CHECKING

if TYPE_CHECKING:
    from .core.template_registry import TemplateRegistry, TemplateInfo


class InvalidAbstractionError(Exception):
    """Raised when an invalid abstraction is requested."""
    pass


class TemplateFileNotFoundError(Exception):
    """Raised when a template file is not found on disk."""
    pass


class TemplateLoader:
    """Loader for locating Jinja template files."""
    
    def __init__(self, registry: "TemplateRegistry"):
        """
        Initialize the template loader.
        
        Args:
            registry: TemplateRegistry instance for template lookup.
        """
        self.registry = registry
    
    def load(self, template_name: str, abstraction: str) -> Path:
        """
        Load the path to a template file.
        
        Args:
            template_name: Name of the template.
            abstraction: Abstraction level (raw, partial, or full).
            
        Returns:
            Path to the Jinja template file.
            
        Raises:
            InvalidAbstractionError: If the abstraction is not supported.
            TemplateFileNotFoundError: If the template file does not exist.
        """
        template_info = self.registry.get(template_name)
        
        # Validate abstraction
        if abstraction not in template_info.abstractions:
            raise InvalidAbstractionError(
                f"Abstraction '{abstraction}' not supported by template '{template_name}'. "
                f"Supported abstractions: {', '.join(template_info.abstractions)}"
            )
        
        # Construct template file path
        template_path = template_info.directory / f"{abstraction}.py.j2"
        
        # Check if file exists
        if not template_path.exists():
            raise TemplateFileNotFoundError(
                f"Template file not found: {template_path}"
            )
        
        return template_path
