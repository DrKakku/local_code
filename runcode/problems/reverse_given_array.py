from typing import List, Any

# ==== DETAILED TEMPLATE ====
class Problem:
    title: str = "Reverse a given Array"

    description: str = """
You are given an array. The task is to reverse the array and print it.
"""

    # Implement your solution function below:
    @staticmethod
    def user_solution(arr:[int]) -> Any:
        """
        Example:
            def user_solution(nums: List[int], target: int) -> List[int]:
                pass
        """
        if not arr:
            return []
        return Problem.user_solution(arr[1:]) + [arr[0]]

    # Optional reference solution:
    @staticmethod
    def reference_solution(arr:[int]) -> Any:
        if not arr:
            return []
        return Problem.reference_solution(arr[1:]) + [arr[0]]

    # TEST CASES
    tests: List[dict] = [
        {"input": ([1,2,3,4,5],), "output": [5,4,3,2,1]},
        #only positive integers
        {"input": ([1,2,3,4,5,6],), "output": [6,5,4,3,2,1]},
        {"input": ([1,2,3,4,5,6,7],), "output": [7,6,5,4,3,2,1]},
        #edge cases
        {"input": ([1,2,3,4,5,6,7,8],), "output": [8,7,6,5,4,3,2,1]},
        {"input": ([1],), "output": [1]},
        {"input": ([-1,-2,-3,-4,-5],), "output": [-5,-4,-3,-2,-1]},
        {"input": ([0],), "output": [0]},
        {"input": ([-1],), "output": [-1]},
    ]