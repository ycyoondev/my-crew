import logging

# Type definitions
Plan = dict
PlanStep = dict

logger = logging.getLogger(__name__)


def create_plan(query: str, context: list[dict]) -> Plan:
    """
    Creates a simple execution plan based on the user query and context.
    """
    logger.info("Planner called with query: %s", query)

    # TODO: Replace with LLM-based planner (JSON output)
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
