"""
DP - Count Square Submatrices with All Ones (medium)

Description:
Given a m * n matrix of ones and zeros, return how many square submatrices 
have all ones.

Example:
Input: matrix =
[
  [0,1,1,1],
  [1,1,1,1],
  [0,1,1,1]
]
Output: 15
Explanation: 
There are 10 squares of side 1.
There are 4 squares of side 2.
There is  1 square of side 3.
Total number of squares = 10 + 4 + 1 = 15.

LeetCode: https://leetcode-cn.com/problems/count-square-submatrices-with-all-ones/
"""

def count_squares(matrix: list) -> int:
    """ Dynamic Programming

    State definition:
    dp[i][j] - the number of squares that use matrix[i][j] as bottom-right 
    corner (or the maximum side length with the square using matrix[i][j] as 
    bottom-right corner). 

    Initialization:
    For the first row and first column, if the matrix value is 0, then the 
    dp value will be 0 as well, if it's 1, then dp value is 1 as well, since 
    the first row and column can only have one square with side length == 1.
    In short, for i == 0 or j == 0, dp value is the same as matrix value.

    DP State Transition:
    The current state is related to the left cell (i, j - 1), the upper cell
    (i - 1m j), and the top-left cell (i - 1, j - 1), as they could be the 
    right corner for the square with current side length - 1.
    So if matrix[i][j] == 1:
        dp[i][j] = min(dp[i][j-1], dp[i-1][j-1], dp[i-1][j-1]) + 1

    Optimization:
    Since the current DP state is only relevant to the current row and the 
    row above it, so we can simplify the DP state array.
        
    Time Complexity - O(M*N) - Iterate throug the matrix only once.
    Space Complexity - O(M*N) - For the DP state array.
    """
    # Edge cases
    if not matrix or not matrix[0]: return 0

    m, n = len(matrix), len(matrix[0])
    # DP state array
    dp = [[0] * n for _ in range(m)]
    # Initialization
    # for i in range(m):
    #     dp[i][0] = 1 if matrix[i][0] == 1 else 0
    # for j in range(n):
    #     dp[0][j] = 1 if matrix[0][j] == 1 else 0
    
    res = 0
    # DP
    for i in range(m):
        for j in range(n):
            # For first row and first column.
            if i == 0 or j == 0:
                dp[i][j] = matrix[i][j]
            elif matrix[i][j] == 0:
                dp[i][j] = 0
            else:
                dp[i][j] = min(dp[i][j-1], dp[i-1][j], dp[i-1][j-1]) + 1
            
            res += dp[i][j]

    return res


if __name__ == "__main__":
    matrix = [[0,1,1,1], \
            [1,1,1,1], \
            [0,1,1,1]]
    print(count_squares(matrix))

    matrix = [[1,0,1], \
            [1,1,0], \
            [1,1,0]]
    print(count_squares(matrix))