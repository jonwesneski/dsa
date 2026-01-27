"""
Problem: Can Place Flowers
Difficulty: Easy
Time Complexity: O(N)
Space Complexity: O(1)
"""

def can_place_flowers(flowerbed: list[int], n: int) -> bool:
    count = 0 
    flowerbed_len = len(flowerbed)
    for i in range(flowerbed_len):
        if flowerbed[i] == 0:
            left = (i == 0) or (flowerbed[i - 1] == 0)
            right = (i == flowerbed_len - 1) or (flowerbed[i + 1] == 0)
            
            if left and right:
                flowerbed[i] = 1
                count += 1
                if count >= n:
                    return True
    return count >= n
