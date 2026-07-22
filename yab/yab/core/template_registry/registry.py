"""
Template Registry for YAB.

This module provides TemplateRegistry class for managing available templates.
"""

from pathlib import Path
from typing import List, Dict, Any


class TemplateNotFoundError(Exception):
    """Raised when a requested template is not found in the registry."""
    pass


class TemplateInfo:
    """Information about a registered template."""
    
    def __init__(
        self,
        name: str,
        directory: Path,
        metadata_path: Path,
        readme_path: Path,
        abstractions: List[str]
    ):
        self.name = name
        self.directory = directory
        self.metadata_path = metadata_path
        self.readme_path = readme_path
        self.abstractions = abstractions
    
    def to_dict(self) -> Dict[str, Any]:
        """Convert template info to dictionary."""
        return {
            "name": self.name,
            "directory": str(self.directory),
            "metadata_path": str(self.metadata_path),
            "readme_path": str(self.readme_path),
            "abstractions": self.abstractions
        }


class TemplateRegistry:
    """Registry for managing available YAB templates."""
    
    def __init__(self, templates_dir: Path):
        """
        Initialize the template registry.
        
        Args:
            templates_dir: Path to the templates directory.
        """
        self.templates_dir = templates_dir
        self._templates: Dict[str, TemplateInfo] = {}
        self._register_templates()
    
    def _register_templates(self) -> None:
        """Register available templates."""
        abstractions = ["raw", "partial", "full"]
        
        # Register image_classifier
        self._templates["image_classifier"] = TemplateInfo(
            name="image_classifier",
            directory=self.templates_dir / "image_classifier",
            metadata_path=self.templates_dir / "image_classifier" / "metadata.yaml",
            readme_path=self.templates_dir / "image_classifier" / "README.md",
            abstractions=abstractions
        )
        
        # Register text_classifier
        self._templates["text_classifier"] = TemplateInfo(
            name="text_classifier",
            directory=self.templates_dir / "text_classifier",
            metadata_path=self.templates_dir / "text_classifier" / "metadata.yaml",
            readme_path=self.templates_dir / "text_classifier" / "README.md",
            abstractions=abstractions
        )
        
        # Register tabular_classifier
        self._templates["tabular_classifier"] = TemplateInfo(
            name="tabular_classifier",
            directory=self.templates_dir / "tabular_classifier",
            metadata_path=self.templates_dir / "tabular_classifier" / "metadata.yaml",
            readme_path=self.templates_dir / "tabular_classifier" / "README.md",
            abstractions=abstractions
        )
    
    def get(self, template_name: str) -> TemplateInfo:
        """
        Get template information by name.
        
        Args:
            template_name: Name of the template to retrieve.
            
        Returns:
            TemplateInfo object for the requested template.
            
        Raises:
            TemplateNotFoundError: If the template is not found.
        """
        if template_name not in self._templates:
            available = ", ".join(self.list_templates())
            raise TemplateNotFoundError(
                f"Template '{template_name}' not found. "
                f"Available templates: {available}"
            )
        return self._templates[template_name]
    
    def list_templates(self) -> List[str]:
        """
        List all registered template names.
        
        Returns:
            List of template names.
        """
        return list(self._templates.keys())
