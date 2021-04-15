"""
DP - Unique Paths (medium)

Decription:
A robot is located at the top-left corner of a m x n grid (marked 'Start' 
in the diagram below).

The robot can only move either down or right at any point in time. The 
robot is trying to reach the bottom-right corner of the grid (marked 
'Finish' in the diagram below).

How many possible unique paths are there?

Example:
Input: m = 3, n = 7
Output: 28

LeetCode: https://leetcode-cn.com/problems/unique-paths/
"""


def unique_paths_recursion(m: int, n:int) -> int:
    """ Naive Recursion.

    Time Complexity - O(2^(M+N)) - For the recursion, each step, we have 
    two choices.
    Space Complexity - O(M+N) - For recursion call stack.
    """
    def helper(row, col):
        # Recursion termination - out of the grid.
        if row >= m or col >= n: return 0
        # Termination - reached the end
        if (row, col) == end: return 1
        # Drill down
        return helper(row + 1, col) + helper(row, col + 1)

    end = (m-1, n-1)
    return helper(0, 0)

def unique_paths_recur_memo(m: int, n:int) -> int:
    """ Recursion wiht memorization.

    Time Complexity - O(M*N) - Reduced repeated calculations with 
    memorization.
    Space Complexity - O(M*N) - For memorization array.
    """
    def helper(row, col):
        # Recursion termination
        if row >= m or col >= n: return 0
        if (row, col) == end: return 1

        # If the result already exists, return it directly.
        if memo[row][col]: return memo[row][col]

        # Calculate a new result and return if it's not in the 
        # memorization array.
        memo[row][col] = helper(row + 1, col) + helper(row, col + 1)
        return memo[row][col]

    # Memorization array.
    memo = [[0 for _ in range(n)] for _ in range(m)]
    end = (m-1, n-1)
    return helper(0, 0)

def unique_paths_dp(m: int, n:int) -> int:
    """ Dynamic Programming.

    Time Complexity - O(M*N) - For two loops.
    Space Complexity - O(M*N) - For DP status array.
    """
    # 2D array for DP status
    dp = [[0 for _ in range(n)] for _ in range(m)]

    # Initialization for last row and last column, set them to 1.
    dp[m - 1] = [1 for _ in range(n)]
    for i in range(m):
        dp[i][n-1] = 1

    # DP process
    for row in range(m - 2, -1, -1):
        for col in range(n - 2, -1, -1):
            dp[row][col] = dp[row+1][col] + dp[row][col+1]

    return dp[0][0]

def unique_paths_math(m: int, n:int) -> int:
    """ Combination and Permutation.

    From top-left corner to the bottom-right corner, we need to move 
    m + n - 2 times, in which m -1 will be moving down and n - 1 will 
    be moving right. So the total number of unique paths is:
    C_{m+n-2}^(m-1) = (m + n - 2)! / (m - 1)!(n - 1)!

    removing (n - 1)! from numerator and denominator, which is:
    (m + n - 2)(m + n - 3) ... n / (m - 1)!

    Time Complexity - O(min⁡(m,n)) - Using the number of rows or columns 
    won't change the result, so the for loop can always be the minimum 
    of m and n.
    Space Complexity - O(1) - Constant space.
    """
    # import math
    # return math.comb(m + n - 2, n - 1)

    base = m + n - 2
    r = min(m - 1, n - 1)
    
    numerator = 1
    denominator = 1

    for i in range(r):
        # (m + n - 2)(m + n - 3) ... n
        numerator *= (base - i)
        # (m - 1)!
        denominator *= (r - i)
    
    return int(numerator / denominator)


if __name__ == "__main__":
    print(unique_paths_recursion(3, 7))
    print(unique_paths_recur_memo(3, 7))
    print(unique_paths_dp(3, 7))
    print(unique_paths_math(3, 7))
