"""
DP - Maximal Square

Given an m x n binary matrix filled with 0's and 1's, find the largest 
square containing only 1's and return its area.

Example:
Input: matrix = 
[["1","0","1","0","0"],
 ["1","0","1","1","1"],
 ["1","1","1","1","1"],
 ["1","0","0","1","0"]]
Output: 4

LeetCode: https://leetcode-cn.com/problems/maximal-square
"""

def maximal_square(matrix: list) -> int:
    """ Dynamic Programming

    State definition:
    dp[i][j] - the maximum side length of the square of 1s we can get with 
    (i, j) as the bottom-right corner.

    Initialization:
    When i == 0 (topmost row) or j == 0 (leftmost column), if matrix[i][j] is 
    1, then the value be 1, otherwise 0. The maximum side length could only 
    be 1 if we are at the topmost row or leftmost column.
    In short, for i == 0 or j == 0, dp value is the same as matrix value.

    DP state transition:
    1. If the matrix alue on the (i, j) position is 0, then dp[i][j] == 0.
    2. If the matrix alue on the (i, j) position is 1, then dp[i][j] is 
    determined by the up, left and up-left cell. The value will be:
    dp[i][j] = min(dp[i-1][j], dp[i][j-1], dp[i-i][j-1]) + 1

    Time Complexity - O(M*N) - Iterate throug the matrix only once.
    Space Complexity - O(M*N) - For the DP state array.
    """
    # Edge cases
    if not matrix or not matrix[0]: return 0

    m, n = len(matrix), len(matrix[0])
    # DP state array
    dp = [[0] * n for _ in range(m)]
    # Initilization
    # for i in range(m):
    #     dp[i][0] = 1 if dp[i][0] == 1 else 0
    # for j in range(n):
    #     dp[0][j] = 1 if dp[0][j] == 1 else 0

    # Record the maximum length
    max_side_len = 0

    for i in range(m):
        for j in range(n):
            # For first row and column.
            if i == 0 or j == 0:
                dp[i][j] = int(matrix[i][j])
            elif matrix[i][j] == "0":
                dp[i][j] = 0
            else:
                dp[i][j] = min(dp[i-1][j], dp[i][j-1], dp[i-1][j-1]) + 1
            
            # Update the maximum side length.
            max_side_len = max(max_side_len, dp[i][j])

    return max_side_len * max_side_len


if __name__ == "__main__":
    matrix = [["1","0","1","0","0"], \
            ["1","0","1","1","1"], \
            ["1","1","1","1","1"], \
            ["1","0","0","1","0"]]

    print(maximal_square(matrix))

    matrix = [["0"]]
    print(maximal_square(matrix))