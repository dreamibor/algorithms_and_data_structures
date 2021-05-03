"""
DP - Minimum Path Sum (medium)

Description:
Given a m x n grid filled with non-negative numbers, find a path from 
top left to bottom right, which minimizes the sum of all numbers along 
its path.

Note: You can only move either down or right at any point in time.

Example:
Input: grid = [[1,3,1],[1,5,1],[4,2,1]]
Output: 7
Explanation: Because the path 1 → 3 → 1 → 1 → 1 minimizes the sum.

LeetCode: https://leetcode-cn.com/problems/minimum-path-sum/
"""


def min_path_sum(grid: list) -> int:
    """ Dynamic Programming

    DP State Definition:
    dp[i][j] - the minimum path sum until node grid[i][j].

    Initialization:
    For first row and column, we can only move right or down, so for each 
    node, the path sum equals to the sum of all nodes.
    for row in rows:
        dp[row][0] = sum(dp[0:row][0])
    for col in columns:
        dp[0][col] = sum(dp[0][0:col])

    DP State Transition:
    dp[i][j] = min(dp[i-1][j], dp[i][j-1]) + sum

    Time Complexity - O(M*N) - M and N are the number of rows and columns.
    Space Complexity - O(M*N) - For the DP state array.
    """
    # Edge cases
    if not grid or not grid[0]: return 0

    rows, columns = len(grid), len(grid[0])
    # DP state definition
    dp = [[0] * columns for _ in range(rows)]
    # Initialization
    for row in range(rows):
        dp[row][0] = dp[row-1][0] + grid[row][0]
    for col in range(1, columns):
        dp[0][col] = dp[0][col-1] + grid[0][col]

    # DP state transition
    for i in range(1, rows):
        for j in range(1, columns):
            dp[i][j] = min(dp[i-1][j], dp[i][j-1]) + grid[i][j]
    
    return dp[rows - 1][columns - 1]

if __name__ == "__main__":
    grid = [[1,3,1],[1,5,1],[4,2,1]]
    print(f"Minimum Path Sum: {min_path_sum(grid)}")

    grid = [[1,2,3],[4,5,6]]
    print(f"Minimum Path Sum: {min_path_sum(grid)}")