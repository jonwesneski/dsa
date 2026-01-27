'''
Two pointer is indexing two items at the same time but at different paces
- It works well for sorted arrays and finding something

https://www.geeksforgeeks.org/dsa/top-problems-on-two-pointers-technique-for-interviews/#
'''
import sys
from typing import List

def is_subsequence(l: str, r: str) -> bool:
    l_pointer = 0
    r_pointer = 0
    while l_pointer < len(l) and r_pointer < len(r):
        if l[l_pointer] == r[r_pointer]:
            l_pointer+=1
        r_pointer+=1
    return l_pointer == len(l)

# print(is_subsequence("abc", "ahbgdc"))
# print(is_subsequence("axc", "ahbgdc"))


def removeElement(nums: list[int], val: int) -> int:
    count = 0
    for i in range(len(nums)):
        if nums[i] == val:
            nums[i] = sys.maxsize
        else:
            count += 1
    nums.sort()
    return count

# print(removeElement([3,2,2,3], 3))
# print(removeElement([0,1,2,2,3,0,4,2], 2))

def removeDuplicates(nums: list[int]) -> int:
    count = 1
    l,r = 0, 1
    while r < len(nums):
        if nums[l] == nums[r]:
            nums[r] = sys.maxsize
        else:
            count += 1
            l=r
        r+=1
    nums.sort()
    return count

# print(removeDuplicates([1,1,2]))
# print(removeDuplicates([0,0,1,1,1,2,2,3,3,4]))

def removeDuplicatesSorted(nums: list[int]) -> int:
    if (len(nums) <= 1):
        return 1
    

    r = 1
    for i in range(r,len(nums)):
        if nums[i] != nums[i-1]:
            nums[r] = nums[i]
            r+=1

    return r

# print(removeDuplicatesSorted([2, 2, 2, 2, 2]))
# print(removeDuplicatesSorted([1,1,2]))
# print(removeDuplicatesSorted([1, 2, 2, 3, 4, 4, 4, 5, 5]))
# print(removeDuplicatesSorted([0,0,1,1,1,2,2,3,3,4]))
# print(removeDuplicatesSorted([1, 2, 3]))


def threeSum(nums: List[int]) -> List[List[int]]:
    answers = []
    nums.sort()
    for i in range(len(nums)):
        if nums[i] > 0:
            break
        elif i > 0 and nums[i] == nums[i-1]:
            # already computed
            continue
        
        l, r = i+1, len(nums)-1
        while l < r:
            sum = nums[i] + nums[l] + nums[r]
            if sum == 0:
                # found match increment both l and r
                answers.append([nums[i] , nums[l] , nums[r]])
                l+=1
                r-=1
                # if the next l is the same no need to re-compute
                while l < r and nums[l] == nums[l-1]:
                    l+=1
                # if the next r is the same no need to re-compute
                while l < r and nums[r] == nums[r+1]:
                    r-=1
            elif sum < 0:
                l+=1
            else:
                r-=1
    return answers

# print(threeSum([-1,0,1,2,-1,-4]))
# print(threeSum([0,1,1]))
# print(threeSum([0,0,0]))

def maxArea(nums: list[int]) -> int:
    l, r = 0, len(nums) -1
    answer = 0
    while l < r:
        height = min(nums[l], nums[r])
        answer = max(answer, (r-l) * height)
        if nums[l] < nums[r]:
            l+=1
        else:
            r-=1
    return answer

# print(maxArea([1,8,6,2,5,4,8,3,7]))

def moveZerosToEnd(nums: list[int]) -> list[int]:
    r_pointer = 0
    for i in range(len(nums)):
        # when if is false, that means value at r_pointer will be zero
        # and we swap the next time we reach a none zero
        if nums[i] != 0:
            nums[i], nums[r_pointer] = nums[r_pointer], nums[i]
            r_pointer +=1

    return nums

# print(moveZerosToEnd([1, 2, 0, 4, 3, 0, 5, 0]))
# print(moveZerosToEnd([10,20,30]))
# print(moveZerosToEnd([0,0]))


def reserveStringPreseveSpaceIndexes(phrase: str) -> str:
    l, r = 0, len(phrase) - 1
    phrase_list = [p for p in phrase]
    while l < r:
        if phrase[l] == ' ':
            l+= 1
            continue
        if phrase[r] == ' ':
            r-= 1
            continue
        
        phrase_list[l], phrase_list[r] = phrase_list[r], phrase_list[l]
        l+= 1
        r-= 1
        
    return ''.join(phrase_list)

# print(reserveStringPreseveSpaceIndexes('internship at geeks for geeks')) # skeegrofsk ee gtapi hsn retni
# print(reserveStringPreseveSpaceIndexes('abc de')) # edc ba
# print(reserveStringPreseveSpaceIndexes('Help others')) # sreh topleH

def pairInSortedPivoted(nums: list[int], target) -> bool:
    l, r = 0, 0
    length = len(nums)
    for i in range(length-1):
        if nums[i] > nums[i+1]:
            l = i+1
            r = i
            break

    while l!= r:
        total = nums[l] + nums[r]
        if total == target:
            return True
        if total < target:
            l = (l+1) #%length
        else:
            r = (r-1)#+length) #%length
    return False

# print(pairInSortedPivoted([11, 15, 6, 8, 9, 10], target = 16))
# print(pairInSortedPivoted([11, 11, 15, 26, 38, 9, 10], target = 35))
# print(pairInSortedPivoted([9, 10, 10, 11, 15, 26, 38], target = 45))

def closestPair(nums1: list[int], nums2: list[int], x: int) -> tuple[int, int]:
    indexes = 0,0
    nums2.sort()
    smallestDiff = float('inf')

    for i in range(len(nums1)):
        diff = x - nums1[i]

        #binary search
        l,r = 0, len(nums2) - 1
        minDiff = float('inf')
        closestIndex = -1
        while l <= r:
            mid = (l+r)//2
            remaining = abs(nums2[mid] - diff)
            if remaining < minDiff:
                minDiff = remaining
                closestIndex = mid
            
            if nums2[mid] == diff:
                closestIndex = mid
                break
            elif nums2[mid] < diff:
                l = mid + 1
            else:
                r = mid - 1

        if closestIndex != -1 and abs(diff - nums2[closestIndex]) < smallestDiff:
            smallestDiff = abs(diff - nums2[closestIndex])
            indexes = i, closestIndex


    return nums1[indexes[0]], nums2[indexes[1]]

print(closestPair([1, 4, 5, 7], [10, 20, 30, 40], x = 32)) # [1,30]
print(closestPair([1, 4, 5, 7], [10, 20, 30, 40], x = 50)) # [7,40]