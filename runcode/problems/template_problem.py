from typing import List, Any


# ==== TEMPLATE PROBLEM ====
# 1) Update `title` and `description` below.
# 2) Implement `user_solution` and, optionally, `reference_solution`.
# 3) Define test cases in the `tests` list. Each test is a dict:
#      - "input": a tuple of arguments to pass to your functions
#      - "output": the expected output (optional; if omitted or None, ref sol is used)


class Problem:
    title: str = "<Problem Title>"  # e.g. "Two Sum"
    description: str = (
        "<Problem Description>"  # e.g. "Return indices of two nums adding to target."
    )

    @staticmethod
    def user_solution(*args) -> Any:
        """
        Your solution here. Example:
            def user_solution(nums: List[int], target: int) -> List[int]:
                # write code
        args will match the tuple you specify in tests.
        """
        raise NotImplementedError("Implement user_solution")

    @staticmethod
    def reference_solution(*args) -> Any:
        """
        (Optional) Correct solution used when `output` is None in a test.
        """
        raise NotImplementedError("Implement reference_solution or provide `output`")

    # TEST CASES:
    tests: List[dict] = [
        # Example:
        # {"input": ([2,7,11,15], 9), "output": [0,1]},  # explicit expected
        # {"input": ([3,2,4], 6),   "output": None},    # will use ref sol
    ]
