from typing import List, Any

# ==== TEMPLATE PROBLEM ====
# 1) Update `title` and `description` below.
# 2) Implement `user_solution` and, optionally, `reference_solution`.
# 3) Define test cases in the `tests` list. Each test is a dict:
#      - "input": a tuple of arguments to pass to your functions
#      - "output": the expected output (optional; if omitted or None, ref sol is used)


class Problem:
    title: str = "Extract Digits from a Given Number"
    description: str = (
        "Given a positive integer N, return the digits of N as a list of integers. "
        "For example, if N = 1234, return [1, 2, 3, 4]."
    )

    @staticmethod
    def user_solution(n: int) -> List[int]:
        if n == 0:
            return [0]
        get_last_digit = lambda x: x % 10
        remove_last_digit = lambda x: x // 10
        output = []
        while n:
            output.append(get_last_digit(n))
            n = remove_last_digit(n)
        return output[::-1]

    @staticmethod
    def reference_solution(n: int) -> List[int]:
        result = []
        while n > 0:
            result.append(n % 10)
            n = n // 10
        return result[::-1]

    # TEST CASES:
    tests: List[dict] = [
        {"input": (1234,), "output": [1, 2, 3, 4]},
        {"input": (0,), "output": [0]},
        {"input": (7,), "output": [7]},
        {"input": (1001,), "output": [1, 0, 0, 1]},
        {"input": (9876543210,), "output": [9, 8, 7, 6, 5, 4, 3, 2, 1, 0]},
        {"input": (42,), "output": [4, 2]},
        {"input": (99999,), "output": [9, 9, 9, 9, 9]},
    ]
