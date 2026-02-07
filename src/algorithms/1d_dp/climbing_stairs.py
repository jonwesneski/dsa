

def climbStairs(n: int) -> int:
    '''
    https://leetcode.com/problems/climbing-stairs/description/

    Start from back and store the results at each step
    The last 2 elements will also have a base

    Index:     0      1      2      3      4      5  (Top)
            +------+------+------+------+------+------+
    Ways:   |  8   |  5   |  3   |  2   |  1   |  1   | 
            +------+------+------+------+------+------+
                ^      ^      ^      ^      ^      |
                |      |      |      |      |    [Base Case]
                |      |      |      |      +--- [Base Case]
                |      |      |      +---- (1+1) = 2
                |      |      +----------- (1+2) = 3
                |      +------------------ (2+3) = 5
                +------------------------- (3+5) = 8


    now we only really need to remember the last 2 variables, so
    that can be used instead to save space. going from o(n) to o(1) space

    '''
    one, two = 1, 1
    for _ in range(n):
        # temp = one # make temp before we update one and assign to two
        # one += two
        # two = temp
        # this works as well
        one, two = one+two, one

    return one
    
print(climbStairs(2)) # 2
print(climbStairs(3)) # 3