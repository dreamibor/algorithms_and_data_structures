"""
Pruning - N-Queens II (hard)

Description:
The n-queens puzzle is the problem of placing n queens on an n x n chessboard such that 
no two queens attack each other.

Given an integer n, return the number of distinct solutions to the n-queens puzzle.

Example:
Input: n = 4
Output: 2
Explanation: There are two distinct solutions to the 4-queens puzzle as shown.

LeetCode: https://leetcode-cn.com/problems/n-queens-ii/
"""

def solve_n_queens(n: int) -> list:
    """ Backtracking / DFS - with recurison and set.

    Using backtracking or DFS with recursion to traverse each row / recursion level, the 
    recursion terminination condition will be when we've reached level n. For each row, 
    we enumerate each column to see where shall we put the queen at. 

    Using set to track whether the cell is within the previous queen's attack range.
    There are several cases:
    1. The same columns - the same as the queen's column (col).
    2. Left diagonal - y = -x + c, x + y = c, so row + col = queen's row + col.
    3. Right diagonal - row - col = constant, the same as  queen's row - col.

    Time Complexity - O() - 
    Space Complexity - O() - 
    """
    def backtracking(row, n, cur_state):
        """ Backtracking to find the proper positions of queens.

        :params row - current row / level.
        :params n - the size of chess board.
        :params cur_state - the position of queen in each row.
        """
        # Recursion termination.
        if row == n:
            # Append the valid board into result list.
            return 1

        count = 0
        # Enumerate all columns
        for col in range(n):
            # Check whether the current cell is in previous queens' attack range.
            if col in columns or row + col in left_diagonal or row - col in right_diagonal:
                continue
            
            # Put the queen at the cell and update the attack range.
            columns.add(col)
            left_diagonal.add(row + col)
            right_diagonal.add(row - col)

            # Recursion for next row.
            count += backtracking(row + 1, n, cur_state + [col])

            # Remove the queen after recursion.
            columns.remove(col)
            left_diagonal.remove(row + col)
            right_diagonal.remove(row - col)
        
        return count

    # Edge cases, empty chess board.
    if n < 1: return 0

    
    # Using set to store previous queens's attack range.
    columns, left_diagonal, right_diagonal = set(), set(), set()

    return backtracking(0, n, [])


if __name__ == "__main__":
    print(solve_n_queens(1))
    print(solve_n_queens(4))