"""
Problem: Image Smoother
Difficulty: Easy
Time Complexity: O(R * C)
Space Complexity: O(R * C)
"""
import math

def image_smoother(image: list[list[int]]) -> list[list[int]]:
    answer: list[list[int]] = [[0 for _ in range(len(image[0]))] for _ in range(len(image))]

    possible_neighbors = [(-1,0), (-1,-1), (0,-1), (1,-1), (1,0), (1,1), (0, 1), (-1, 1)]
    for i in range(len(image)):
        for j in range(len(image[i])):
            total = image[i][j]
            count = 1
            for possible_neighbor in possible_neighbors:
                try:
                    one_d_index = i + possible_neighbor[0]
                    two_d_index = j + possible_neighbor[1]
                    if one_d_index < 0 or two_d_index < 0:
                        raise IndexError()
                    total += image[one_d_index][two_d_index]
                    count += 1
                except:
                    pass

            if total > 0:
                answer[i][j] = math.floor(total/count)

    return answer
