"""
Trie - Word Search II (hard)

Description:
Given an m x n board of characters and a list of strings words, return all words on the board.

Each word must be constructed from letters of sequentially adjacent cells, where adjacent cells 
are horizontally or vertically neighboring. The same letter cell may not be used more than once 
in a word.

Example:
Input: board = 
[["o","a","a","n"],
["e","t","a","e"],
["i","h","k","r"],
["i","f","l","v"]], 
words = ["oath","pea","eat","rain"]

Output: ["eat","oath"]

LeetCode: https://leetcode-cn.com/problems/word-search-ii/
"""


def word_search(board: list, words: list) -> list:
    """ DFS (Backtracking) + Trie

    First, we can build a trie for the given words, to be used for the following matching process. 
    Second, For each cell, if there are words in the trie start with the char in the cell, then 
    we can start to backtracking.
    In the backtracking function, we explore the neighbouring cells for next backtracking recursion. 
    We use the trie to check if the characters traversed so far is matching with any words in the 
    given list or not.

    Time Complexity - Upper bound O(M*N*4⋅3^(L−1)) - Loop through each cell on the board which is 
    O(MN), for each cell, at the beginning, we can explore 4 directions, after than, we can only 
    explore 3 directions, and L is the length of the string / word.
    Space Complexity - O(Σ) - Σ is the alphabet size, mainly for the trie.
    """
    # Edge cases for empty board or words.
    if not board or not board[0]: return []
    if not words: return []

    # The sign for end of word.
    END_OF_WORD = "#"
    # Build a trie for given words.
    trie = {}
    for word in words:
        node = trie
        for char in word:
            # Retrieve the next node, if not found, create a empty node.
            node = node.setdefault(char, {})
        # The end of a word
        node[END_OF_WORD] = END_OF_WORD

    def backtracking(i, j, cur_word, cur_trie):
        """ Backtracking to search for matching word string.

        :params i - current row number.
        :params j - current column number.
        :params cur_word - current word string.
        :params cur_trie - current trie position (dict).
        """
        # Update current word / string and current trie position.
        cur_word += board[i][j]
        cur_trie = cur_trie[board[i][j]]

        # Found a word.
        if END_OF_WORD in cur_trie:
            result.add(cur_word)
        
        # Save the current position value, and change it to a sign meaning it 
        # has been visited.
        temp, board[i][j] = board[i][j], "@"
        # Traverse the four directions.
        for di, dj in moving_directions:
            i_new, j_new = i + di, j + dj
            # Check if the new position is out of index.
            if 0 <= i_new < height and 0 <= j_new < width:
                # Check if the char on new postion has been visited and if it's in 
                # current trie.
                if board[i_new][j_new] != "@" and board[i_new][j_new] in cur_trie:
                    backtracking(i_new, j_new, cur_word, cur_trie)
        # Recover the current position.
        board[i][j] = temp

    # Four moving directions: up, right, down, left.
    moving_directions = [(-1, 0), (0, 1), (1, 0), (0, -1)]
    height, width = len(board), len(board[0])
    # Using set to record result, to avoid repeated words.
    # such as ["oa","oa","oaa"] where "oa" could present twice in the board.
    result = set()

    # Traverse each cell in the board.
    for i in range(height):
        for j in range(width):
            # Check if the first char is in the trie as a prefix, if not, skip.
            if board[i][j] in trie:
                backtracking(i, j, "", trie)

    return [word for word in result]

if __name__ == "__main__":
    board = [["o","a","a","n"],
    ["e","t","a","e"],
    ["i","h","k","r"],
    ["i","f","l","v"]]

    words = ["oath","pea","eat","rain"]
    print(word_search(board, words))

    board = [["o","a","b","n"],
    ["o","t","a","e"],
    ["a","h","k","r"],
    ["a","f","l","v"]]

    words = ["oa","oaa"]
    print(word_search(board, words))
