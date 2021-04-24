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
    pass



if __name__ == "__main__":
    matrix = [["1","0","1","0","0"], \
            ["1","0","1","1","1"], \
            ["1","1","1","1","1"], \
            ["1","0","0","1","0"]]

    print(maximal_square(matrix))

    matrix = [["0"]]
    print(maximal_square(matrix))