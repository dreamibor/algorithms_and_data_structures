"""
Backtracking + DP - Palindrome Partitioning (medium)

Description:
Given a string s, partition s such that every substring of the partition is 
a palindrome. Return all possible palindrome partitioning of s.

A palindrome string is a string that reads the same backward as forward.

Example:
Input: s = "aab"
Output: [["a","a","b"],["aa","b"]]

LeetCode: https://leetcode-cn.com/problems/palindrome-partitioning/
"""
from functools import lru_cache


def partition(s: str) -> list:
    """ Backtracking + DP Preprocessing

    Since we need to find all the possible solutions, so we can use 
    backtracking (or DFS) to search all split methods.

    Assuming we are at index i, so s[0...i-1] has been already split into 
    several palindromes and put into temp list ans. We need to propose the 
    right boundary j so s[i...j] is also a palindrome. 

    We can use two pointers to check whether a string is palidrome or not. 
    With dynamic programming, the state transition equation will be:
    dp[i][j] = { True (i >= j, empty string or single character)
               { dp[i+1][j-1] and (s[i] == s[j]), otherwise

    After preprocessing with DP, we can reduce the time complecity of 
    checking a palindrome to O(1). 

    Time Complexity - O(N * 2^N) - N is the length of the input string. In 
    the worst case, s contains all the same character, and for N characters, 
    there are in total 2^N ways to split the string. For each split method, 
    we need O(N) time complexity to check and put them into ans list. So, in 
    total, the time complexity is O(N * 2^N).
    Space Complexity - O(N^2) - For the DP state array, for backtracking 
    stack, it's O(N), so in total O(N^2).
    """
    n = len(s)

    # DP state array, dp[i][j] - whether s[i...j] is palindrome.
    dp = [[True] * n for _ in range(n)]

    # DP state transition
    for i in reversed(range(n)):
        for j in range(i + 1, n):
            dp[i][j] = (s[i] == s[j]) and dp[i + 1][j - 1]
        
    def dfs(i: int):
        """ Backtracking for splitting palindrome.
        params: i - the starting index of current sub-string.
        """
        # Recursion termination, when i == n.
        if i == n:
            # Get a copy of ans and add to result list.
            result.append(ans.copy())
            return

        # Propose the right boundary j.
        for j in range(i, n):
            # If s[i...j] is palindrome, then drill down.
            if dp[i][j]:
                ans.append(s[i:j+1])
                # Start from the next character after right boundary. 
                dfs(j + 1)
                # Recover the temp variable ans.
                ans.pop()
    
    result = []
    ans = []
    dfs(0)
    return result

def partition_memo(s: str) -> list:
    """ Backtracking + Memorization

    Apart from DP, we can also use memorization to accelerate checking 
    whether a string is palindrome.

    Time Complexity - O(N * 2^N) - Same as the above method.
    Space Complexity - O(N^2) - Same as the above method.
    """
    n = len(s)

    # Using @cache in Python 3.9 and onwards.
    @lru_cache(maxsize=None)
    def is_palidrome(i: int, j: int) -> bool:
        if i >= j:
            # Empty string or contains only one character.
            return True
        return is_palidrome(i + 1, j - 1) if s[i] == s[j] else False
        
    def dfs(i: int):
        """ Backtracking for splitting palindrome.
        params: i - the starting index of current sub-string.
        """
        # Recursion termination, when i == n.
        if i == n:
            # Get a copy of ans and add to result list.
            result.append(ans.copy())
            return

        # Propose the right boundary j.
        for j in range(i, n):
            # If s[i...j] is palindrome, then drill down.
            if is_palidrome(i, j):
                ans.append(s[i:j+1])
                # Start from the next character after right boundary. 
                dfs(j + 1)
                # Recover the temp variable ans.
                ans.pop()
    
    result = []
    ans = []
    dfs(0)
    return result


if __name__ == "__main__":
    s = "aab"
    print(partition(s))
    print(partition_memo(s))