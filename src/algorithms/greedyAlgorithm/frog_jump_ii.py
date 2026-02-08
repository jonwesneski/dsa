
from typing import List


def maxJump(stones: List[int]) -> int:
    '''
    https://leetcode.com/problems/frog-jump-ii/description/

    Stones:     [0]     [2]     [5]     [6]     [7]
                |       |       |       |       |
    Forward:    (0) ----------->(5) ----------->(7)  
                \  Jump: 5-0=5  \  Jump: 7-5=2  /
                \             / \             /
    Return:     (0)<----(2)<------------(6)<---(7)
                    2-0=2   \  6-2=4   /  7-6=1

    Why skip over by 1 stone:
     1. We can only visit each stone once. Then at the end you have
     to jump from end to beginning which will have the biggest cost
     2. We want to find the minimum cost in the path. These numbers are
     in increases order, so we know the next best thing would be to do
     the next stone
    '''
    result = stones[1] - stones[0] # This helps if we have a list of size 2
    for i in range(2, len(stones)): # We calculated 1 with 0, so start with 2
        result = max(result, stones[i] - stones[i-2]) # i-2 -> skip over
    return result

print(maxJump([0,2,5,6,7])) # 5