def sort012(nums: list[int]) -> list[int]:
    # https://www.geeksforgeeks.org/dsa/sort-an-numsay-of-0s-1s-and-2s/
    lo = 0
    hi = len(nums) - 1
    mid = 0
    while mid <= hi:
        if nums[mid] == 0:
            nums[lo], nums[mid] = nums[mid], nums[lo]
            lo += 1
            mid += 1
        elif nums[mid] == 1:
            mid += 1
        else:
            # current is 2: swap with hi and move hi backward
            # do not increment mid, as swapped value needs
            # to be re-checked
            nums[mid], nums[hi] = nums[hi], nums[mid]
            hi -= 1
    return nums

# print(sort012([0, 1, 2, 0, 1, 2]))
# print(sort012([0, 1, 1, 0, 1, 2, 1, 2, 0, 0, 0, 1]))