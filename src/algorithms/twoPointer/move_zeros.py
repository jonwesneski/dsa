"""
Problem: Move Zeroes
Difficulty: Easy
Time Complexity: O(N)
Space Complexity: O(1)
"""

# Algorithm is a variant of Two-Pointer called the Partition/Overwrite method
def move_zeros(nums: list[int]) -> list[int]:
    count = 0 # l pointer
    for i in range(len(nums)): # right pointer
        if nums[i] != 0:
            nums[count] = nums[i]
            count +=1

    for i in range(count, len(nums)):
        nums[i] = 0
    return nums
