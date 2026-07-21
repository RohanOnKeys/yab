"""
Utilities for resolving information about the calling code.
"""

from __future__ import annotations

import inspect
from pathlib import Path

from IPython import get_ipython

from .exceptions import CallerResolutionError
from .models import CallerInfo, ExecutionContext


def _detect_context() -> ExecutionContext:
    """
    Detect the current execution environment.

    Returns:
        ExecutionContext representing the active environment.
    """

    try:
        shell = get_ipython()
    except Exception:
        return ExecutionContext.SCRIPT

    if shell is None:
        return ExecutionContext.SCRIPT

    shell_name = shell.__class__.__name__

    if shell_name == "ZMQInteractiveShell":
        return ExecutionContext.JUPYTER

    if shell_name == "TerminalInteractiveShell":
        return ExecutionContext.VSCODE

    return ExecutionContext.UNKNOWN


def resolve_caller(stack_offset: int = 2) -> CallerInfo:
    """
    Resolve information about the caller.

    Args:
        stack_offset:
            Index within the current stack that represents the caller.

    Returns:
        CallerInfo containing file, line, function, and execution context.

    Raises:
        CallerResolutionError:
            If the caller cannot be determined.
    """

    stack = inspect.stack()

    if len(stack) <= stack_offset:
        raise CallerResolutionError("Unable to resolve caller.")

    frame = stack[stack_offset]

    return CallerInfo(
        file_path=Path(frame.filename) if frame.filename else None,
        line_number=frame.lineno,
        function_name=frame.function,
        context=_detect_context(),
    )