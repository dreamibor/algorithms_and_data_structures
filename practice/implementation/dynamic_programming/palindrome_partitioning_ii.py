"""
DP - Palindrome Partitioning II (hard)

Description:
Given a string s, partition s such that every substring of the partition is 
a palindrome.

Return the minimum cuts needed for a palindrome partitioning of s.

Example:
Input: s = "aab"
Output: 1
Explanation: The palindrome partitioning ["aa","b"] could be produced using 
1 cut.

LeetCode: https://leetcode-cn.com/problems/palindrome-partitioning-ii/
"""


def min_cut(s: str) -> int:
    """ Dynamic Programming

    DP state definition:
    f[i] - the minimum split times at index i for predix s[0...i].

    Initialization:
    Initialize the DP array with maximum float number.

    DP state transition:
    TO calculate the value of f[i], we can get the last palindrome split 
    before i, and the state transition equation will be:
    f[i] = min(f[j]) + 1 for j ∈ [0, i) and s[j+1...i] is a palindrome. 
    We propose the last palindrome start postion before i as j + 1, and 
    s[j+1...i] is a palindrome, so f[i] can be transferred from f[j], and 
    the split times for f[i] will be f[j] + 1.

    We also need to consider the situation for s[0...i] itself is a 
    palindrome, and in this case, we don't need to split and f[i] = 0.

    The final answer will be f[n - 1].

    We can use DP to do preprocessing and figure whether s[i...j] is a 
    palindrome. So the time complexity for checking whether a string is 
    palindrome will be O(1).
    
    Time Complexity - O(N^2) - For the DP state transition of both the 
    preprocessing and the minimum task.
    Space Complexity - O(N^2) - For the first DP array. The second DP array
    requires O(N) space.
    """
    n = len(s)
    # DP state array for preprocessing.
    dp = [[True] * n for _ in range(n)]

    # DP state transition for palindrome proprocessing.
    for i in reversed(range(n)):
        for j in range(i+1, n):
            dp[i][j] = (s[i] == s[j]) and dp[i+1][j-1]

    # DP state array for the minimum cut task.
    f = [float("inf")] * n

    for i in range(n):
        # For s[0...i] itself is a palindrome.
        if dp[0][i]:
            f[i] = 0
        else:
            # Check the last palindrome (with minimum cut) before index i.
            for j in range(i):
                # If s[j+1...i] is a palindrome, then update the DP state.
                if dp[j+1][i]:
                    # Compare with other j values and get the minimum one.
                    f[i] = min(f[i], f[j] + 1)
    
    return f[n-1]
    

if __name__ == "__main__":
    s = "aab"
    print(min_cut(s))

    s = "a"
    print(min_cut(s))