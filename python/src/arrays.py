import math
import random
from typing import List

def climbing_leaderboard(ranked: list[int], players: list[int]) -> list[int]:
    places = [1]

    for i in range(1, len(ranked)):
        if ranked[i-1] == ranked[i]:
            places.append(places[i-1])
           # places[ranked[i]] = places[ranked[i-1]]
        else:
            places.append(places[i-1]+1)
            #places[ranked[i]] = places[ranked[i-1]] + 1

    #players.sort(reverse=True)
    # place = 1
    #print(places)
    answer = []
    for player in players[::-1]:
        answer_found = False
        for i in range(len(ranked)):
            if player >= ranked[i]:
                answer.append(places[i])
                answer_found = True
                break
        if not answer_found:
            answer.append(places[len(ranked)-1]+1)

    return answer

# print(climbing_leaderboard([100, 90, 90, 80], [70, 80, 105]))
# print(climbing_leaderboard([100, 100, 50, 40, 40, 20, 10], [5, 25, 50, 120]))
# print(climbing_leaderboard([100, 90, 90, 80, 75, 60], [50, 65, 77, 90, 102]))

def image_smoother(image: list[list[int]]) -> list[list[int]]:
    answer: list[list[int]] = [[0 for _ in range(len(image[0]))] for _ in range(len(image))]

    possible_neighbors = [(-1,0), (-1,-1), (0,-1), (1,-1), (1,0), (1,1), (0, 1), (-1, 1)]
    for i in range(len(image)):
        for j in range(len(image[i])):
            total = image[i][j]
            count = 1
            for possible_neighbor in possible_neighbors:
                try:
                    one_d_index = i + possible_neighbor[0]
                    two_d_index = j + possible_neighbor[1]
                    if one_d_index < 0 or two_d_index < 0:
                        raise IndexError()
                    total += image[one_d_index][two_d_index]
                    count += 1
                except:
                    pass

            if total > 0:
                answer[i][j] = math.floor(total/count)

    return answer

# print(image_smoother([[1,1,1],[1,0,1],[1,1,1]])) # [[0,0,0],[0,0,0],[0,0,0]]
# print(image_smoother([[100,200,100],[200,50,200],[100,200,100]])) # [[137,141,137],[141,138,141],[137,141,137]]
# print(image_smoother([[100, 0, 10], [0, 0, 25], [10, 10, 10]])) # [[25, 22, 8], [20, 18, 9], [5, 9, 11]]


# Given an array of integers, find the longest subarray where the absolute difference between any two elements is less than or equal to .
# Example
# There are two subarrays meeting the criterion:  and . The maximum length subarray has  elements.

# Function Description
# Complete the pickingNumbers function in the editor below.
# pickingNumbers has the following parameter(s):
# int a[n]: an array of integers
# Returns
# int: the length of the longest subarray that meets the criterion
def picking_numbers(nums: list[int]):
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

# print(picking_numbers([4, 6, 5, 3, 3, 1])) # 3
# print(picking_numbers([1, 2, 2, 3, 1, 2])) # 5
# print(picking_numbers([66] * 100))



def hurdle_race(nums: list[int], k: int):
    potions = 0
    for n in nums:
        potions = max(n-k, potions)
    return potions

# print(hurdle_race([1,2,3,3,2], 1)) # 2
# print(hurdle_race([1, 6, 3, 5, 2], 4)) # 2


def area_line_height(heights, word):
    a_code = ord('a')
    tallest = 0
    for w in word:
        tallest = max(heights[ord(w) - a_code], tallest)
    return len(word) * tallest

def intersect(nums1: list[int], nums2: list[int]) -> list[int]:
        my_dict = {0: {}, 1: {}}
        for num1 in nums1:
            if num1 in my_dict[0]:
                my_dict[0][num1] += 1
            else:
                my_dict[0][num1] = 1
    
        for num2 in nums2:
            if num2 in my_dict[1]:
                my_dict[1][num2] += 1
            else:
                my_dict[1][num2] = 1

        iter_index = 0
        check_index = 1
        if len(my_dict[1].keys()) < len(my_dict[0].keys()):
            iter_index = 1
            check_index = 0

        answer = []
        for k in my_dict[iter_index]:
            if k in my_dict[check_index]:
                occurrences = [k] * min(my_dict[iter_index][k], my_dict[check_index][k])
                answer.extend(occurrences)
        return answer

