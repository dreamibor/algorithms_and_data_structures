"""
DFS/BFS - Number of Islands (medium)

Description:
Given an m x n 2d grid map of '1's (land) and '0's (water), return the 
number of islands.

An island is surrounded by water and is formed by connecting adjacent 
lands horizontally or vertically. You may assume all four edges of the 
grid are all surrounded by water.

Example:
Input: 
grid = [
  ["1","1","1","1","0"],
  ["1","1","0","1","0"],
  ["1","1","0","0","0"],
  ["0","0","0","0","0"]
]
Output: 1

LeetCode Link: https://leetcode-cn.com/problems/number-of-islands/
"""


def num_of_islands(grid: list) -> int:
    pass



if __name__ == "__main__":
    grid = [
        ["1","1","1","1","0"],
        ["1","1","0","1","0"],
        ["1","1","0","0","0"],
        ["0","0","0","0","0"]
    ]
    print(f"Number of islands: {num_of_islands}")
