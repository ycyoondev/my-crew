from ai_orchestrator.orchestrator.core import run

if __name__ == "__main__":
    user_input = input("Enter query: ")
    result = run(user_input)
    print(f"Result: {result}")
