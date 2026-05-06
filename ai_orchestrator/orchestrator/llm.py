import logging

# Logger setup
logger = logging.getLogger(__name__)

# TODO: Replace with real LLM API (OpenAI, Anthropic, etc.)

def _format_prompt(prompt: str, context: list[dict]) -> str:
    """
    Simulates how prompt and context would be combined.
    Truncates the combined string if it exceeds 50 characters.
    """
    last_items = context[-3:]
    context_str = "\n".join(str(item) for item in last_items)
    combined = f"{context_str}\n{prompt}"

    if len(combined) > 50:
        return combined[:50] + "..."
    return combined

def call_llm(prompt: str, context: list[dict]) -> str:
    """
    Mock implementation of an LLM call.
    Logs the request details and returns a deterministic mock string.
    """
    logger.info("LLM is called")
    logger.info("Original prompt length: %d", len(prompt))
    logger.info("Context size: %d", len(context))

    # Simulate prompt formatting
    _ = _format_prompt(prompt, context)

    # Shorten original prompt for the return string
    short_prompt = prompt
    if len(short_prompt) > 50:
        short_prompt = short_prompt[:50] + "..."

    return f"[LLM MOCK] prompt={short_prompt} | context_size={len(context)}"
