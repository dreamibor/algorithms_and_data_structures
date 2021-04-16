"""
DP - Triangle (medium)

Description:
Given a triangle array, return the minimum path sum from top to bottom.

For each step, you may move to an adjacent number of the row below. More 
formally, if you are on index i on the current row, you may move to either 
index i or index i + 1 on the next row.

Example:
Input: triangle = [[2],[3,4],[6,5,7],[4,1,8,3]]
Output: 11
Explanation: The triangle looks like:
   2
  3 4
 6 5 7
4 1 8 3
The minimum path sum from top to bottom is 2 + 3 + 5 + 1 = 11 (underlined 
above).

Follow up: Could you do this using only O(n) extra space, where n is the 
total number of rows in the triangle?

LeetCode: https://leetcode-cn.com/problems/triangle
"""


def minimum_path_recursion(triangle: list) -> int:
   """ Recursion

   Time Complexity - O(2^(M+N)) - Each step has two choices.
   Space Complexity - O(M*N) - For recursion call stack.
   """
   def helper(i, j):
      # Recrusion terminiation
      if i >= rows - 1: return triangle[i][j]
      if j >= len(triangle[i]): return 0

      # Drill down
      left_path = helper(i+1, j) + triangle[i][j]
      right_path = helper(i+1, j+1) + triangle[i][j]

      return min(left_path, right_path) 

   rows = len(triangle)
   return helper(0, 0)

def minimum_path_dp(triangle: list) -> int:
   """ Dynamic Programming (Bottom-up)

   State: dp[i][j] - the minimum path sum of node [i,j] from 
   bottom nodes. Result will be dp[0][0].

   State transition:
   dp[i][j] = min(dp[i + 1][j], dp[i + 1][j + 1]) + triangle[i][j]

   Initial states:
   The bottom line's values as the DP's bottom line's values.

   Time Complexity - O(M*N) - M and N are the number of rows and columns.
   Space Complexity - O(M*N) - For the 2D DP state array.
   """
   # Edge cases
   if not triangle: return 0

   rows = len(triangle)
   # DP state with 1D rolling array, also initialization
   dp = triangle[rows - 1] # triangle[- 1]
   
   # DP
   for row in range(rows - 2, -1, -1):
      for col in range(len(triangle[row])):
         dp[col] = triangle[row][col] + min(dp[col], dp[col + 1]) 

   return dp[0]

if __name__ == "__main__":
   triangle = [[2],[3,4],[6,5,7],[4,1,8,3]]
   print(minimum_path_recursion(triangle))
   print(minimum_path_dp(triangle))