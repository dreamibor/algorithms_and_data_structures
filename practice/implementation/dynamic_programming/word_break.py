"""
DP - Word Break (medium)

Description:
Given a string s and a dictionary of strings wordDict, return true if s can 
be segmented into a space-separated sequence of one or more dictionary words.

Note that the same word in the dictionary may be reused multiple times in the 
segmentation.

Example:
Input: s = "leetcode", wordDict = ["leet","code"]
Output: true
Explanation: Return true because "leetcode" can be segmented as "leet code".

LeetCode: https://leetcode-cn.com/problems/word-break/
"""


def word_break(string: str, word_dict: list) -> bool:
    """ Dynamic Programming

    DP state definition:
    dp[i] - Whether the previous i characters could be broken into words in 
    the word_dict.

    Initialization:
    dp[0] representing empty string, shall be True.

    DP state transition:
    Iterating through all substrings, starting with index i which is in the 
    range of [0, n), and ending with index j in the range of [i+1, n+1):
    If dp[i] = True and string[i:j] is in the word list, then:
        dp[j] = True
    
    dp[i] = True meaning the previous i characters could be represented with 
    words in the word list, and string[i:j] is in the word list means the 
    previoud j characters could be represented as well.

    Return dp[n] as the result.

    Time Complexity - O(N^2) - Iterate all substrings.
    Space Complexity - O(N) - For DP array. 
    """
    # Edge cases
    if not string or not word_dict: return True

    n = len(string)
    # DP state definition
    dp = [False] * (n + 1)

    # Initialization
    dp[0] = True

    # DP state transition
    for i in range(n):
        for j in range(i+1, n+1):
            # Optimization:
            # 1. Pruning based on words' length. Words' lengths usually have a fixed range. 
            # We can get the minimum and maximum length in the word dict and ignore those 
            # out of range.
            # 2. Using set / hash table rather than list for searching.
            if dp[i] and string[i:j] in word_dict:
                dp[j] = True

    return dp[n]


if __name__ == "__main__":
    string, word_dict = "leetcode", ["leet", "code"]
    print(word_break(string, word_dict))

    string, word_dict = "applepenapple", ["apple", "pen"]
    print(word_break(string, word_dict))

    string, word_dict = "catsandog", ["cats", "dog", "sand", "and", "cat"]
    print(word_break(string, word_dict))