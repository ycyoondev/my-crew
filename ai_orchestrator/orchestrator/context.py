import logging

logger = logging.getLogger(__name__)

def build_context(query: str) -> list[dict]:
    """
    Builds the context for a given query.
    """
    logger.info("Building context for query: %s", query)

    context = [_create_query_context(query)]

    logger.info("Context size: %d", len(context))

    # TODO: Integrate RAG retrieval here
    # TODO: Load relevant Obsidian markdown files

    return context

def _create_query_context(query: str) -> dict:
    """
    Creates a context dictionary for a user query.
    """
    return {
        "type": "user_query",
        "value": query
    }
