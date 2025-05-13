from typing import List, Any

# ==== TEMPLATE PROBLEM ====
class Problem:
    title: str = "{{ title }}"
    description: str = """
        {{ description }}
    """


    @staticmethod
    def user_solution(*args) -> Any:
        """
        Implement your solution here. `args` matches the tuple in tests.
        """
        raise NotImplementedError("Implement user_solution")

    @staticmethod
    def reference_solution(*args) -> Any:
        """
        (Optional) Correct reference solution used if `output` is None.
        """
        raise NotImplementedError("Implement reference_solution or specify output in tests")

    tests: List[dict] = [
{% for case in cases %}        {"input": {{ case.input }}, "output": {{ case.output }}},
{% endfor %}    ]