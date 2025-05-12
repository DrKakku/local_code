from typing import List, Any


class Problem:
    title = "Palendrome Number"
    description = """
    Problem Statement: Given an integer N, return true if it is a palindrome else return false.

A palindrome is a number that reads the same backward as forward. For example, 121, 1331, and 4554 are palindromes because they remain the same when their digits are reversed.
    """

    @staticmethod
    def user_solution(x: int) -> Any:
        # Extract the numbers in an array
        if x < 0:
            return False
        revnum = 0
        xx = x
        while x > 0:
            revnum = revnum * 10 + x % 10
            x = x // 10
        if revnum == xx:
            return True
        return False

    @staticmethod
    def user_solution_1(x: int) -> Any:
        # Extract the numbers in an array
        if x < 0:
            return False
        num_arr = [int(i) for i in str(x)]
        for _ in range(len(num_arr)):
            if len(num_arr) <= 1:
                break
            if num_arr[0] != num_arr[-1]:
                return False
            num_arr.pop(0)
            num_arr.pop(-1)
        return True

    @staticmethod
    def reference_solution(x: int) -> Any:
        if x < 0 or (x % 10 == 0 and x != 0):
            return False
        reverted_number = 0
        while x > reverted_number:
            reverted_number = reverted_number * 10 + x % 10
            x //= 10
        return x == reverted_number or x == reverted_number // 10

    tests = [
        # Example test case:
        {"input": (121,), "output": True},
        {"input": (-121,), "output": False},
        {"input": (10,), "output": False},
        {"input": (12321,), "output": True},
        {"input": (0,), "output": True},
        # Example test case:
        # {"input": ([arg1, arg2, ...],), "output": expected_output},
    ]
