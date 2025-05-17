from typing import List, Any


# ==== DETAILED TEMPLATE ====
class Problem:
    title: str = "printing numbers using recursion till n in reverse"

    description: str = """
use recursion to numbers from n to 1
no testing required here
"""
    tags: List[str] = ["recursion", "numbers", "practice"]

    # Implement your solution function below:
    @staticmethod
    def user_solution(n: int) -> Any:
        if n <= 0:
            return
        print(n)
        Problem.user_solution(n - 1)

    # Optional reference solution:
    @staticmethod
    def reference_solution(n: int) -> Any:
        if n <= 0:
            return
        print(n)
        Problem.reference_solution(n - 1)

    # TEST CASES
    tests: List[dict] = [
        {"input": (5,)},
    ]
