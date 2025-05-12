from typing import List, Any

# ==== DETAILED TEMPLATE ====
class Problem:
    title: str = "{{ title }}"

    description: str = """
{{ description }}
"""

    # Implement your solution function below:
    @staticmethod
    def user_solution(*args) -> Any:
        """
        Example:
            def user_solution(nums: List[int], target: int) -> List[int]:
                pass
        """
        raise NotImplementedError("Implement user_solution")

    # Optional reference solution:
    @staticmethod
    def reference_solution(*args) -> Any:
        raise NotImplementedError

    # TEST CASES
    tests: List[dict] = [
{% for case in cases %}        {"input": {{ case.input }}, "output": {{ case.output }}},
{% endfor %}    ]