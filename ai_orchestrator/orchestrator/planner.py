import logging
import json
from .llm import call_llm

# Type definitions
Plan = dict
PlanStep = dict

logger = logging.getLogger(__name__)

USE_LLM_PLANNER = False

def _create_llm_plan(query: str, context: list[dict]) -> dict:
    prompt = f"""You are an AI planner.
Given a user query, generate a JSON plan.

Rules:
* Return ONLY JSON
* Format:
{{
  "steps": [
    {{"tool": "tool_name", "params": {{}}}}
  ]
}}
* Do not add explanation

User query: {query}"""

    logger.info("Using LLM planner")
    raw_response = call_llm(prompt, context)
    logger.info("Raw LLM response: %s", raw_response)

    # Attempt to extract JSON if formatted with markdown
    clean_response = raw_response.strip()
    if clean_response.startswith("```json"):
        clean_response = clean_response[7:-3].strip()
    elif clean_response.startswith("```"):
        clean_response = clean_response[3:-3].strip()

    return json.loads(clean_response)

def create_plan(query: str, context: list[dict]) -> Plan:
    """
    Creates a simple execution plan based on the user query and context.
    """
    logger.info("Planner called with query: %s", query)

    if USE_LLM_PLANNER:
        try:
            plan = _create_llm_plan(query, context)
            steps = plan.get("steps", [])
            logger.info("Generated %d steps from LLM", len(steps))
            return {"steps": steps}
        except Exception as e:
            logger.error("LLM Planner failed: %s. Falling back to dummy steps.", e)

    steps = _build_dummy_steps(query)
    logger.info("Generated %d steps", len(steps))

    return {"steps": steps}


def _build_dummy_steps(query: str) -> list[PlanStep]:
    """
    Returns exactly 2 dummy steps for traceability.
    """
    return [
        {"tool": "dummy_step_1", "params": {"info": "step1", "query": query}},
        {"tool": "dummy_step_2", "params": {"info": "step2", "query": query}},
    ]
