import logging

logger = logging.getLogger(__name__)

def execute_step(step: dict, context: list[dict]) -> dict:
    """
    Executes a single step from the plan.
    """
    try:
        tool = step["tool"]
        params = step.get("params", {})

        logger.info("Executing tool: %s", tool)

        output = _execute_dummy(tool, params)
        logger.info("Execution result: %s", output)

        return {
            "tool": tool,
            "status": "success",
            "output": output
        }
    except Exception as e:
        return {
            "tool": step.get("tool", "unknown"),
            "status": "error",
            "output": str(e)
        }

def _execute_dummy(tool: str, params: dict) -> str:
    """
    Handles all dummy tools by returning a deterministic string.
    """
    return f"Executed {tool} with params {str(params)}"
