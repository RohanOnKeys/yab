"""
Metadata Loader for YAB.

This module provides MetadataLoader class for loading and parsing
metadata.yaml files from template directories.
"""

from pathlib import Path
from typing import Any, Dict
import yaml


class MetadataLoader:
    """Loader for template metadata.yaml files."""
    
    def load(self, metadata_path: Path) -> Dict[str, Any]:
        """
        Load and parse a metadata.yaml file.
        
        Args:
            metadata_path: Path to the metadata.yaml file.
            
        Returns:
            Dictionary containing the parsed metadata.
        """
        with open(metadata_path, 'r') as f:
            metadata = yaml.safe_load(f)
        
        return metadata
