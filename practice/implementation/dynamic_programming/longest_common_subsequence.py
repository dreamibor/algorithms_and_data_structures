"""
DP - Longest Common Subsequence, LCS (medium)

Given two strings text1 and text2, return the length of their longest 
common subsequence. If there is no common subsequence, return 0.

A subsequence of a string is a new string generated from the original 
string with some characters (can be none) deleted without changing the 
relative order of the remaining characters.

For example, "ace" is a subsequence of "abcde".

A common subsequence of two strings is a subsequence that is common to 
both strings.

Example:
Input: text1 = "abcde", text2 = "ace" 
Output: 3  
Explanation: The longest common subsequence is "ace" and its length is 3.

LeetCode: https://leetcode-cn.com/problems/longest-common-subsequence
"""


def common_subsequence_dp(text1: str, text2: str) -> int:
    """ Dynamic Programming

    DP State Definition:
    dp[i][j] - the length of the longest common subsequence between two 
    sub-strings text1[1...i] and text2[1...j].

    Index 0 represents empty string "", and we use 1 as the starting index 
    of the string, so we need to plus the length of text1 and text2 here to 
    define the DP array dp[m+1][n+1].
    
    For example, for strings "ac" and "babc", dp[2][4] means the length of 
    the LCS between them. 

    Initialization:
    Assuming n = len(text1), m = len(text2)
    When i == 0, there is no common subsequence, so:
    for i in range(n):
        dp[i][0] = 0
    Same to text2, when j == 0, there is no common subsequence as well:
    for j in range(m):
        dp[0][j] = 0

    DP State Transition:
    1. When text1[i] == text[j], then the character must be in the LCS, so 
    we only need to add the LCS length by 1:
    dp[i][j] = dp[i-1][j-1] + 1

    2. When text1[i] != text[j], we must remove at least one of the charcters
    in text1 or text2 and we shall choose the one makes longer subsequence:
    dp[i][j] = max(dp[i-1][j], dp[i][j-1])
    It means, we take maximum between the LCS of text1[1...i-1] and 
    text2[1...j] and the LCS of text1[1...i] and text2[1...j-1].

    Time Complexity - O(M*N) - Two for loops for the two strings.
    Space Complexity - O(M*N) - For the DP state array.
    """
    # Edge cases
    if not text1 or not text2: return 0

    m, n = len(text1), len(text2)
    # DP state definition
    dp = [[0] * (n + 1) for _ in range(m + 1)]
    # Initialization
    # for i in range(m):
    #     dp[i][0] = 0
    # for j in range(n):
    #     dp[0][j] = 0
    
    # DP state transition
    for i in range(1, m + 1):
        for j in range(1, n + 1):
            # Minus 1 here since we start from 1.
            if text1[i - 1] == text2[j - 1]:
                dp[i][j] = dp[i-1][j-1] + 1
            else:
                dp[i][j] = max(dp[i-1][j], dp[i][j-1])
    
    lcs_set = set()
    # Trace back the LCS string.
    def track_back(i: int, j: int, lcs_str: str, max_len: int) -> str:
        # Trace back from dp[m][n] (right-bottom).
        while i > 0 and j > 0:
            # If the two characters are the same, then it's transferred from 
            # dp[i-1][j-1], add the charcter into LCS string and minius 
            # i and j by one.  
            if text1[i-1] == text2[j-1]:
                lcs_str += text1[i-1]
                i -= 1
                j -= 1
            else:
                # If text1[i-1] != text2[j-1], then we need to compare the 
                # value of dp[i-1][j] and dp[i][j-1]. We shall select the 
                # larger one to dive into.
                if dp[i-1][j] > dp[i][j-1]:
                    i -= 1
                elif dp[i-1][j] < dp[i][j-1]:
                    j -= 1 
                # If the two values are the same, it means there are multiple 
                # LCSs, so we need to backtracking to all of them with recursion.
                else:
                    track_back(i - 1, j, lcs_str, max_len)
                    track_back(i, j - 1, lcs_str, max_len)
                    return 
        
        # If the string length is the same as longest LCS, add it into set.
        if len(lcs_str) == max_len:
            lcs_set.add(lcs_str[::-1])

    # Retreive the LCS string.
    track_back(m, n, "", dp[m][n])

    return dp[m][n], lcs_set

def common_subsequence_recur(text1: str, text2: str) -> int:
    """ Recursion - Backward

    Recursion / Backtracking based method from backward.
    """
    def helper(i, j):
        # Empty string for text1 or text2
        if i == -1 or j == -1:
            return 0
        if text1[i] == text2[j]:
            # A common character, so add the length of LCS by 1.
            return helper(i-1, j-1) + 1
        else:
            # Choose the one who can make LCS longer.
            return max(helper(i-1, j), helper(i, j-1))
    
    m, n = len(text1), len(text2)
    return helper(m-1, n-1)

if __name__ == "__main__":
    text1, text2 = "abcde", "ace"
    print(common_subsequence_dp(text1, text2))
    print(common_subsequence_recur(text1, text2))
    
    text1, text2 = "abc", "abc"
    print(common_subsequence_dp(text1, text2))
    print(common_subsequence_recur(text1, text2))

    text1, text2 = "abc", "def"
    print(common_subsequence_dp(text1, text2))
    print(common_subsequence_recur(text1, text2))