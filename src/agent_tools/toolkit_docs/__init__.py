"""
Toolkit Docs — self-documenting toolkit introspection.

Introspects all agent_tools sub-packages to generate capability
matrices, API summaries, and workflow documentation on the fly.
"""

from src.agent_tools.toolkit_docs.introspector import ToolkitIntrospector
from src.agent_tools.toolkit_docs.capability_matrix import CapabilityMatrix
from src.agent_tools.toolkit_docs.workflow_guide import WorkflowGuide

__all__ = ["ToolkitIntrospector", "CapabilityMatrix", "WorkflowGuide"]
