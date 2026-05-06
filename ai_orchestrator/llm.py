"""
LLM abstraction layer.

Defines the interfaces for interacting with Large Language Models.
"""
from abc import ABC, abstractmethod
from typing import Any, Dict, List, Optional
from dataclasses import dataclass


@dataclass
class Message:
    """Represents a message in a conversation."""
    role: str
    content: str


@dataclass
class LLMResponse:
    """Represents a standardized response from an LLM."""
    content: str
    raw_response: Any
    usage: Dict[str, int]


class LLMInterface(ABC):
    """Abstract base class for LLM providers."""

    @abstractmethod
    def generate(self, messages: List[Message], **kwargs: Any) -> LLMResponse:
        """
        Generate a response based on the provided messages.

        Args:
            messages: A list of messages representing the conversation history.
            **kwargs: Provider-specific parameters (temperature, max_tokens, etc.).

        Returns:
            An LLMResponse object containing the result.
        """
        pass


class StubLLM(LLMInterface):
    """A stub LLM for testing and development."""

    def generate(self, messages: List[Message], **kwargs: Any) -> LLMResponse:
        """Returns a fixed response for testing."""
        return LLMResponse(
            content="This is a stubbed response from the LLM.",
            raw_response={"status": "success"},
            usage={"prompt_tokens": 0, "completion_tokens": 0, "total_tokens": 0}
        )
