import logging
import os

logger = logging.getLogger(__name__)

def _read_file(params: dict) -> str:
    path = params.get("path", "")
    if "/ai-root" not in path:
        raise Exception("Access denied")
    
    logger.info("Attempting to read file: %s", path)
    if not os.path.exists(path):
        raise Exception("File not found")
        
    file_size = os.path.getsize(path)
    logger.info("File size: %d bytes", file_size)
    
    with open(path, "r", encoding="utf-8") as f:
        return f.read()

def _execute_dummy(tool: str, params: dict) -> str:
    """
    Handles all dummy tools by returning a deterministic string.
    """
    return f"Executed {tool} with params {str(params)}"

TOOL_REGISTRY = {
    "file.read": _read_file,
    "dummy": _execute_dummy
}

def execute_step(step: dict, context: list[dict]) -> dict:
    """
    Executes a single step from the plan.
    """
    try:
        tool = step["tool"]
        params = step.get("params", {})

        logger.info("Executing tool: %s", tool)

        if tool in TOOL_REGISTRY:
            func = TOOL_REGISTRY[tool]
            if func == _execute_dummy:
                output = func(tool, params)
            else:
                output = func(params)
        else:
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
