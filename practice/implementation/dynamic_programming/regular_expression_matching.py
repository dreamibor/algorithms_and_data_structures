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
    dp[0][0] = True, when the input string and the pattern are both empty, 
    the value is True as two empty string can match.

    DP state transition equation:
    For the j_th character in the pattern:
    1. If the j_th character is a lowercase letter, then we must find a same 
    lowercase letter in the input string, so:
        dp[i][j] = dp[i-1][j-1], s[i] == p[j]
                   False       , s[i] != p[j]
    It means if the i_th letter in string couldn't match with the j_th letter 
    in the pattern, then the value shall be False, otherwise, it depends on 
    the previous part.

    2. If the j_th character in the pattern is '.', then we can always match 
    any single lowercase letter in the input string. 
        dp[i][j] = dp[i-1][j-1], s[i] == p[j]

    3. If the j_th character in the pattern is '*', it means we can match the 
    j-1 character in the pattern for N (non-negative integers / natural number) 
    times.
    When we match 0 times, the equation will be:
        dp[i][j] = dp[i][j-2]
    meaning we ignored the combination of letter + '*' and didn't match any 
    characters in the input string.

    As we can matching zero or more the character before '*', so it's related 
    to p[j-1]. Only when p[j-1] matches (==) s[i], '*' functions, otherwise, 
    we will match 0 times the previous letter, or make the letter disappeared. 
    
    To match the combination of letter and '*', there are two cases:
    (1) Could match the character p[j-1] before '*' with s[i], or the character 
    before '*' is '.'. 
    (2) Couldn't match any character, drop the combination. For example, (ab, 
    abc*), 'ab' could match, and we can match 'c' for zero times, so it's true 
    that these two strings could match.

    The state transition equation is:
        dp[i][j] = dp[i-1][j] or dp[i][j-2], s[i] == p[j-1] or p[j-1] == "."
                   dp[i][j-2]              , s[i] != p[j-1]
    
    Here the different match results are:
    dp[i][j] = dp[i-1][j] // in this case, a* counts as multiple a, for 
                          // example, 'aaab' and 'aaabbb'.
             = dp[i][j-1] // in this case, a* counts as single a, remove the 
                          // effect of '*'. for example, 'qqb' and 'qqb*'.
             = dp[i][j-2] // in this case, a* counts as empty, or remove 'a*'.

    The final will be at dp[m][n], where m and n are the length of input 
    string and pattern respectively.

    Time Complexity - O(M*N) - M and N are the length of the input string and 
    pattern respectively. 
    Space Complexity - O(M*N) - For the DP state array.
    """
    m, n = len(string), len(pattern)

    def matches(i: int, j: int) -> bool:
        """ The function to check whether two characters match.
        params: i - the index of input string.
        parmas: j - the index of the pattern.

        When j's character is '.' or the characters for i and j are the same, 
        return True, meaning they match each other.
        """
        # For initialization dp[0][j].
        if i == 0:
            return False
        # '.' could match any character.
        if pattern[j - 1] == ".":
            return True
        # Return whether i and j match (same character).
        return string[i - 1] == pattern[j - 1]

    # DP state array, plus 1 dimension for empty string.
    dp = [[False] * (n + 1) for _ in range(m + 1)]
    # Initialization, empty string and pattern, could match.
    dp[0][0] = True

    for j in range(1, n + 1):
        # If the j_th character is '*', then it doesn't matter what the 
        # letter for j and j - 1 is, as long as j - 2 has matched, then 
        # it's also matched, otherwise keep False.
        if pattern[j - 1] == '*':
            dp[0][j] = dp[0][j - 2]

    # DP state transition
    for i in range(m + 1):
        for j in range(1, n + 1):
            # For cases when p[j-1] == '*'.
            if pattern[j - 1] == "*":
                # Not matching, s[i] != p[j-1], ignore 'a*'.
                dp[i][j] |= dp[i][j - 2]
                # s[i] == p[j-1] or p[j-1] == '.'.
                if matches(i, j - 1):
                    dp[i][j] |= dp[i - 1][j]
            else:
                # For cases s[i] == p[j] or p[j] == '.'. 
                if matches(i, j):
                    dp[i][j] |= dp[i - 1][j - 1]

    return dp[m][n]


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