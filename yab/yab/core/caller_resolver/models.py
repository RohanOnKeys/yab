"""
Data models used by the caller resolver.
"""

from dataclasses import dataclass
from enum import Enum
from pathlib import Path


class ExecutionContext(str, Enum):
    """
    Supported execution environments.
    """

    SCRIPT = "script"
    JUPYTER = "jupyter"
    VSCODE = "vscode"
    UNKNOWN = "unknown"


@dataclass(slots=True)
class CallerInfo:
    """
    Stores information about the code that invoked YAB.
    """

    file_path: Path | None
    line_number: int
    function_name: str
    context: ExecutionContext