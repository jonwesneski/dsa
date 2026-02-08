
from typing import List


def findMin(nums: List[int]) -> int:
    '''
    https://leetcode.com/problems/find-minimum-in-rotated-sorted-array/description/
    
    using binary search, I can find out:
     - IF left < mid then those are sorted ELSE update mid and right to be inside left&mid
     - IF mid < right then those are sorted ELSE update mid and left to be inside mid&right
    '''
    result = nums[0]
    l, r = 0, len(nums) - 1
    mid = (r-l) // 2
    while l < r:
        if l == mid:
            result = nums[r] if nums[l] > nums[r] else nums[l]
            break

        if nums[l] > nums[mid]:
            r = mid
        elif nums[mid] > nums[r]:
            l = mid
        else:
            r -= 1
        mid = l + (r-l) // 2

    return result


# print(findMin([4,5,6,7,0,1,2])) # 0
# print(findMin([4])) # 4
# print(findMin([3,1,2])) # 1
# print(findMin([4,5,6,7,0,1,2])) # 0
# print(findMin([3,4,5,1,2])) # 1
# print(findMin([5,1,2,3,4])) # 1



def search(nums: List[int], target: int) -> int:
    '''
    A variant
    '''
    l, r = 0, len(nums) - 1
    while l <= r:
        mid = l + (r-l) // 2
        if nums[mid] == target:
            return mid

        if nums[mid] >= nums[l]:
            if target >= nums[l] and target < nums[mid]:
                r = mid - 1
            else:
                l = mid + 1
        else:
            if target > nums[mid] and target <= nums[r]:
                l = mid + 1
            else:
                r = mid - 1

    return -1


# print(search([3,5,6,0,1,2], target = 4)) # -1
# print(search(nums = [3,4,5,6,1,2], target = 1)) # 4
# print(search(nums = [4,5,6,7,0,1,2], target = 0)) # 4
# print(search(nums = [1], target = 1)) # 0
# print(search(nums = [1, 3], target = 1)) # 0
# print(search(nums = [1, 3], target = 0)) # -1
# print(search([3,4,5,6,7,1,2], 4)) # 1
# print(search([8,1,2,3,4,5,6,7], target=6)) # 6
# print(search([5,1,2,3,4], 1)) # 1