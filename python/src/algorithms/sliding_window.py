'''
https://www.geeksforgeeks.org/dsa/window-sliding-technique/#
'''
import sys


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


print(find_max_average([1,12,-5,-6,50,3], 4))
print(find_max_average([5], 1))
print(find_max_average([0,1,1,3,3], 4))
