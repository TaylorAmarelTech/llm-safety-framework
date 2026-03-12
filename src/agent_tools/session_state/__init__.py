"""
Session State — track in-progress work and enable atomic rollback.

Provides centralized state management for agent sessions: what's being
worked on, which files have been modified, and rollback on failure.
"""

from src.agent_tools.session_state.session_manager import SessionManager
from src.agent_tools.session_state.file_snapshot import FileSnapshotStore
from src.agent_tools.session_state.transaction import Transaction

__all__ = ["SessionManager", "FileSnapshotStore", "Transaction"]
