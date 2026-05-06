"""
Context management module.

Handles the state and memory of the orchestration process.
"""
from dataclasses import dataclass, field
from typing import Any, Dict, List, Optional
from ai_orchestrator.llm import Message


@dataclass
class ConversationContext:
    """
    Holds the state of a single conversation session.
    """
    session_id: str
    messages: List[Message] = field(default_factory=list)
    metadata: Dict[str, Any] = field(default_factory=dict)

    def add_message(self, role: str, content: str) -> None:
        """Adds a message to the context."""
        self.messages.append(Message(role=role, content=content))

    def clear(self) -> None:
        """Clears the conversation history."""
        self.messages = []


class ContextManager:
    """
    Manages multiple conversation contexts.
    """
    def __init__(self) -> None:
        self._contexts: Dict[str, ConversationContext] = {}

    def get_context(self, session_id: str) -> ConversationContext:
        """Retrieves or creates a context for the given session ID."""
        if session_id not in self._contexts:
            self._contexts[session_id] = ConversationContext(session_id=session_id)
        return self._contexts[session_id]
