from typing import List, Any

# ==== TEMPLATE PROBLEM ====
# 1) Update `title` and `description` below.
# 2) Implement `user_solution` and, optionally, `reference_solution`.
# 3) Define test cases in the `tests` list. Each test is a dict:
#      - "input": a tuple of arguments to pass to your functions
#      - "output": the expected output (optional; if omitted or None, ref sol is used)


class Problem:
    title: str = "GCD Or HCF"  # e.g. "Two Sum"
    description: str = """You are given two integers n1 and n2. You need find the Greatest Common Divisor (GCD) of the two given numbers. Return the GCD of the two numbers.
                            The Greatest Common Divisor (GCD) of two integers is the largest positive integer that divides both of the integers."""  # e.g. "Return indices of two nums adding to target."
    tags: List[str] = ["math", "gcd", "hcf", "greatest common divisor"]
    notes: str = """The GCD of two numbers can be calculated using the Euclidean algorithm. The algorithm is based on the principle that the GCD of two numbers also divides their difference. The steps are as follows:"""

    @staticmethod
    def user_solution(n1: int, n2: int) -> Any:
        ## Using Euclidean Algorithm to find GCD
        while n1 > 0 and n2 > 0:
            n1, n2 = max(n1, n2) - min(n1, n2), min(n1, n2)

        print(n1, n2)
        return max(n1, n2)

    @staticmethod
    def reference_solution(n1: int, n2: int) -> Any:
        """
        (Optional) Correct solution used when `output` is None in a test.
        """
        while n2:
            n1, n2 = n2, n1 % n2
        return n1

    # TEST CASES:
    tests: List[dict] = [
        # Example:
        {"input": (12, 15)},
        {"input": (100, 10)},
        {"input": (7, 14)},
        {"input": (0, 5)},
        {"input": (0, 0), "output": None},  # will use ref sol
    ]