# print(intersect(nums1 = [1,2,2,1], nums2 = [2,2])) # [2,2]
# print(intersect(nums1 = [4,9,5], nums2 = [9,4,9,8,4])) # [4,9]

def minimumOperationsToWriteY(grid: list[list[int]]):
    center = math.floor(len(grid)/2)
    y_ops_dict = {}
    non_y_ops_dict = {}
    for r in range(len(grid)):
        for c in range(len(grid[r])):
            if (r == c and c <= center) \
            or (r + c + 1 == len(grid) and c > center) \
            or c == center and r > center:
                if grid[r][c] in y_ops_dict:
                    y_ops_dict[grid[r][c]] += 1
                else:
                    y_ops_dict[grid[r][c]] = 1
            else:
                if grid[r][c] in non_y_ops_dict:
                    non_y_ops_dict[grid[r][c]] += 1
                else:
                    non_y_ops_dict[grid[r][c]] = 1

    sum_y = sum(y_ops_dict.values())
    sum_non_y = sum(non_y_ops_dict.values())
    total_min = len(grid)**2
    for i in range(3):
        total_y = 0
        if i in y_ops_dict:
            total_y = sum_y - y_ops_dict[i]
        else:
            total_y = sum_y
        for j in range(3):
            if i == j:
                continue
            total_non_y = 0
            if j in non_y_ops_dict:
                total_non_y = sum_non_y - non_y_ops_dict[j]
            else:
                total_non_y = sum_non_y
            total_min = min(total_min, total_y + total_non_y)
    return total_min

# print(minimumOperationsToWriteY([[1,2,2],[1,1,0],[0,1,0]])) # 3
# print(minimumOperationsToWriteY([[0,1,0,1,0],[2,1,0,1,2],[2,2,2,0,1],[2,2,2,2,2],[2,1,2,2,2]])) # 12
# print(minimumOperationsToWriteY([[0,2,0,1,2],[0,0,0,1,2],[2,0,2,1,0],[2,0,2,2,0],[1,2,2,0,1]])) # 13
# print(minimumOperationsToWriteY([[0,1,0],[2,1,0],[0,2,0]])) # 5
# print(minimumOperationsToWriteY([[1,1,0,1,1],[2,1,1,1,1],[1,2,0,2,1],[2,0,0,1,2],[2,0,0,1,0]])) # 14
# print(minimumOperationsToWriteY([[0,0,1],[0,0,2],[1,0,2]])) # 4


def stones(stones: list[int]) -> int:
    destroyed_indices = {i : False for i in range(len(stones))}
    last_index = len(stones) - 1
    while len(destroyed_indices.keys()) != 1:
        random_index1 = random.randint(0, last_index)
        while stones[random_index1] == 0:
            random_index1 = random.randint(0, last_index)
        random_index2 = random.randint(0, last_index)
        while random_index1 == random_index2 or stones[random_index2] == 0:
            random_index2 = random.randint(0, last_index)
        
        if stones[random_index1] == stones[random_index2]:
            # destroyed_indices[random_index1] = True
            # destroyed_indices[random_index2] = True
            del destroyed_indices[random_index1]
            del destroyed_indices[random_index2]
            stones[random_index1] = 0
            stones[random_index2] = 0
        elif stones[random_index1] > stones[random_index2]:
            stones[random_index1] = stones[random_index1] - stones[random_index2] 
            # destroyed_indices[random_index2] = True
            del destroyed_indices[random_index2]
            stones[random_index2] = 0
        else:
            # destroyed_indices[random_index1] = True
            del destroyed_indices[random_index1]
            stones[random_index1] = 0
            stones[random_index2] = stones[random_index2] - stones[random_index1]
        print(destroyed_indices)
    print(destroyed_indices)
    return stones[list(destroyed_indices.keys())[0]]

