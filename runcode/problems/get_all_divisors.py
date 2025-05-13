import math
from typing import List, Any


# ==== DETAILED TEMPLATE ====
class Problem:
    title: str = "Print all divisors for a given number"

    description: str = """
 Given an integer N, return all divisors of N.

A divisor of an integer N is a positive integer that divides N without leaving a remainder. 
In other words, if N is divisible by another integer without any remainder, then that integer is considered a divisor of N.

"""

    # Implement your solution function below:
    @staticmethod
    def user_solution(n: int) -> list[int]:
        """
        Example:
            def user_solution(nums: List[int], target: int) -> List[int]:
                pass
        """
        if n <= 0:
            return []
        sol = set()
        for i in range(1, int(math.isqrt(n)) + 1):
            if n % i == 0:
                sol.add(i)
                sol.add(n // i)
        return sorted(sol)

    # Optional reference solution:
    @staticmethod
    def reference_solution(n: int) -> Any:
        # optimal solution for the get all divisors problem
        sol = []
        for i in range(1, n + 1):
            if n % i == 0:
                sol.append(i)
        return sol

    # TEST CASES
    tests: List[dict] = [
        # Example:
        {"input": (12,), "output": [1, 2, 3, 4, 6, 12]},
        {"input": (15,), "output": [1, 3, 5, 15]},
        {"input": (28,), "output": [1, 2, 4, 7, 14, 28]},
        {"input": (1,), "output": [1]},
        {"input": (64,)},
        {"input": (0,), "output": []},
        {"input": (-10,), "output": []},
        {"input": (100,), "output": [1, 2, 4, 5, 10, 20, 25, 50, 100]},
        {"input": (50,), "output": [1, 2, 5, 10, 25, 50]},
        {"input": (36,), "output": [1, 2, 3, 4, 6, 9, 12, 18, 36]},
        {
            "input": (1000,),
            "output": [
                1,
                2,
                4,
                5,
                8,
                10,
                20,
                25,
                40,
                50,
                100,
                125,
                200,
                250,
                500,
                1000,
            ],
        },
        {"input": (7,), "output": [1, 7]},
        {"input": (21,), "output": [1, 3, 7, 21]},
        {"input": (30,), "output": [1, 2, 3, 5, 6, 10, 15, 30]},
        {"input": (45,), "output": [1, 3, 5, 9, 15, 45]},
    ]
