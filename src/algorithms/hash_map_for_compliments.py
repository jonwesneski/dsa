# Can be good for:
# - Two Sum type problems

def sumIsTrue(nums: list[int], target: int) -> bool:
    seen = {}
    for n in nums:
        if n in seen:
            return True
        seen[target - n] = True
    return False

# print(sumIsTrue([0, -1, 2, -3, 1], target = -2))
# print(sumIsTrue([1, -2, 1, 0, 5], target = 0))


def findIndices(input: list[int], target: int) -> tuple[int, int]:
    """
    Have a map of:
    - key="the remainder to reach the target" and
    - value="the index of the element"

    The key insight for Two Sum specifically: 
    "I don't need to search forward for pairs—I can remember
    what I've seen and check if the complement exists." 
    Once you internalize this pattern, you'll recognize it in dozens of other problems.
    """
    nums_dict = {}
    for i in range(len(input)):
        diff = target - input[i]
        if diff in nums_dict:
            # The ask is to return the 2 indices where the
            # values at those indices equals the target
            return nums_dict[diff], i
        nums_dict[input[i]] = i
    return -1, -1

# print(findIndices([2,7,9,11], 18))

