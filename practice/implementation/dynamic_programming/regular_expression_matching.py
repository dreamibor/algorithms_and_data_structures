"""
DP - Regular Expression Matching (hard)

Description:
Given an input string (s) and a pattern (p), implement regular expression 
matching with support for '.' and '*' where: 
1. '.' Matches any single character.​​​​
2. '*' Matches zero or more of the preceding element.

The matching should cover the entire input string (not partial).

Example:
Input: s = "aa", p = "a"
Output: false
Explanation: "a" does not match the entire string "aa".

LeetCode: https://leetcode-cn.com/problems/regular-expression-matching/
"""


def is_match(string: str, pattern: str) -> bool:
    """ Dynamic Programming

    DP state definition:
    dp[i][j] - Whether the first i elements in the string could be matched 
    with first j elements in the pattern.

    Initialization:


    DP state transition equation:
    


    Time Complexity - O(M*N) - 
    Space Complexity - O(M*N) - 
    """
    pass



if __name__ == "__main__":
    string, pattern = "aa", "a"
    print(is_match(string, pattern))

    string, pattern = "aa", "a*"
    print(is_match(string, pattern))

    string, pattern = "ab", ".*"
    print(is_match(string, pattern))

    string, pattern = "aab", "c*a*b"
    print(is_match(string, pattern))

    string, pattern ="mississippi", "mis*is*p*."
    print(is_match(string, pattern))