from typing import List, Any


# ==== DETAILED TEMPLATE ====
class Problem:
    title: str = "Sum of N numbers using Recursion"

    description: str = """
            Given a number ‘N’, find out the sum of the first N natural numbers.
        """

    tags: List[str] = ["Recursion", "Mathematics", "Multiple Solutions"]

    # Implement your solution function below:
    @staticmethod
    def user_solution(n: int) -> Any:
        """
        Example:
            def user_solution(nums: List[int], target: int) -> List[int]:
                pass
        """
        if n >= 1000 or n <= 0:
            return 0

        return Problem.user_solution(n - 1) + n

    @staticmethod
    def optimal_sol(n: int):
        return n * (n + 1) / 2

    # Optional reference solution:
    @staticmethod
    def reference_solution(n: int) -> Any:
        if n >= 1000 or n <= 0:
            return -1

        return Problem.reference_solution(n - 1) + n

    # TEST CASES
    tests: List[dict] = [
        {"input": (5,), "output": 15},
        {"input": (10,), "output": 55},
        {"input": (1,), "output": 1},
        {"input": (0,), "output": 0},
        {"input": (100,), "output": 5050},
        # edge cases
        {"input": (1000,), "output": 0},
        {"input": (10000,), "output": 0},
        {"input": (100000,), "output": 0},
        {"input": (1000000,), "output": 0},
    ]