# print(stones([2,7,4,1,8,1]))


def rotate(nums: list[int], k: int) -> list[int]:
    n = len(nums)
    shifts = k % n
    rotated = [0] * n

    temp = nums[0]
    for i in range(1,n):
        index = (i + shifts) % n
        temp2 = nums[i]
        nums[index] = temp
        temp = temp2
    #     print(temp, nums[i])
    #     temp = nums[i]
    #     rotated[(i + shifts) % n] = nums[i]
    #     print(index, rotated)
    # print(rotated)
    # for i in range(n):
    #     nums[i] = rotated[i]
    return nums
# print(rotate([1,2,3,4,5,6,7], 3))

def findIndices(input: list[int], target: int) -> tuple[int, int]:
    lp = 0
    rp = lp + 1
    max_index = len(input) - 1
    nums_dict = {}
    for i in range(len(input)):
        diff = target - input[i]
        if diff in nums_dict:
            return nums_dict[diff], i
        nums_dict[input[i]] = i
    return -1, -1

# print(findIndices([2,7,9,11], 18))


class Solution1:
    def canPlaceFlowers(self, flowerbed: list[int], n: int) -> bool:
        for i in range(len(flowerbed)):
            left = flowerbed[i-1] if i -1 > -1 else 0
            right = flowerbed[i+1] if i < len(flowerbed) - 1 else 0
            if flowerbed[i] == 0 and left == 0 and right == 0:
                n -= 1
                flowerbed[i] = 1
            if n == 0:
                break
        return n == 0
    
# print(Solution1().canPlaceFlowers([0,0,1,0,0], 1))

class Solution2:
    def minAddToMakeValid(self, s: str) -> int:
        countMap = {"(": 0, ")": 0}
        for ss in s:
            if countMap["("] > 0 and ss == ")":
                countMap["("] -= 1
            elif countMap["("] <= 0 and ss == ")":
                countMap[")"] += 1
            elif ss == "(":
                countMap["("] += 1
        return countMap["("] + countMap[")"]
# print(Solution2().minAddToMakeValid("()))(("))
# print(Solution2().minAddToMakeValid("())"))

class Solution3:
    def groupThePeople(self, groupSizes: list[int]) -> list[list[int]]:
        groups = [[] for _ in range(len(groupSizes)+1)]
        filled_buckets = []
        for i in range(len(groupSizes)):
            if len(groups[groupSizes[i]]) == groupSizes[i]:
                filled_buckets.append(groups[groupSizes[i]])
                groups[groupSizes[i]] = [i]
            else:
                groups[groupSizes[i]].append(i)
        return filled_buckets + [x for x in groups if x]
    
# print(Solution3().groupThePeople([3,3,3,3,3,1,3]))
# print(Solution3().groupThePeople([1]))


def moveZerosToEnd(nums: list[int]) -> list[int]:
    # optimal in algorithms/two_pointer.py
    count = 0
    for i in range(len(nums)):
        if nums[i] != 0:
            nums[count] = nums[i]
            count +=1

    for i in range(count, len(nums)):
        nums[i] = 0
    return nums

# print(moveZero

def rotateArray(nums, k):
    # Write code here
    n = len(nums) - 1
    k = k % len(nums)

    def reverse(start, end):
        while start < end:
            nums[start], nums[end] = nums[end], nums[start]
            start += 1
            end -= 1

    reverse(0, n)
    reverse(0, k-1)
    reverse(k, n)
    return nums

# print(rotateArray([1, 2, 3, 4, 5, 6, 7], 3)) # [5, 6, 7, 1, 2, 3, 4]


def twoSum(nums: List[int], target: int) -> List[int]:
        hashmap = {}

        for i in range(len(nums)):
            diff = target - nums[i]
            if diff in hashmap:
                return [hashmap[diff], i]
            hashmap[nums[i]] = i
        return [-1, -1]

print(twoSum([2,7,11,15], target = 9)) # [0,1] or [1,0]