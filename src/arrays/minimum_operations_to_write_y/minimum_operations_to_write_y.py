"""
Problem: Minimum Operations to Write the Letter Y on a Grid
Difficulty: Medium
Time Complexity: O(N^2)
Space Complexity: O(1) (fixed size dictionaries)
"""
import math

def minimum_operations_to_write_y(grid: list[list[int]]):
    center = math.floor(len(grid)/2)
    y_ops_dict = {}
    non_y_ops_dict = {}
    for r in range(len(grid)):
        for c in range(len(grid[r])):
            if (r == c and c <= center) \
            or (r + c + 1 == len(grid) and c > center) \
            or c == center and r > center:
                if grid[r][c] in y_ops_dict:
                    y_ops_dict[grid[r][c]] += 1
                else:
                    y_ops_dict[grid[r][c]] = 1
            else:
                if grid[r][c] in non_y_ops_dict:
                    non_y_ops_dict[grid[r][c]] += 1
                else:
                    non_y_ops_dict[grid[r][c]] = 1

    sum_y = sum(y_ops_dict.values())
    sum_non_y = sum(non_y_ops_dict.values())
    total_min = len(grid)**2
    for i in range(3):
        total_y = 0
        if i in y_ops_dict:
            total_y = sum_y - y_ops_dict[i]
        else:
            total_y = sum_y
        for j in range(3):
            if i == j:
                continue
            total_non_y = 0
            if j in non_y_ops_dict:
                total_non_y = sum_non_y - non_y_ops_dict[j]
            else:
                total_non_y = sum_non_y
            total_min = min(total_min, total_y + total_non_y)
    return total_min
