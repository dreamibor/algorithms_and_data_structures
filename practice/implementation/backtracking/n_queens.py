"""
Pruning - N-Queens (hard)

Description:
The n-queens puzzle is the problem of placing n queens on an n x n chessboard such that 
no two queens attack each other.

Given an integer n, return all distinct solutions to the n-queens puzzle.

Each solution contains a distinct board configuration of the n-queens' placement, where 
'Q' and '.' both indicate a queen and an empty space, respectively.

Rule:
A queen can be moved any number of unoccupied squares in a straight line vertically, 
horizontally, or diagonally, so wo queens can't be on the same row, column and diagonal.

Constraints: 1 <= n <= 9

Example:
Input: n = 4
Output: [[".Q..","...Q","Q...","..Q."],["..Q.","Q...","...Q",".Q.."]]
Explanation: There exist two distinct solutions to the 4-queens puzzle as shown above.

LeetCode: https://leetcode-cn.com/problems/n-queens/
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

    Time Complexity - O(N!) - N is the number of queens.
    Space Complexity - O(N) - For recursion stack, three sets and the position of each 
    queens.
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
            board = generate_board(cur_state)
            result.append(board)
            return None

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
            backtracking(row + 1, n, cur_state + [col])

            # Remove the queen after recursion.
            columns.remove(col)
            left_diagonal.remove(row + col)
            right_diagonal.remove(row - col)

    def generate_board(cur_state):
        """ Used to generate the chess board from the current status. 

        :params: cur_state - the position of queen in each row, size of n.
        """
        board = []
        for i in cur_state:
            board.append("." * i + "Q" + "." * (n - i - 1))
        return board

    # Edge cases, empty chess board.
    if n < 1: return []

    result = []
    # Using set to store previous queens's attack range.
    columns, left_diagonal, right_diagonal = set(), set(), set()

    backtracking(0, n, [])

    return result


if __name__ == "__main__":
    print(solve_n_queens(1))
    print(solve_n_queens(4))