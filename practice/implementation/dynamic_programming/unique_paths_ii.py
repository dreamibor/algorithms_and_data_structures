"""
DP - Unique Paths II (medium)

Decription:
A robot is located at the top-left corner of a m x n grid (marked 'Start' 
in the diagram below).

The robot can only move either down or right at any point in time. The 
robot is trying to reach the bottom-right corner of the grid (marked 
'Finish' in the diagram below).

Now consider if some obstacles are added to the grids. How many unique 
paths would there be?

An obstacle and space is marked as 1 and 0 respectively in the grid.

Example:
Input: obstacleGrid = [[0,0,0],[0,1,0],[0,0,0]]
Output: 2
Explanation: There is one obstacle in the middle of the 3x3 grid above.
There are two ways to reach the bottom-right corner:
1. Right -> Right -> Down -> Down
2. Down -> Down -> Right -> Right

LeetCode: https://leetcode-cn.com/problems/unique-paths-ii
"""


def unique_paths_recursion(obstacles: list) -> int:
    """ Naive Recursion

    Time Complexity - O(2^(M+N)) - Each step we have two choices, with 
    repeated calculation.
    Space Complexity - O(M+N) - For recursion call stack.
    """
    def helper(row, col):
        # Recursion termination - out of box and is obstacle.
        if row >= rows or col >= columns or obstacles[row][col] == 1:
            return 0
        # Recursion termination - reached the end.
        if row == rows - 1 and col == columns - 1:
            return 1
        
        # Drill down
        return helper(row + 1, col) + helper(row, col + 1)

    rows, columns = len(obstacles), len(obstacles[0])
    return helper(0, 0)

def unique_paths_recur_memo(obstacles: list) -> int:
    """ Recursion with Memorization

    Time Complexity - O(M*N) - Each element is only calculated once.
    Space Complexity - O(M*N) - For memorization array.
    """
    def helper(row, col):
        # Recursion termination - out of box and is obstacle.
        if row >= rows or col >= columns or obstacles[row][col] == 1:
            return 0
        # Recursion termination - reached the end.
        if row == rows - 1 and col == columns - 1:
            return 1
        # Return directly if the value has been already calculated.
        if memo[row][col]: return memo[row][col]

        # Calculate the new value and memorize.
        memo[row][col] = helper(row + 1, col) + helper(row, col + 1)

        return memo[row][col]

    rows, columns = len(obstacles), len(obstacles[0])
    # Memorization array.
    memo = [[0 for _ in range(columns)] for _ in range(rows)]

    return helper(0, 0)

def unique_paths_dp(obstacles: list) -> int:
    """ Dynamic Programming (From top-left to bottom-right)

    State transition equations:
    if obstacles[i][j] == 0: # Not obstacle
        dp[i][j] = dp[i-1][j] + dp[i][j-1]
    else:
        dp[i][j] = 0

    Time Complexity - O(M*N) - Each element is only calculated once.
    Space Complexity - O(M*N) - For DP status array.
    """
    rows, columns = len(obstacles), len(obstacles[0])
    # State array
    dp = [[0]* columns for _ in range(rows)]

    # Initialization
    for row in range(rows):
        if obstacles[row][0] == 1:
            break
        dp[row][0] = 1
    
    for col in range(columns):
        if obstacles[0][col] == 1:
            break
        dp[0][col] = 1

    # DP - From row 1, column 1 to row n - 1, column n - 1.
    for row in range(1, rows):
        for col in range(1, columns):
            if obstacles[row][col] == 1:
                dp[row][col] = 0
            else:
                dp[row][col] = dp[row - 1][col] + dp[row][col - 1]
    
    return dp[rows - 1][columns - 1]

def unique_paths_dp_reverse(obstacles: list) -> int:
    """ Dynamic Programming (From bottom-right to top-left)

    State transition equations:
    if obstacles[i][j] == 0: # Not obstacle
        dp[i][j] = dp[i+1][j] + dp[i][j+1]
    else:
        dp[i][j] = 0

    Time Complexity - O(M*N) - Each element is only calculated once.
    Space Complexity - O(M*N) - For DP status array.
    """
    rows, columns = len(obstacles), len(obstacles[0])
    # Array for DP status
    dp = [[0 for _ in range(columns)] for _ in range(rows)]

    # Initialization
    for row in range(rows - 1, -1, -1):
        if obstacles[row][columns - 1] == 1:
            break
        dp[row][columns - 1] = 1
    
    for col in range(columns - 1, -1, -1):
        if obstacles[rows - 1][col] == 1:
            break
        dp[rows - 1][col] = 1

    # DP
    for row in range(rows - 2, -1, -1):
        for col in range(columns - 2, -1, -1):
            if obstacles[row][col] == 0:
                dp[row][col] = dp[row + 1][col] + dp[row][col + 1]
            # else:
            #     dp[row][col] = 0
            
    return dp[0][0]

def unique_paths_dp_opt(obstacles: list) -> int:
    """ Dynamic Programming (Bottom-up) with Rolling Array

    Since dp[i][j] is only related to dp[i -1][j] and dp[i][j-1], which 
    means it's only related to the last row, so we can use an rolling 
    array to optimise the space complexity to be O(N), where N is the 
    number of columns.

    So that,
    Current DP value = the left DP value (already calculated) + the value 
    at the same location for last row.

    The state transition equations:
    dp[j] = dp[j - 1] + dp[j]

    Time Complexity - O(M*N) - Each element is only calculated once.
    Space Complexity - O(M) - For the rolling DP status array.
    """
    rows, columns = len(obstacles), len(obstacles[0])
    # 1D rolling status array.
    dp = [0] * columns
    # Initialization
    dp[0] = 1 if obstacles[0][0] == 0 else 0

    # DP
    for row in range(rows):
        for col in range(columns):
            # For obstacles.
            if obstacles[row][col] == 1:
                dp[col] = 0
            # Check if col - 1 is valid and the cell is not an 
            # obstacle.
            elif obstacles[row][col] == 0 and col - 1 >= 0:
                dp[col] += dp[col -1]
            
    return dp[-1]

    
if __name__ == "__main__":
    obstacles =  [[0,0,0],[0,1,0],[0,0,0]]
    print(unique_paths_recursion(obstacles))
    print(unique_paths_recur_memo(obstacles))
    print(unique_paths_dp(obstacles))
    print(unique_paths_dp_reverse(obstacles))
    print(unique_paths_dp_opt(obstacles))
    
    obstacles = [[0,1],[0,0]]
    print(unique_paths_recursion(obstacles))
    print(unique_paths_recur_memo(obstacles))
    print(unique_paths_dp(obstacles))
    print(unique_paths_dp_reverse(obstacles))
    print(unique_paths_dp_opt(obstacles))

    # Edge case - target is obstacle.
    obstacles = [[0,0],[0,1]]
    print(unique_paths_recursion(obstacles))
    print(unique_paths_recur_memo(obstacles))
    print(unique_paths_dp(obstacles))
    print(unique_paths_dp_reverse(obstacles))
    print(unique_paths_dp_opt(obstacles))


    
    