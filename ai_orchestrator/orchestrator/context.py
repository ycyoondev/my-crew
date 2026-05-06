import logging
import os

logger = logging.getLogger(__name__)

BASE_DIR = "./ai-root"

def _load_markdown_files() -> list[dict]:
    files_loaded = []
    
    if not os.path.exists(BASE_DIR):
        return files_loaded

    for root, _, files in os.walk(BASE_DIR):
        for file in files:
            if file.endswith(".md"):
                if len(files_loaded) >= 5:
                    break
                    
                file_path = os.path.join(root, file)
                try:
                    with open(file_path, "r", encoding="utf-8") as f:
                        content = f.read(500)
                        
                    files_loaded.append({
                        "type": "file",
                        "path": file_path,
                        "content": content
                    })
                    logger.info("Loaded markdown file: %s", file_path)
                except Exception as e:
                    logger.warning("Failed to read file %s: %s", file_path, e)
        
        if len(files_loaded) >= 5:
            break

    logger.info("Total markdown files loaded: %d", len(files_loaded))
    return files_loaded

def build_context(query: str) -> list[dict]:
    """
    Builds the context for a given query.
    """
    logger.info("Building context for query: %s", query)

    context = [_create_query_context(query)]

    md_files = _load_markdown_files()
    context.extend(md_files)

    logger.info("Context size: %d", len(context))

    # TODO: Integrate RAG retrieval here

    return context

def _create_query_context(query: str) -> dict:
    """
    Creates a context dictionary for a user query.
    """
    return {
        "type": "user_query",
        "value": query
    }
