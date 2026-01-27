"""
Problem: Area Line Height (Designer PDF Viewer)
Difficulty: Easy
Time Complexity: O(word_length)
Space Complexity: O(1)
"""

def area_line_height(heights: list[int], word: str) -> int:
    a_code = ord('a')
    tallest = 0
    for w in word:
        tallest = max(heights[ord(w) - a_code], tallest)
    return len(word) * tallest
