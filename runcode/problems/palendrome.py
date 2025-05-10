from typing import List, Any

# TEMPLATE PROBLEM
class Problem:
    title = "Palendrome Number"
    description = ""

    @staticmethod
    def user_solution(x:int) -> Any:
        if x < 0 or (x % 10 == 0 and x != 0):
            return False
        reverted_number = 0
        while x > reverted_number:
            reverted_number = reverted_number * 10 + x % 10
            x //= 10
        return x == reverted_number or x == reverted_number // 10

    @staticmethod
    def reference_solution(*args) -> Any:
        # Provide a correct reference solution here
        raise NotImplementedError("Implement reference_solution")

    tests = [
        # Example test case:
        {"input": (121,), "output": True},
        {"input": (-121,), "output": False},
        {"input": (10,), "output": False},
        {"input": (12321,), "output": True},
        {"input": (0,), "output": True},
        # Example test case:
        # {"input": ([arg1, arg2, ...],), "output": expected_output},
    ]
