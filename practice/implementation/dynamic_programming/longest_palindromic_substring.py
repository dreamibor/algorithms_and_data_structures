"""
DP - Longest Palindromic Substring

Description:
Given a string s, return the longest palindromic substring in s.

Example:
Input: s = "babad"
Output: "bab"
Note: "aba" is also a valid answer.

LeetCode: https://leetcode-cn.com/problems/longest-palindromic-substring/
"""

def longest_palindrome_dp(s: str) -> str:
    """ Dynamic Programming

    If a string is palindrome, then it's substring with head and tail 
    removed is still palindrome. 

    DP state definition:
    dp[i][j] - whether the substring with index from i to j (closed interval) 
    is a valid palindrome.

    Initialization:
    The diagonal values dp[i][i] are all True.
    
    DP State Transition:
    dp[i][j] = (s[i] == s[j]) and dp[i+1][j-1]

    Time Complexity - O(N^2) - N is the length of the string, for the two 
    nested loops.
    Space Complexity - O(N^2) - For the DP state array.
    """
    # Edge cases
    n = len(s)
    if n < 2: return s

    # DP state definition
    dp = [[False] * n for _ in range(n)]
    # Initialization
    for i in range(n):
        dp[i][i] = True
    
    # Variables to track max palindrome substring's start index 
    # and length.
    max_start = 0
    max_len = 1

    # DP
    # Update column by column, rather than row by row.
    for j in range(1, n):
        for i in range(j):
            # If the two charcters are not the same, it's False.
            if s[i] != s[j]:
                dp[i][j] = False
            else:
                # If the two characters are the same, and the distance 
                # between them is less than 3 (such as 2), meaning there 
                # is only one character between them, so it's palindrome, 
                # assign True.
                if j - i < 3:
                    dp[i][j] = True
                # Otherwise, if the two charcters are the same and the 
                # substring removed the left most and right most is still 
                # palindrome, then the substring is palindrome, assign True.
                else:
                    dp[i][j] = dp[i + 1][j - 1]

            # Update the max subtring, the start and the length.
            if dp[i][j] and j - i + 1 > max_len:
                max_len = j - i + 1
                max_start = i

    return s[max_start: max_start + max_len]
   
def longest_palindrome_center(s: str) -> str:
    """ Expand from Center

    Iterate all palindrome centers (either single character or two same 
    characters) and expand from the center to get maximum palidrome's 
    length. 
    
    If the length of palindrome is odd, then the center is a single 
    character, otherwise, if the length of the palindrome is even, then the 
    center will be two characters.

    Time Complexity - O(N^2) - N is the length of the string, for the two 
    nested loops.
    Space Complexity - O(1) - Constant space.    
    """
    # Edge cases
    n = len(s)
    if n < 2: return s

    def expand_around_center(left, right):
        i, j = left,right
        # Expand the left and right index to two directions.
        while i >=0 and j < n:
            if s[i] == s[j]:
                i -= 1
                j += 1
            else:
                break
        
        # When quit the while loop, s[i] != s[j], so the palindrome's 
        # length is acutally (j - i + 1) - 2 = j - i - 1.
        return j - i - 1

    max_start = 0
    max_len = 1

    # Iterate through all potential substring palindrome centers.
    for i in range(n-1):
        # The center is single character i.
        odd_len = expand_around_center(i, i)
        # The center has two characters i and i + 1.
        even_len = expand_around_center(i, i + 1)
        # Fetch the maximum between odd and even cases
        cur_max_len = max(odd_len, even_len)

        # Compare the current maximum with the global one.
        if cur_max_len > max_len:
            max_len = cur_max_len
            # i is the center, minus the (length - 1) of the substring 
            # divided by 2. We minus the length by 1 here to unify the 
            # odd and even cases. (max_len - 1) // 2 is rounding down.
            max_start = i - (max_len - 1) // 2

    return s[max_start: max_start + max_len]    


if __name__ == "__main__":
    s = "babad"
    print(longest_palindrome_dp(s))
    print(longest_palindrome_center(s))
    