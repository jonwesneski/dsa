from collections import defaultdict
from typing import List


def threeSum(nums: list[int]) -> list[int]:
    '''
    a + b + c = 0
    ↓
    b + c = -a

    We want to sort the array so we can do a 2 pointer approach
    This allows a fixed pointer at start, and 2 pointers for the remaining subarray

    We also don't want duplicates. To handle that we need to add a check on the fixed pointer
    and while loops to check previous pointers AFTER adding a result set

    '''
    result = []
    nums.sort()
    for i in range(len(nums)):
        if nums[i] > 0:
            # since it is sorted all numbers following i will be greater than zero
            # and therefore can't have a total sum equal to 0
            break
        if i > 0 and nums[i] == nums[i - 1]:
            # already computed
            continue

        l, r = i+1, len(nums) - 1
        while l < r:
            total = nums[l] + nums[r]
            if total == -nums[i]:
                result.append([nums[l], nums[r], nums[i]])
                # There might be more pairs in the subarray so lets continue
                l += 1
                r -= 1
                # Since we don't want duplicates we need to check if the next
                # pointer matches the previous
                while l < r and nums[l] == nums[l - 1]:
                    l += 1

                while l < r and nums[r] == nums[r + 1]:
                    r -= 1
            elif total > -nums[i]:
                r -= 1
            else:
                l += 1
    return result

# print(threeSum([-1,0,1,2,-1,-4])) # [[-1, 2, -1], [0, 1, -1]]
# print(threeSum([1,2,0,1,0,0,0,0])) # [[0, 0, 0]]
# print(threeSum([0, 0, 0])) # [[0, 0, 0]]
# print(threeSum([0, 0, 0, 0])) # [[0, 0, 0]]
# print(threeSumm([0, 1, 2, 0, 1, 2]))
# print(threeSumm([0, 1, 1, 0, 1, 2, 1, 2, 0, 0, 0, 1]))

def threeSum2(nums: List[int]) -> List[List[int]]:
    '''
    Same problem but solves uses:
    - Frequency counting (hash maps)
    - Sign partitioning
    - Set-based / combinatorial reasoning
    - Algebraic reduction (a + b + c = 0 → c = -a - b)
    - “Count everything first, then enumerate value combinations instead of index positions.”

    This is a problem decomposition strategy. Any valid triplet must be one of:
    - (-, +, 0)
    - (-, -, +)
    - (+, +, -)
    - (0, 0, 0)
    '''
    neg = defaultdict(int)
    pos = defaultdict(int)
    zeros = 0
    
    # Frequency counting (hash maps)
    for x in nums:
        if x < 0:
            neg[x] += 1
        elif x > 0:
            pos[x] += 1
        else:
            zeros += 1
    
    r = []
    
    if zeros:
        for n in neg:
            if -n in pos:
                # (-, +, 0)
                r.append((0, n, -n))
    
        # (0, 0, 0)
        if zeros > 2:
            r.append((0,0,0))

    # (neg, pos), (pos, neg) -> This symmetry ensures:
    # - all sign combinations are covered
    # - no sorting needed
    for set_a, set_b in ((neg, pos), (pos, neg)):
        set_a_items = list(set_a.items())
        for i, (x, q) in enumerate(set_a_items):
            for x2, q2 in set_a_items[i:]:
                if x != x2 or (x == x2 and q > 1):
                    if -x-x2 in set_b:
                        # (−, −, +) and (+, +, −)
                        r.append((x, x2, -x-x2))

    return r


# print(threeSum2([-1,0,1,2,-1,-4])) # [[-1, 2, -1], [0, 1, -1]]
# print(threeSum2([1,2,0,1,0,0,0,0])) # [[0, 0, 0]]
# print(threeSum2([0, 0, 0])) # [[0, 0, 0]]
# print(threeSum2([0, 0, 0, 0])) # [[0, 0, 0]]
# print(threeSum2([0, 1, 2, 0, 1, 2]))
# print(threeSum2([0, 1, 1, 0, 1, 2, 1, 2, 0, 0, 0, 1]))