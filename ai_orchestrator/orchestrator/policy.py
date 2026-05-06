import logging

logger = logging.getLogger(__name__)


def validate(step: dict) -> None:
    """
    Validates execution steps against defined security rules.
    """
    logger.info("Validating step: %s", step)

    tool = step["tool"]
    params = step.get("params", {})

    # Rule 1: File deletion is forbidden
    if tool == "file.delete":
        raise Exception("File deletion is not allowed")

    # Rule 2: Write access to protected directories
    if tool == "file.write":
        path = params.get("path", "")
        if "/user" in path or "/system" in path:
            raise Exception("Write access denied for protected directories")

    logger.info("Validation passed")
