"""
DP - Longest Common Substring (easy)

Given two strings ‘X’ and ‘Y’, find the length of the longest common 
substring. 

Example:
Input : X = "abcdxyz", y = "xyzabcd"
Output : 4 
Explanation:
The longest common substring is “abcd” and is of length 4.

GeeksforGeeks: https://www.geeksforgeeks.org/longest-common-substring-dp-29/
"""


def lcs(str1: str, str2: str) -> int:
    """ DP

    DP state definition:
    dp[i][j] - the maximum LCS length at index i of str1 and index j of str2. 


    Time Complexity - O(M*N) - DP transition.
    Space Complexity - O(M*N) - For the DP array.
    """
    # Edge cases
    if not str1 or not str2: return 0

    max_len = 0
    m, n = len(str1), len(str2)

    # DP state array
    dp = [[0]*(n+1) for _ in range(m+1)]

    for i in range(1, m + 1):
        for j in range(1, n + 1):
            if str1[i - 1] == str2[j - 1]:
                # If the two characters are the same, update the dp
                # value and compare with current maximum.
                dp[i][j] = dp[i-1][j-1] + 1
                max_len = max(dp[i][j], max_len)
            else:
                # If the two characters are not the same, then
                # set to 0 as it's common substring here.
                dp[i][j] = 0
    
    # Output the LCS string with tracing back.
    lcs_set = set()
    for i in range(1, m + 1):
        for j in range(1, n + 1):
            # Look up for dp value the same as maximum LCS length.
            if dp[i][j] == max_len:
                # Trace back, as dp[i][j] comes from dp[i-1][j-1].
                ii, jj = i, j
                temp_str = ""
                while dp[ii][jj] > 0:
                    temp_str += str1[ii - 1]
                    ii -= 1
                    jj -= 1
                # Reverse and add the string into set.
                lcs_set.add(temp_str[::-1]) 

    return max_len, lcs_set


if __name__ == "__main__":
    A = "今天 天气 很好 ， 今天 心情 也 很好 。" 
    B = "今天 天气 很好 ， 但是 今天 心情 不 好 。"
    C = "今天 天气 不 好 ， 今天 心情 很好 。" 

    print(lcs(A, B))
    print(lcs(A, C))
    print(lcs(B, C))
    print(lcs("abcdxyz", "xyzabcd"))