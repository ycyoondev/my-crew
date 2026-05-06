import logging

logger = logging.getLogger(__name__)

def _contains_complex_keywords(query: str) -> bool:
    """Checks if any complex keyword exists in the query (case-insensitive)."""
    keywords = ["jira", "confluence", "github", "report", "summary"]
    query_lower = query.lower()
    for keyword in keywords:
        if keyword in query_lower:
            return True
    return False

def classify_intent(query: str) -> str:
    """
    Classifies the user intent as 'simple' or 'complex'.

    TODO: Replace with LLM-based intent classification
    """
    logger.info("Input query: %s", query)

    if len(query) < 30 and not _contains_complex_keywords(query):
        intent = "simple"
    else:
        intent = "complex"

    logger.info("Detected intent: %s", intent)
    return intent
