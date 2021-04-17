"""
DP - Edit Distance (hard)

Description:
Given two strings word1 and word2, return the minimum number of operations 
required to convert word1 to word2.

You have the following three operations permitted on a word:
1. Insert a character
2. Delete a character
3. Replace a character

Example:
Input: word1 = "horse", word2 = "ros"
Output: 3
Explanation: 
horse -> rorse (replace 'h' with 'r')
rorse -> rose (remove 'r')
rose -> ros (remove 'e')

LeetCode: https://leetcode-cn.com/problems/edit-distance
"""


def edit_distance_dp(word1: str, word2: str) -> int:
    """ Dynamic Programming
    
    State definition:
    dp[i][j] - the minimum distance between index i at word1 and index j 
    at word2.

    Initialization:
    dp[i][0] = i | i ∈ len(word1)
    dp[0][j] = j | j ∈ len(word2)
    即 j 走完 word2 或 i 走完 word1，返回另一个字符串剩下的长度。

    State transition equation:
    dp[i][j] = if word1[i] == word2[j]
                   dp[i - 1][j - 1] 
               else:
                   min(dp[i - 1][j], dp[i][j - 1], dp[i - 1][j - 1]) + 1

    在每一步：
    if s1[i] == s2[j]:
        skip
        i, j 同时向前移动
    else:
        三选一：
            插入（insert）
            删除（delete）
            替换（replace）

    Check ![Edit Distance](assets/edit_distance.png)

    Time Complexity - O(M*N) - M and N are the length of two strings. 
    Space Complexity - O(M*N) - For DP state array.
    """
    m, n = len(word1), len(word2)

    # DP state array, containing "" here, so need a m * n matrix.
    dp = [[0 for _ in range(n + 1)] for _ in range(m + 1)]

    # Initialization
    for i in range(m + 1): dp[i][0] = i
    for j in range(n + 1): dp[0][j] = j

    # DP
    for i in range(1, m + 1):
        for j in range(1, n + 1):
            # Skip if the two characters are the same.
            # Including "", so the index will minus 1 here.
            # See ![DP Table](assets/edit_distance_dp_table.png)
            if word1[i - 1] == word2[j - 1]:
                dp[i][j] = dp[i - 1][j - 1]
            else:
                # Deletion, insertion, replacement.
                dp[i][j] = min(dp[i - 1][j], dp[i][j - 1], dp[i - 1][j - 1]) + 1

    return dp[m][n]

def edit_distance_recur(word1: str, word2: str) -> int:
    """ Recursion

    Drawback: there are overlapping sub-problems.

    Now that we have the minimum edit distance, but what are the specific 
    operations?

    We can define a dp array with extra information, such as:
    ```
    // Rather than int[][] dp;
    Node[][] dp;

    class Node {
        int val;
        int choice;
        // 0 代表啥都不做
        // 1 代表插入
        // 2 代表删除
        // 3 代表替换
    }
    ```

    Reference: https://labuladong.github.io/algo/%E5%8A%A8%E6%80%81%E8%A7%84
    %E5%88%92%E7%B3%BB%E5%88%97/%E7%BC%96%E8%BE%91%E8%B7%9D%E7%A6%BB.html
    """
    def helper(i, j):
        """ 返回 s1[0..i] 和 s2[0..j] 的最小编辑距离 """
        # Recursion termination - base case
        if i == -1: return j + 1
        if j == -1: return i + 1

        if word1[i] == word2[j]:
            return helper(i - 1, j - 1)
        else:
            return min(helper(i, j - 1) + 1, # Insertion
                    helper(i - 1, j) + 1, # Deletion
                    helper(i - 1, j - 1) + 1)# Replacement
    
    return helper(len(word1) - 1, len(word2) - 1)


if __name__ == "__main__":
    word1, word2 = "horse", "ros"
    print(edit_distance_dp(word1, word2))
    print(edit_distance_recur(word1, word2))
    
    word1, word2 = "", "ros"
    print(edit_distance_dp(word1, word2))
    print(edit_distance_recur(word1, word2))