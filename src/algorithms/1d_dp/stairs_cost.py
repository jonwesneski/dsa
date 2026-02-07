from typing import List


def minCostClimbingStairs(cost: List[int]) -> int:
    '''
    https://leetcode.com/problems/min-cost-climbing-stairs/
    
        Index:       0          1          2        3 (Finish)
                +----------+----------+----------+----------+
    Cost:     |    10    |    15    |    20    |    0     |
                +----------+----------+----------+----------+
    
    DP Array: [    25    |    15    |    20    |    0     ]
                    ^          ^          ^          |
                    |          |          |          |
                    |          |          |        [Base Case]
                    |          |          |
                    |          |          +-- 20 + min(dp[3], dp[4]*) = 20
                    |          |              (*dp[4] treated as 0 or skipped)
                    |          |
                    |          +------------- 15 + min(dp[2], dp[3])
                    |                         15 + min(20, 0) = 15
                    |
                    +------------------------ 10 + min(dp[1], dp[2])
                                            10 + min(15, 20) = 25

    then min(dp[0], dp[1]) = 15

    I can also just use 2 variables here instead of an array where the 2 variables
    are just the last two results
    '''
    one, two = cost[len(cost) - 1], 0
    for i in range(len(cost)-2, -1, -1):
        temp = one
        one = cost[i] + min(
            one,
            two
        )
        two = temp
    return min(one, two)

print(minCostClimbingStairs([0,1,1,1])) # 1
print(minCostClimbingStairs([10,15,20])) # 15
print(minCostClimbingStairs([100,10,1])) # 10
print(minCostClimbingStairs([1,100,1,1,1,100,1,1,100,1])) # 6
