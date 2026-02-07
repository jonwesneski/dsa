from typing import List


def rob(nums: List[int]) -> int:
    l_sum, r_sum = 0, 0
    for i in range(0,len(nums), 2):
        l_sum += nums[i]
        if i+1 < len(nums):
            r_sum += nums[i+1]
    return max(l_sum, r_sum)

# print(rob([1,2,3,1])) # 4
# print(rob([2,7,9,3,1])) # 12
print(rob([2,1,1,2])) # 4