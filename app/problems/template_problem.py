from typing import List, Any

# TEMPLATE PROBLEM
class Problem:
    title = "<Problem Title>"
    description = "<Problem Description>"

    @staticmethod
    def user_solution(*args) -> Any:
        # Write your solution logic here
        raise NotImplementedError("Implement user_solution")

    @staticmethod
    def reference_solution(*args) -> Any:
        # Provide a correct reference solution here
        raise NotImplementedError("Implement reference_solution")

    tests = [
        # Example test case:
        # {"input": ([arg1, arg2, ...],), "output": expected_output},
    ]
