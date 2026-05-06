"""
AI Orchestrator package.

Provides a clean architecture implementation of an AI agent system.
"""
import logging
from typing import Any, Dict, Optional

# Setup basic logging for the package
logging.basicConfig(
    level=logging.INFO,
    format="%(asctime)s - %(name)s - %(levelname)s - %(message)s"
)
logger = logging.getLogger("ai_orchestrator")


class OrchestratorError(Exception):
    """Base exception for the AI Orchestrator."""
    pass


class LLMError(OrchestratorError):
    """Raised when an LLM operation fails."""
    pass


class ExecutionError(OrchestratorError):
    """Raised when execution of a plan fails."""
    pass
