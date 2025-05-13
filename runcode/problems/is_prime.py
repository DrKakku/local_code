from typing import List, Any
import math
# ==== DETAILED TEMPLATE ====
class Problem:
    title: str = "CHeck if a number is prime or not"

    description: str = """
Given an integer N, check whether it is prime or not. A prime number is a number that is only divisible by 1 and itself and the total number of divisors is 2.
        Constraints:
        1 <= n <= 5000
"""

    # Implement your solution function below:
    @staticmethod
    def user_solution(x:int) -> Any:
        if x <= 1 or x> 5000:
            return False
        for i in range(1,int(math.isqrt(x))+1):
            print(x%i)
            print(i)
            print(x//i)
            if x%i == 0 and i not in {1,x} :
                print("will return false")
                return False
        return True
       

    # Optional reference solution:
    @staticmethod
    def reference_solution(x:int) -> Any:
        raise NotImplementedError

    # TEST CASES
    tests: List[dict] = [
        # Example:
        {"input": (2,), "output": True},
        {"input": (3,), "output": True},
        {"input": (4,), "output": False},
        {"input": (5,), "output": True},
        {"input": (6,), "output": False},
        {"input": (7,), "output": True},
        {"input": (8,), "output": False},
        {"input": (9,), "output": False},
        {"input": (10,), "output": False},
        {"input": (11,), "output": True},
        {"input": (12,), "output": False},
        {"input": (13,), "output": True},
        {"input": (14,), "output": False},
        {"input": (15,), "output": False},
        {"input": (16,), "output": False},
        {"input": (17,), "output": True},
        {"input": (18,), "output": False},
        {"input": (19,), "output": True},
        {"input": (20,), "output": False},
        {"input": (21,), "output": False},
        {"input": (22,), "output": False},
        {"input": (23,), "output": True},
        {"input": (24,), "output": False},
        {"input": (25,), "output": False},
        {"input": (26,), "output": False},
        {"input": (27,), "output": False},
        {"input": (28,), "output": False},
        {"input": (29,), "output": True},
        {"input": (30,), "output": False},
        #edge cases
        {"input": (1,), "output": False},
        {"input": (0,), "output": False},
        {"input": (-1,), "output": False},
        {"input": (-2,), "output": False},
        {"input": (-3,), "output": False},
        {"input": (-4,), "output": False},
        {"input": (-5,), "output": False},
        {"input": (5000,), "output": False},
    ]