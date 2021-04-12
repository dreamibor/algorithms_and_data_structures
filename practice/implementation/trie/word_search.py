"""
Trie - Word Search (medium)

Description:
Given an m x n grid of characters board and a string word, return true if word exists in the 
grid.

The word can be constructed from letters of sequentially adjacent cells, where adjacent cells 
are horizontally or vertically neighboring. The same letter cell may not be used more than 
once.

Example:
Input: board = [["A","B","C","E"],
                ["S","F","C","S"],
                ["A","D","E","E"]], 
word = "ABCCED"

Output: True

LeetCode: https://leetcode-cn.com/problems/word-search/
"""

def word_search(board: list, word: str) -> bool:
    """ DFS

    We can use a function called check(i, j, k) to check whether we can find the word[k:] from
    the grid position (i, j), word[k:] means the sub-string of word from the k_th character. If 
    we can find the string, then return True, otherwise return False. 

    The steps for the function check(i, j, k):
    * If board[i][j] != word[k], then the current character doesn't match, return False.
    * If we've reached the end of the string and the character still matches, then return True.
    * Otherwise, traverse the neighbouring positions, if we can find sub-string word[k+1:] from 
    a neighbouring position, then return True, otherwise False.

    We use this function to check each (i,j) combination and as long as there is one position 
    can return True, that means we have found the word.

    To avoid traversing the same location, we can use a array / set called visited which is the 
    same size as board, to mark whether a position has been visited or not.

    Time Complexity - Loose upper bound O(M*N*3^L) - where M and N are the height and width of 
    the board, L is the length of the word. Apart from the first time we can enter four 
    directions, we can only check three directions, and since the length of the word is L, we 
    can say that the time compplexity for the backtracing function is 3^L. We've done the 
    backtracking for each cell in the baord, so in total O(M*N*3^L). However, due to pruning, 
    we can stop early when it doesn't match, so the actual time complexity shall be less than 
    the upper bound O(M*N*3^L).
    Space Complexity - O(MN) - For the extra space for visited. For the recursion stack, the 
    maximum of recursion depth will be O(min(L, MN)). 
    """
    # Four moving directions, right, left, down and up.
    directions = [(0, 1), (0, -1), (1, 0), (-1, 0)]

    def check(i, j, k) -> bool:
        # Recursison termination
        if board[i][j] != word[k]:
            return False
        if k == len(word) - 1:
            return True 
        
        # Mark the current position as visited.
        visited.add((i,j))
        result = False

        # Explore four directions.
        for di, dj in directions:
            i_new, j_new = i + di, j + dj
            # Check if the new i and j are in the board's height and width index range.
            if 0 <= i_new < height and 0 <= j_new < width:
                # Check if the position has been visited or not.
                if (i_new, j_new) not in visited:
                    # We've find a position contain the string, break the for loop.
                    if check(i_new, j_new, k + 1):
                        result = True
                        break
        # Mark the current position as not visited.
        visited.remove((i, j))
        return result

    # A set for tracking visited positions.
    visited = set()
    # Board height and width used to loop through the board.
    height, width = len(board), len(board[0])

    # Traverse each cell in the board.
    for i in range(height):
        for j in range(width):
            # If we can find a matched string, return.
            if check(i, j, 0):
                return True
    
    # If we can't find the string, reurn False.
    return False


if __name__ == "__main__":
    board = [["A","B","C","E"],
            ["S","F","C","S"],
            ["A","D","E","E"]]
    word = "ABCCED"
    print(word_search(board, word))

    board = [["A","B","C","E"],
             ["S","F","C","S"],
             ["A","D","E","E"]]
    word = "SEE"
    print(word_search(board, word))




