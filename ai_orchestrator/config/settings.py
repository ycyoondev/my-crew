"""Settings management for the AI Orchestrator."""
import os
from typing import Any, Dict


class Settings:
    """
    Settings class to handle application configuration.

    This class uses environment variables with default values to provide
    a production-ready configuration mechanism.
    """

    def __init__(self) -> None:
        self.app_name: str = os.getenv("APP_NAME", "AI Orchestrator")
        self.log_level: str = os.getenv("LOG_LEVEL", "INFO")
        self.llm_model: str = os.getenv("LLM_MODEL", "gpt-4")
        self.timeout: int = int(os.getenv("TIMEOUT", "30"))

    def to_dict(self) -> Dict[str, Any]:
        """Returns settings as a dictionary."""
        return {
            "app_name": self.app_name,
            "log_level": self.log_level,
            "llm_model": self.llm_model,
            "timeout": self.timeout,
        }


# Global settings instance
settings = Settings()
