"""
Entry point for the AI Orchestrator application.
"""
from ai_orchestrator.core import AIOrchestrator


def main() -> None:
    """
    Main function to demonstrate the AI Orchestrator.
    """
    # Initialize the orchestrator with default stub components
    orchestrator = AIOrchestrator()

    # Sample user input
    user_query = "Hello, what can you do?"
    print(f"User: {user_query}")

    # Process the query
    try:
        response = orchestrator.run(user_query)
        print(f"Assistant: {response}")
    except Exception as e:
        print(f"An error occurred: {e}")


if __name__ == "__main__":
    main()
