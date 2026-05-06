"""
Tools package.

Defines the interface for external tools that the orchestrator can use.
"""
from abc import ABC, abstractmethod
from typing import Any, Dict


class BaseTool(ABC):
    """Abstract base class for all tools."""

    @property
    @abstractmethod
    def name(self) -> str:
        """The unique name of the tool."""
        pass

    @property
    @abstractmethod
    def description(self) -> str:
        """A description of what the tool does."""
        pass

    @abstractmethod
    def run(self, **kwargs: Any) -> Any:
        """Executes the tool."""
        pass


class DummyTool(BaseTool):
    """A dummy tool for demonstration purposes."""

    @property
    def name(self) -> str:
        return "dummy_tool"

    @property
    def description(self) -> str:
        return "A tool that does nothing."

    def run(self, **kwargs: Any) -> Any:
        return "Dummy tool result"
