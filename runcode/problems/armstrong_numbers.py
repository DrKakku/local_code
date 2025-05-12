from typing import List, Any



class Problem:
    title: str = "Check if a number is Armstrong Number or not"
    description: str = (
        """Given an integer N (0 <= N <= 5000), return True if it is an Armstrong number, otherwise return False.

An Armstrong number is a number that is equal to the sum of its own digits each raised to the power of the number of digits.

For example, 153 is an Armstrong number because 1³ + 5³ + 3³ = 153."""
    )

    @staticmethod
    def user_solution(n:int) -> Any:
        """
        Your solution here.
        """
        if 0<=n<=5000:
            return False

    @staticmethod
    def reference_solution(n: int) -> bool:
        digits = list(map(int, str(n)))
        power = len(digits)
        return sum(d ** power for d in digits) == n

    # TEST CASES:
    tests: List[dict] = [
        # Known Armstrong numbers in the range 0–5000
        {"input": (0,), "output": True},
        {"input": (1,), "output": True},
        {"input": (2,), "output": True},
        {"input": (3,), "output": True},
        {"input": (4,), "output": True},
        {"input": (5,), "output": True},
        {"input": (6,), "output": True},
        {"input": (7,), "output": True},
        {"input": (8,), "output": True},
        {"input": (9,), "output": True},
        {"input": (153,), "output": True},
        {"input": (370,), "output": True},
        {"input": (371,), "output": True},
        {"input": (407,), "output": True},
        {"input": (1634,), "output": True},
        {"input": (8208,), "output": False},  # > 5000, included just to clarify the limit

        # Boundary and near-boundary non-Armstrong numbers
        {"input": (10,), "output": False},
        {"input": (99,), "output": False},
        {"input": (100,), "output": False},
        {"input": (152,), "output": False},
        {"input": (154,), "output": False},
        {"input": (369,), "output": False},
        {"input": (372,), "output": False},
        {"input": (999,), "output": False},
        {"input": (1000,), "output": False},
        {"input": (1633,), "output": False},
        {"input": (1635,), "output": False},
        {"input": (2000,), "output": False},
        {"input": (4070,), "output": False},
        {"input": (4095,), "output": False},
        {"input": (4999,), "output": False},
        {"input": (5000,), "output": False},
    ]
