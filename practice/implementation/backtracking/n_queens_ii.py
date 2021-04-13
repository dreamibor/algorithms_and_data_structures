"""
Pruning - N-Queens II (hard)

Description:
The n-queens puzzle is the problem of placing n queens on an n x n chessboard 
such that no two queens attack each other.

Given an integer n, return the number of distinct solutions to the n-queens 
puzzle.

Example:
Input: n = 4
Output: 2
Explanation: There are two distinct solutions to the 4-queens puzzle as shown.

LeetCode: https://leetcode-cn.com/problems/n-queens-ii/
"""

def solve_n_queens(n: int) -> list:
    """ Backtracking / DFS - with recurison and set.

    Using backtracking or DFS with recursion to traverse each row / recursion 
    level, the recursion terminination condition will be when we've reached 
    level n. For each row, we enumerate each column to see where shall we put 
    the queen at. 

    Using set to track whether the cell is within the previous queen's attack 
    range. There are several cases:
    1. The same columns - the same as the queen's column (col).
    2. Left diagonal - y = -x + c, x + y = c, so row + col = queen's row + col.
    3. Right diagonal - row - col = constant, the same as  queen's row - col.

    Time Complexity - O(N!) - N is the number of queens. 
    Space Complexity - O(N) - For recursion stack and three sets. The recursion 
    depth will not exceed N, since there are only N rows.
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
            if col in columns \
                or row + col in left_diagonal \
                or row - col in right_diagonal:
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

def solve_n_queens_bit(n: int) -> list:
    """ DFS + Bit Manipulation

    Using bitwise manipulation to replace set / array to track the queen's 
    attack range.

    Assuming columns, left_diagonal, right_diagonal are three integers to 
    represent the available positions for new queens, we first get the OR 
    between all of them to get all the available positions:
    ```columns | left_diagonal | right_diagonal```
    Here 0 means it's not occupied, where we can put the new queen.
    
    Then we flip the result:
    ``~(columns | left_diagonal | right_diagonal)```
    With 1 means the positions (columns) to put queens in the row now.
    
    Remove all unecessary bits before N bits with:
    ```& ((1 << n) - 1)```
    For example, if n == 4, then (1 << n) will be 16 or (10000) in binary 
    format and then we subtract it by 1, to get 15 which is (1111) and 
    meaning the four bits for the number of queens. All the bits before 
    four bits will be removed (or set to 0). If we (11110000010) & with 
    (1111), the result will be (0010), removed all the bits before 4 bits.

    Then we iterate through bits (when bits > 0), meaning there are still 
    positions to put queens.

    We get the last bit with 1 by using a & -a, or here:
    ```p = bits & - bits```
    Assuming bits is (10100), then negative bits will be (01100). Negative 
    number is represented by two's complement (neganate and then add 1). Here 
    it's (01011) + 1 = (01100).
    So  the logical AND of them will be (00100), which is the last bit with 1 
    in bits.
    This will be the position for the new queen in this row.

    Then we need to update columns, left_diagonal, right_diagonal accordingly 
    and drill down to the next level of the recursion.

    columns = columns | p, as p is the new position for the queen, and in the 
    next row, this column is still in the current queen's attack range.

    left_diagonal = (left_diagonal | p) << 1, for left diagonal, we need to 
    move the bits left by 1 bit. 

    Same to right diagonal.

    Finally, we update the bits by removing the last bit is 1 in bits (since 
    we've explored the position). 

    Time Complexity - O(N!) - N is the number of queens. 
    Space Complexity - O(N) - For the recursion stack. The recursion 
    depth will not exceed N, since there are only N rows. The space for bits 
    is O(1), so in total O(N).
    """
    def backtracking(row, columns, left_diagonal, right_diagonal):
        # Recursion termination
        if row == n: return 1

        # Process
        count = 0
        # Get available empty positions to put queens
        bits = (~(columns | left_diagonal | right_diagonal)) & ((1 << n) - 1)
        
        # Iterate through all empty positions for new queens.
        while bits:
            # Get one empty position and explore.
            p = bits & -bits
             # Drill down
            count += backtracking(row + 1, 
                        # Update columns
                        columns | p, 
                        # Update left diagonal
                        (left_diagonal | p) << 1,
                        # Update right diagonal
                        (right_diagonal | p) >> 1)
            
            # Remove the last bit with 1 (set to 0).
            bits &= bits - 1

        return count
    
    # Edge cases.
    if n < 1: return 0

    return backtracking(0, 0, 0, 0)


if __name__ == "__main__":
    print(solve_n_queens(1))
    print(solve_n_queens(4))

    print(solve_n_queens_bit(1))
    print(solve_n_queens_bit(4))