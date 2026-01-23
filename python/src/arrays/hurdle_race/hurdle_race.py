"""
Problem: The Hurdle Race
Difficulty: Easy
Time Complexity: O(N)
Space Complexity: O(1)
"""

def hurdle_race(nums: list[int], k: int) -> int:
    potions = 0
    for n in nums:
        potions = max(n-k, potions)
    return potions
