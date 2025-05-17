from typing import List, Any
from functools import reduce
# ==== DETAILED TEMPLATE ====
class Problem:
    title: str = "Factorial for a number N"

    description: str = """
Given a number X,  print its factorial.
To obtain the factorial of a number, it has to be multiplied by all the whole numbers preceding it. More precisely X! = X*(X-1)*(X-2) … 1.
Note: X  is always a positive number.
"""

    # Implement your solution function below:
    @staticmethod
    def user_solution(n:int) -> Any:
        """
        Example:
            def user_solution(nums: List[int], target: int) -> List[int]:
                pass
        """
        if n <= 0 or n>=100:
            return 1
        
        return Problem.user_solution(n-1)*n
    
    
    @staticmethod
    def solution_2(n:int) -> Any:
        """
        uses iteration over a range to get the factorial
        """
        
        if n >= 100 or n <= 0:
            return 1
        return reduce(lambda x,y:x*y,[i for i in range(1,n+1)])


    # Optional reference solution:
    @staticmethod
    def reference_solution(*args) -> Any:
        raise NotImplementedError

    # TEST CASES
    tests: List[dict] = [
        {"input": (5,), "output": 120},
        {"input": (3,), "output": 6},
        {"input": (1,), "output": 1},
        {"input": (0,), "output": 1},
        {"input": (10,), "output": 3628800},
        # edge cases
        {"input": (100,), "output": 1},
        {"input": (1000,), "output": 1},
        {"input": (10000,), "output": 1},
        {"input": (100000,), "output": 1},

    ]