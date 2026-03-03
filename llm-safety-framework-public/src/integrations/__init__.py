"""
Attack library integration adapters.

Optional integrations with garak, pyrit, and deepteam.
The framework works without them — they are detected at runtime.
"""

from .detector import detect_all
from .garak_adapter import GarakAdapter
from .pyrit_adapter import PyRITAdapter
from .deepteam_adapter import DeepTeamAdapter

__all__ = [
    "detect_all",
    "GarakAdapter",
    "PyRITAdapter",
    "DeepTeamAdapter",
]
