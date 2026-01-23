# You are climbing a staircase. It takes n steps to reach the top.

# Each time you can either climb 1 or 2 steps. In how many distinct ways can you climb to the top?
# Example 1:

# Input: n = 2
# Output: 2
# Explanation: There are two ways to climb to the top.
# 1. 1 step + 1 step
# 2. 2 steps
# Example 2:

# Input: n = 3
# Output: 3
# Explanation: There are three ways to climb to the top.
# 1. 1 step + 1 step + 1 step
# 2. 1 step + 2 steps
# 3. 2 steps + 1 step
def stair_case(n: int) -> int:
    one = 1
    two = 1
    for i in range(n-1):
        temp = one
        one += two
        two = temp
    return one


# print(stair_case(1))
# print(stair_case(3))
# print(stair_case(4))
# print(stair_case(5))
# print(stair_case(6))


class Solution:
    def totalNumbers(self, digits: list[int]) -> int:
        max_index = len(digits) - 1
        answers = set()
        for i in range(len(digits)):
            if digits[i] % 2 != 0:
                continue

            for j in range(len(digits)):
                if j == i:
                    continue
                r_pointer = j+1
                while r_pointer <= max_index:
                    if r_pointer != i:
                        left_digit = digits[r_pointer] * 100
                        if left_digit != 0:
                            answers.add(digits[i] + (digits[j] * 10) + (digits[r_pointer] * 100))
                        left_digit = digits[j] * 100
                        if left_digit != 0:
                            answers.add(digits[i] + (digits[r_pointer] * 10) + (digits[j] * 100))
                    r_pointer+=1

        # print(answers)
        return len(answers)




# print(Solution().totalNumbers([1,2,3,4]))
# print(Solution().totalNumbers([0,2,2]))
# print(Solution().totalNumbers([6,6,6]))
# print(Solution().totalNumbers([1,3,5]))

class Solution1:
    def minSteps(self, n: int) -> int:
        ans = 0
        d = 2
        while n > 1:
            # If d is prime factor, keep dividing
            # n by d until its no longer divisible
            print('==', n, d, n%d)
            while n % d == 0:
                ans += d
                n //= d
            d += 1
        return ans
    
print(Solution1().minSteps(3))
print(Solution1().minSteps(2))
print(Solution1().minSteps(1))


def countOperations(num1: int, num2: int) -> int:
    # using Euclidean Algorithm both in recursion & iteration is better than the
    # solution I came up with
    operations = 0
    while num1 != 0 and num2 != 0:
        if num1 < num2:
            num2 = num2 - num1
        else:
            num1 = num1 - num2
        operations += 1
    return operations

print(countOperations(2, 3))
        