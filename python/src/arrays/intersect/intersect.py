"""
Problem: Intersection of Two Arrays II
Difficulty: Easy
Time Complexity: O(N + M)
Space Complexity: O(min(N, M))
"""

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
