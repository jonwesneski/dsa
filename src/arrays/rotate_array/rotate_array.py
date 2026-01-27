"""
Problem: Rotate Array
Difficulty: Medium
Time Complexity: O(N)
Space Complexity: O(1)
"""

def rotate_array(nums: list[int], k: int) -> list[int]:
    if not nums:
        return nums
    n = len(nums)
    k = k % n

    def reverse(start, end):
        while start < end:
            nums[start], nums[end] = nums[end], nums[start]
            start += 1
            end -= 1

    reverse(0, n - 1)
    reverse(0, k - 1)
    reverse(k, n - 1)
    return nums
