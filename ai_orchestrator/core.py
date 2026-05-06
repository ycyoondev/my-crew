"""
Core orchestration module.

The central component that coordinates all other modules to fulfill user requests.
"""
import logging
from typing import Any, Dict, Optional

from ai_orchestrator.intent import IntentAnalyzer
from ai_orchestrator.planner import Planner
from ai_orchestrator.executor import Executor
from ai_orchestrator.policy import PolicyEngine
from ai_orchestrator.context import ContextManager
from ai_orchestrator.llm import LLMInterface, StubLLM

logger = logging.getLogger(__name__)


class AIOrchestrator:
    """
    Main orchestrator class that manages the end-to-end flow.
    """

    def __init__(
        self,
        llm: Optional[LLMInterface] = None,
        intent_analyzer: Optional[IntentAnalyzer] = None,
        planner: Optional[Planner] = None,
        executor: Optional[Executor] = None,
        policy_engine: Optional[PolicyEngine] = None,
        context_manager: Optional[ContextManager] = None,
    ) -> None:
        self.llm = llm or StubLLM()
        self.intent_analyzer = intent_analyzer or IntentAnalyzer()
        self.planner = planner or Planner()
        self.executor = executor or Executor()
        self.policy_engine = policy_engine or PolicyEngine()
        self.context_manager = context_manager or ContextManager()

    def run(self, user_input: str, session_id: str = "default") -> str:
        """
        Processes a user request through the full orchestration pipeline.

        Args:
            user_input: The raw text input from the user.
            session_id: A unique identifier for the conversation session.

        Returns:
            The final response as a string.
        """
        logger.info(f"Processing input for session {session_id}: {user_input}")

        # 1. Policy check (Input)
        is_valid, error = self.policy_engine.validate_input(user_input)
        if not is_valid:
            return f"Policy Violation: {error}"

        # 2. Get/Update Context
        context = self.context_manager.get_context(session_id)
        context.add_message("user", user_input)

        # 3. Intent Analysis
        intent = self.intent_analyzer.analyze(user_input)
        logger.info(f"Detected intent: {intent.name}")

        # 4. Planning
        # Convert context metadata for planner
        plan = self.planner.generate_plan(intent.name, context.metadata)
        logger.info(f"Generated plan with {len(plan.tasks)} tasks")

        # 5. Execution
        execution_results = self.executor.execute(plan)
        logger.info(f"Execution completed: {execution_results}")

        # 6. Final LLM Generation (using execution results and context)
        # In a real scenario, we'd format the prompt here
        response = self.llm.generate(context.messages)

        # 7. Policy check (Output)
        is_valid, error = self.policy_engine.validate_output(response.content)
        if not is_valid:
            return f"Policy Violation: {error}"

        # Update context with assistant response
        context.add_message("assistant", response.content)

        return response.content
