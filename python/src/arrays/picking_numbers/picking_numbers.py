"""
Problem: Picking Numbers
Difficulty: Easy
Time Complexity: O(N log N)
Space Complexity: O(1) (depending on sort)
"""

def picking_numbers(nums: list[int]) -> int:
    nums.sort()
    max_length = 0
    current = 1
    first = nums[0]
    for i in range(1, len(nums)):
        if abs(nums[i] - first) <= 1:
            current+=1
        else:
            first = nums[i]
            max_length = max(max_length, current)
            current = 1
    max_length = max(max_length, current)
    return max_length
