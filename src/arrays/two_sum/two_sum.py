"""
Problem: Two Sum
Difficulty: Easy
Time Complexity: O(N)
Space Complexity: O(N)
"""
from typing import List

def two_sum(nums: List[int], target: int) -> List[int]:
    hashmap = {}

    for i in range(len(nums)):
        diff = target - nums[i]
        if diff in hashmap:
            return [hashmap[diff], i]
        hashmap[nums[i]] = i
    return [-1, -1]
