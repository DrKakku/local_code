from typing import List


# Example problem: Two Sum
class Problem:
    title = "Two Sum"
    description = "Given an array of integers, return indices of the two numbers such that they add up to a specific target."

    @staticmethod
    def user_solution(nums: List[int], target: int) -> List[int]:
        # TODO: replace with your solution
        for i in range(len(nums)):
            for j in range(i + 1, len(nums)):
                if nums[i] + nums[j] == target:
                    return [i, j]
        return []

    @staticmethod
    def reference_solution(nums: List[int], target: int) -> List[int]:
        mapping = {}
        for i, num in enumerate(nums):
            diff = target - num
            if diff in mapping:
                return [mapping[diff], i]
            mapping[num] = i
        return []

    tests = [
        {"input": ([2, 7, 11, 15], 9), "output": [0, 1]},
        {"input": ([3, 2, 4], 6), "output": [1, 2]},
        {"input": ([3, 3], 6), "output": [0, 1]},
        {"input": ([3, 3], 6), "output": [1, 1]},
    ]