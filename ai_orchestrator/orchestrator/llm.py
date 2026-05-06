import logging
import os
import json
import urllib.request
import urllib.error

# Logger setup
logger = logging.getLogger(__name__)

USE_REAL_LLM = False

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

def _call_real_llm(prompt: str, context: list[dict]) -> str:
    api_key = os.environ.get("OPENAI_API_KEY")
    if not api_key:
        raise ValueError("OPENAI_API_KEY environment variable is not set.")

    context_str = "\n".join(str(item) for item in context)
    combined_prompt = f"{context_str}\n{prompt}"

    url = "https://api.openai.com/v1/chat/completions"
    headers = {
        "Authorization": f"Bearer {api_key}",
        "Content-Type": "application/json"
    }
    data = {
        "model": "gpt-4o-mini",
        "messages": [
            {"role": "system", "content": "You are a helpful assistant"},
            {"role": "user", "content": combined_prompt}
        ]
    }

    req = urllib.request.Request(
        url,
        data=json.dumps(data).encode("utf-8"),
        headers=headers,
        method="POST"
    )

    with urllib.request.urlopen(req) as response:
        response_body = response.read().decode("utf-8")
        response_data = json.loads(response_body)
        return response_data["choices"][0]["message"]["content"]

def call_llm(prompt: str, context: list[dict]) -> str:
    """
    Mock implementation of an LLM call.
    Logs the request details and returns a deterministic mock string.
    """
    logger.info("LLM is called")
    logger.info("Original prompt length: %d", len(prompt))
    logger.info("Context size: %d", len(context))

    if USE_REAL_LLM:
        logger.info("Using real LLM API")
        try:
            return _call_real_llm(prompt, context)
        except Exception as e:
            logger.error("Real API failed: %s. Falling back to mock.", e)
    else:
        logger.info("Using mock LLM")

    # Simulate prompt formatting
    _ = _format_prompt(prompt, context)

    # Shorten original prompt for the return string
    short_prompt = prompt
    if len(short_prompt) > 50:
        short_prompt = short_prompt[:50] + "..."

    return f"[LLM MOCK] prompt={short_prompt} | context_size={len(context)}"
