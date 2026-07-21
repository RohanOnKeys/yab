"""
Template Renderer for YAB.

This module provides TemplateRenderer class for rendering Jinja templates
into Python source code strings.
"""

from pathlib import Path
from typing import Any, Dict
from jinja2 import Environment, FileSystemLoader, TemplateNotFound, TemplateSyntaxError


class TemplateRenderError(Exception):
    """Raised when template rendering fails."""
    pass


class TemplateRenderer:
    """Renderer for Jinja templates."""
    
    def __init__(self):
        """Initialize the template renderer."""
        self.env = Environment(loader=FileSystemLoader('.'))
    
    def render(self, template_path: Path, context: Dict[str, Any]) -> str:
        """
        Render a Jinja template with the given context.
        
        Args:
            template_path: Path to the Jinja template file.
            context: Dictionary of variables to pass to the template.
            
        Returns:
            Rendered Python source code as a string.
            
        Raises:
            TemplateRenderError: If the template file is missing or rendering fails.
        """
        if not template_path.exists():
            raise TemplateRenderError(
                f"Template file not found: {template_path}"
            )
        
        try:
            # Get the directory and filename for Jinja2 loader
            template_dir = template_path.parent
            template_name = template_path.name
            
            # Create environment with the template directory
            env = Environment(loader=FileSystemLoader(str(template_dir)))
            
            # Load and render the template
            template = env.get_template(template_name)
            rendered = template.render(**context)
            
            return rendered
            
        except TemplateNotFound as e:
            raise TemplateRenderError(
                f"Template not found: {e}"
            )
        except TemplateSyntaxError as e:
            raise TemplateRenderError(
                f"Template syntax error at line {e.lineno}: {e.message}"
            )
        except Exception as e:
            raise TemplateRenderError(
                f"Template rendering failed: {e}"
            )
