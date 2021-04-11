"""
Backtracking - Sudoku Solver (hard)

Description:
Determine if a 9 x 9 Sudoku board is valid. Only the filled cells need to be validated 
according to the following rules:
1. Each row must contain the digits 1-9 without repetition.
2. Each column must contain the digits 1-9 without repetition.
3. Each of the nine 3 x 3 sub-boxes of the grid must contain the digits 1-9 without 
repetition.

Note:
* A Sudoku board (partially filled) could be valid but is not necessarily solvable.
* Only the filled cells need to be validated according to the mentioned rules.

Constraints:
1. board.length == 9
2. board[i].length == 9
3. board[i][j] is a digit or '.'.

Example:
Input: board = 
[["5","3",".",".","7",".",".",".","."]
,["6",".",".","1","9","5",".",".","."]
,[".","9","8",".",".",".",".","6","."]
,["8",".",".",".","6",".",".",".","3"]
,["4",".",".","8",".","3",".",".","1"]
,["7",".",".",".","2",".",".",".","6"]
,[".","6",".",".",".",".","2","8","."]
,[".",".",".","4","1","9",".",".","5"]
,[".",".",".",".","8",".",".","7","9"]]
Output: true

LeetCode: https://leetcode-cn.com/problems/valid-sudoku/
"""
from collections import defaultdict


def valid_sudoku(board: list) -> bool:
    """ Iteration

    We can iterate through the board and see if each element follows the rules of sudoku. 
    For each row and column, we can just iterate with two loops and check if there are 
    repeated nnumbers in each column or row. For each sub-sudoku / sub-board, we can get 
    the index (0-9) of each box by using integer division with the formula:
    box_index = (row // 3) * 3 + column // 3
    
    To track the numbers in the row / column / sub-sudoku, we can use a hash map to count 
    the frequency. Here we use an array to function as hash map.

    Time Complexity - O(1) - Only iterate 81 units once.
    Space Complexity - O(1) - Constant space.
    """
    # Array / hash map to track the numbers from 1-9 for each row / column / sub-sudoku.
    # For example, rows[row_index][number_index].
    rows = [[0 for _ in range(9)] for _ in range(9)]
    columns = [[0 for _ in range(9)] for _ in range(9)]
    subsudokus = [[0 for _ in range(9)] for _ in range(9)]

    for i in range(9):
        for j in range(9):
                num = board[i][j]
                if num != ".":
                    # Get the integer number and minus one since array indices start with 0.
                    num = int(num) - 1
                    # Calculate the index of the box / sub-sudoku.
                    box_index = (i // 3 ) * 3 + j // 3

                    # Count the number in its row, column and sub-sudoku.
                    rows[i][num] += 1
                    columns[j][num] += 1
                    subsudokus[box_index][num] += 1

                    # Check if there are numbers have been used twice.
                    if rows[i][num] > 1 or columns[j][num] > 1 or subsudokus[box_index][num] > 1:
                        return False
    
    # Return True if we've checked all the values.
    return True



if __name__ == "__main__":
    board = [["5","3",".",".","7",".",".",".","."]
            ,["6",".",".","1","9","5",".",".","."]
            ,[".","9","8",".",".",".",".","6","."]
            ,["8",".",".",".","6",".",".",".","3"]
            ,["4",".",".","8",".","3",".",".","1"]
            ,["7",".",".",".","2",".",".",".","6"]
            ,[".","6",".",".",".",".","2","8","."]
            ,[".",".",".","4","1","9",".",".","5"]
            ,[".",".",".",".","8",".",".","7","9"]]
    print(valid_sudoku(board))

    board = [["8","3",".",".","7",".",".",".","."]
            ,["6",".",".","1","9","5",".",".","."]
            ,[".","9","8",".",".",".",".","6","."]
            ,["8",".",".",".","6",".",".",".","3"]
            ,["4",".",".","8",".","3",".",".","1"]
            ,["7",".",".",".","2",".",".",".","6"]
            ,[".","6",".",".",".",".","2","8","."]
            ,[".",".",".","4","1","9",".",".","5"]
            ,[".",".",".",".","8",".",".","7","9"]]
    print(valid_sudoku(board))