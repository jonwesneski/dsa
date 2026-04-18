from typing import List


class Solution:
    def findKthPositive(self, arr: List[int], k: int) -> int:
        missing_count = 0
        arr_index = 0
        num = 0
        while missing_count < k:
            num += 1
            if arr_index < len(arr):
                if num == arr[arr_index]:
                    arr_index += 1
                else:
                    missing_count += 1
            else:
                missing_count += 1
        return num

    def advantageCount(self, nums1: List[int], nums2: List[int]):# -> List[int]:
        nums1.sort(reverse=True)
        nums2_tuple = [(nums2[i], i) for i in range(len(sorted(nums2, reverse=True)))]
        answer = [0 for _ in nums1]

        for n in nums2_tuple:
            pass

# print(Solution().findKthPositive(arr = [2,3,4,7,11], k = 5))
# print(Solution().findKthPositive([1,2,3,4], k = 2))





