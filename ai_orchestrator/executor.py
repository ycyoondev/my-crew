"""
Executor module.

Carries out the tasks defined in a plan.
"""
from typing import Any, List
from ai_orchestrator.planner import Plan, Task


class Executor:
    """
    Executes a sequence of tasks and aggregates results.
    """

    def execute(self, plan: Plan) -> List[Any]:
        """
        Iterates through the tasks in a plan and executes them.

        Args:
            plan: The Plan object to execute.

        Returns:
            A list of results from each task.
        """
        results = []
        for task in plan.tasks:
            results.append(self._run_task(task))
        return results

    def _run_task(self, task: Task) -> Any:
        """Executes a single task."""
        # Placeholder execution logic
        return f"Executed task {task.id}: {task.action}"
