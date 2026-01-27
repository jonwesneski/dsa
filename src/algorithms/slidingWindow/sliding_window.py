'''
https://www.geeksforgeeks.org/dsa/window-sliding-technique/#
'''
import sys
from typing import List


# Use this pattern when dealing with problems involving contiguous subarrays or substrings.
def find_max_average(nums: list[int], k: int) -> float:
    if len(nums) == 1:
        return nums[0] / k
    
    SMALLEST_INT = -sys.maxsize - 1
    answer: int = SMALLEST_INT

    l_pointer = 0
    r_pointer = l_pointer + (k-1)
    while r_pointer < len(nums):
        sum = 0
        for i in range(l_pointer, r_pointer):
            sum += nums[i]

        if answer == SMALLEST_INT:
            answer = sum
        else:
            answer = max(answer, sum)
        l_pointer+=1
        r_pointer+=1
    return answer/k


# print(find_max_average([1,12,-5,-6,50,3], 4))
# print(find_max_average([5], 1))
# print(find_max_average([0,1,1,3,3], 4))


def findRepeatedDnaSequences(s: str) -> list[str]:
    seen = set()
    repeated = set()
    length = 10
    for r in range(length, len(s)+1):
        temp = s[r-length:r]
        if (temp in seen):
             repeated.add(temp)
        seen.add(temp)
    return list(repeated)


# print(findRepeatedDnaSequences("AAAAACCCCCAAAAACCCCCCAAAAAGGGTTT")); # ["AAAAACCCCC","CCCCCAAAAA"]
# print(findRepeatedDnaSequences("AAAAAAAAAAAAA")); # ["AAAAAAAAAA"]
# print(findRepeatedDnaSequences("AAAAAAAAAAA")); # ["AAAAAAAAAA"]


def containsNearbyDuplicate(nums: List[int], k: int) -> bool:
    '''https://leetcode.com/problems/contains-duplicate-ii/description/?envType=problem-list-v2&envId=sliding-window'''
    sett = set() # the "window"
    for r in range(len(nums)):
        # if we are greater than target, remove L from set
        if r > k:
            sett.remove(nums[r - k - 1])
        # if this is True that mean L exists in set
        if nums[r] in sett:
            return True
        sett.add(nums[r])
    return False

print(containsNearbyDuplicate([1,2,3,1], k = 3)) # True
print(containsNearbyDuplicate([1,0,1,1], k = 1)) # True
print(containsNearbyDuplicate([1,2,3,1,2,3], k = 2)) # False



def minSubArrayLen(target: int, nums: List[int]) -> int:
    answer = float('inf')
    l = 0
    # Keeping a current sum so we don't recalculate
    # in each iteration with sum(nums[l:r+1])
    current_sum = 0
    for r in range(len(nums)):
        # Keep adding the r pointer
        current_sum += nums[r]
        while current_sum >= target:
            answer = min(answer, r+1-l)
            # subract l pointer and shrink window
            current_sum -= nums[l]
            l += 1
    try:
        return int(answer)
    except:
        return 0

# print(minSubArrayLen(target = 7, nums = [2,3,1,2,4,3])) # 2
# print(minSubArrayLen(target = 4, nums = [1,4,4])) # 1
# print(minSubArrayLen(target = 11, nums = [1,1,1,1,1,1,1,1])) # 0