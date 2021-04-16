"""
DP - Climbing Stairs (easy)

Description:
You are climbing a staircase. It takes n steps to reach the top.

Each time you can either climb 1 or 2 steps. In how many distinct ways can 
you climb to the top?

Example:
Input: n = 2
Output: 2
Explanation: 
There are two ways to climb to the top.
1. 1 step + 1 step
2. 2 steps

Constraints: 1 <= n <= 45

LeetCode: https://leetcode-cn.com/problems/climbing-stairs
"""


def climb_stairs_recurison(n: int) -> int:
    """ Recursion

    Time Comlexity - O(2^N) - For each step, we have two choices.
    Space Complexity - O(N) - For recursion stack.
    """
    # Recursion termination
    if n < 2:
        return 1
    
    return climb_stairs_recurison(n - 1) + climb_stairs_recurison(n - 2)

def climb_stairs_recur_memo(n: int) -> int:
    """ Recursion with Memorization

    Time Comlexity - O(N) - Recursion calculate only N times.
    Space Complexity - O(N) - For the memorization array.
    """
    def helper(n: int) -> int:
        # Recursion termination
        if n < 2: return 1

        # If the value already exist.
        if stairs[n]:
            return stairs[n]
        
        stairs[n] = helper(n - 1) + helper(n - 2)

        return stairs[n]
    
    stairs = [0] * (n + 1)
    helper(n)

    return stairs[n]

def climb_stairs_dp(n: int) -> int:
    """ Dynamic Programming

    State: The number of paths to stage n.
    Recurrence formula:
    dp[i] = dp[i-1] + dp[i-2]

    Time Comlexity - O(N) - Iterate through N once.
    Space Complexity - O(N) - For the DP state array.
    """
    # DP state array
    dp = [0] * n
    # Initilization
    dp[0], dp[1] = 1, 2

    # DP
    for i in range(2, n):
        dp[i] = dp[i-1] + dp[i-2]

    return dp[n-1]

def climb_stairs_dp_opt(n: int) -> int:
    """ DP with Optimised Space.

    Since the current state only depends on the previous state
    and the state two steps before, so we only need to use two 
    variables to track the previous two states.

    Time Comlexity - O(N) - Iterate through N once.
    Space Complexity - O(1) - Constant space.
    """
    # # Edge cases
    # if n <= 2: return n

    # a, b = 1, 2
    # for i in range(2, n):
    #     a, b = b, a + b
    
    # return b
    a, b = 1, 1
    
    for _ in range(1, n):
        a, b = b, a + b
    
    return b

def climb_stairs_matrix_power(n: int) -> int:
    """ Matrix Power

    |  F_n  | = | 1 1 | * | F_n-1 | 
    | F_n-1 |   | 1 0 |   | F_n-2 |   

    Time Comlexity - O(logN) - Iterate through N once.
    Space Complexity - O(1) - Constant space.
    """
    import numpy as np

    m = np.array([[1, 1],[1, 0]])
    res = np.linalg.matrix_power(m, n - 1)
    # Return the matrix result
    # | a b | * | 1 | = | a + b |
    # | c d |   | 1 |   | c + d |
    # F(n) = a + b = res[0][0] + res[0][1]
    return res[0][0] + res[0][1]

if __name__ == "__main__":
    print(climb_stairs_recurison(3))
    print(climb_stairs_recurison(10))

    print(climb_stairs_recur_memo(3))
    print(climb_stairs_recur_memo(10))

    print(climb_stairs_dp(3))
    print(climb_stairs_dp(10))

    print(climb_stairs_dp_opt(3))
    print(climb_stairs_dp_opt(10))
    
    print(climb_stairs_matrix_power(3))
    print(climb_stairs_matrix_power(10))