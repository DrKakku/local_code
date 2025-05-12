from typing import List, Any

# ==== TEMPLATE PROBLEM ====
# 1) Update `title` and `description` below.
# 2) Implement `user_solution` and, optionally, `reference_solution`.
# 3) Define test cases in the `tests` list. Each test is a dict:
#      - "input": a tuple of arguments to pass to your functions
#      - "output": the expected output (optional; if omitted or None, ref sol is used)


class Problem:
    title: str = "Count number of odd digits in a number"  # e.g. "Two Sum"
    description: str = """You are given an integer n. You need to return the number of odd digits present in the number.

The number will have no leading zeroes, except when the number is 0 itself."""  # e.g. "Return indices of two nums adding to target."

    @staticmethod
    def user_solution(num: int) -> int:
        odd = 0
        while num > 0:
            if (num % 10) % 2 != 0:
                odd += 1
            num = num // 10
        return odd

    @staticmethod
    def reference_solution(num: int) -> int:
        """
        (Optional) Correct solution used when `output` is None in a test.
        """
        raise NotImplementedError("Implement reference_solution or provide `output`")

    # TEST CASES:
    tests: List[dict] = [
        # Example:
        {"input": (1234567890,), "output": 5},
        {"input": (13579,), "output": 5},
        {"input": (24680,), "output": 0},
        {"input": (0,), "output": 0},
        # {"input": ([2,7,11,15], 9), "output": [0,1]},  # explicit expected
        # {"input": ([3,2,4], 6),   "output": None},    # will use ref sol
    ]
