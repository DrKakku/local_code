from typing import List, Any

# ==== DETAILED TEMPLATE ====
class Problem:
    title: str = "If the given string is Palendrome or not"

    description: str = """
A phrase is a palindrome if, after converting all uppercase letters into lowercase letters and removing all non-alphanumeric characters, it reads the same forward and backward. Alphanumeric characters include letters and numbers.
Given a string s, return true if it is a palindrome, or false otherwise.
"""

    # Implement your solution function below:
    @staticmethod
    def user_solution(s:str) -> Any:
        """
        Example:
            def user_solution(nums: List[int], target: int) -> List[int]:
                pass
        """
        clean_s = ''.join(ch for ch in s if ch.isalnum())
        clean_s = clean_s.lower()
        return Problem.rev_str(clean_s) == clean_s

    @staticmethod
    def rev_str(s:str):

        if len(s)<=0:
            return ""
        return Problem.rev_str(s[1:])+s[0]






    # Optional reference solution:
    @staticmethod
    def reference_solution(*args) -> Any:
        raise NotImplementedError

    # TEST CASES
    tests: List[dict] = [
        {"input": ("A man, a plan, a canal: Panama"), "output": True},
        {"input": ("race a car"), "output": True},
        {"input": (" "), "output": True},
    ]