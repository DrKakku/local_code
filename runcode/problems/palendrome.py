from typing import List, Any


# TEMPLATE PROBLEM
class Problem:
    title = "Palendrome Number"
    description = ""

    @staticmethod
    def user_solution(x: int) -> Any:
        if x < 0 or (x % 10 == 0 and x != 0):
            return False
        reverted_number = 0
        while x > reverted_number:
            reverted_number = reverted_number * 10 + x % 10
            x //= 10
        return x == reverted_number or x == reverted_number // 10

    @staticmethod
    def reference_solution(x: int) -> Any:
        # Provide a correct reference solution here
        if x < 0 or (x % 10 == 0 and x != 0):
            return False
        reverted_number = 0
        while x > reverted_number:
            reverted_number = reverted_number * 10 + x % 10
            x //= 10
        return x == reverted_number or x == reverted_number // 10

    tests = [
        # Example test case:
        {"input": (121,), "output": True},
        {"input": (-121,), "output": False},
        {"input": (10,), "output": False},
        {"input": (12321,), "output": True},
        {"input": (0,), "output": True},
        {"input": (1234321,), "output": None},
        {"input": (12345678987654321,), "output": True},
        {"input": (1234567898765432,), "output": False},
        {"input": (123456789876543210,), "output": False},
        {"input": (1234567898765432100,), "output": False},
        {"input": (1234567898765432101,), "output": False},
        {"input": (12345678987654321012,), "output": False},
        {"input": (12345678987654321012345678987654321,), "output": True},
        {"input": (123456789876543210123456789876543210,), "output": False},
        {"input": (1234567898765432101234567898765432101,), "output": False},
        {"input": (12345678987654321012345678987654321012,), "output": False},
        # Example test case:
        # {"input": ([arg1, arg2, ...],), "output": expected_output},
    ]
