"""
Problem: Find Indices (Find index and value difference?)
Difficulty: Easy/Medium
Time Complexity: O(N)
Space Complexity: O(N)
"""

def find_indices(input: list[int], target: int) -> tuple[int, int]:
    # NOTE: The original code logic was `target - input[i]`. Looks like Two Sum?
    # Original function name: `findIndices`
    # Logic:
    # nums_dict = {}
    # for i in range...
    #   diff = target - input[i]
    #   if diff in nums_dict: return nums_dict[diff], i
    # This IS Two Sum. But the file `arrays.py` also has `twoSum` at the bottom.
    # I will keep this as `find_indices` or maybe `two_sum_variant`?
    # The return type is tuple.
    
    nums_dict = {}
    for i in range(len(input)):
        diff = target - input[i]
        if diff in nums_dict:
            return nums_dict[diff], i
        nums_dict[input[i]] = i
    return -1, -1
