import math

def bucket_sort(nums: list[int]) -> list[int]:
    largest = max(nums)
    magicNumber = largest / len(nums)

    buckets = [[] for _ in range(len(nums))]

    for num in nums:
        index = math.floor(num/magicNumber)
        if index >= len(nums):
            index = len(nums) - 1
        buckets[index].append(num)

    # Now we just do a regular sort on the buckets arrays and flatten
    for bucket in buckets:
        bucket.sort()

    # Flatten
    return [item for bucket in buckets for item in bucket]

print(bucket_sort([12, 4, 11, 90, 99, 3, 40, 41]))