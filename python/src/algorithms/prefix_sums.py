'''
Prefix are good for
'''
def generalIdea(nums: list[int]) -> list[int]:
    prefixSums = []
    for i in range(len(nums)):
        if i == 0:
            prefixSums.append(nums[i])
        else:
            prefixSums.append(nums[i] + prefixSums[i-1])
    return prefixSums

print(generalIdea([10, 20, 10, 5, 15]))
