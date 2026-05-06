import logging
from ai_orchestrator.orchestrator.context import build_context
from ai_orchestrator.orchestrator.intent import classify_intent
from ai_orchestrator.orchestrator.planner import create_plan
from ai_orchestrator.orchestrator.executor import execute_step
from ai_orchestrator.orchestrator.policy import validate
from ai_orchestrator.orchestrator.llm import call_llm

# Type definition for context
Context = list[dict]

# Logger setup
logger = logging.getLogger(__name__)

def run(user_input: str) -> str:
    """
    Main orchestration function to process user input.
    """
    try:
        # 1. Build context
        logger.info("Building context")
        context: Context = build_context(user_input)

        # 2. Classify intent
        logger.info("Classifying intent")
        intent: str = classify_intent(user_input)

        # 3. Handle simple intent
        if intent == "simple":
            logger.info("Handling simple intent")
            return call_llm(user_input, context)

        # 4. Handle complex intent
        if intent == "complex":
            logger.info("Handling complex intent")
            plan: dict = create_plan(user_input, context)

            for step in plan["steps"]:
                logger.info("Validating step")
                validate(step)

                logger.info("Executing step")
                result: dict = execute_step(step, context)

                logger.info("Appending result to context")
                context.append(result)

            logger.info("Summarizing results")
            return call_llm("Summarize the results", context)

        logger.warning("Unknown intent: %s", intent)
        return f"Error: Unknown intent {intent}"

    except Exception as e:
        logger.error("Orchestration error: %s", str(e))
        return f"Error: {str(e)}"
