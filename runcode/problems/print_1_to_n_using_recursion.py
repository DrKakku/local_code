from typing import List, Any

# ==== DETAILED TEMPLATE ====
class Problem:
    title: str = "printing numbers using recursion till n"

    description: str = """
use recursion to numbers from 1 to n
no testing required here
"""
    tags: List[str] = ["recursion", "numbers","practice"]

    # Implement your solution function below:
    @staticmethod
    def user_solution(n:int) -> Any:
        if n <= 0:
            return
        Problem.user_solution(n-1)
        print(n)

        
    # Optional reference solution:
    @staticmethod
    def reference_solution(n:int) -> Any:
        if n <= 0:
            return
        Problem.reference_solution(n-1)
        print(n)
                
    # TEST CASES
    tests: List[dict] = [
        {"input": (5,)},
    ]