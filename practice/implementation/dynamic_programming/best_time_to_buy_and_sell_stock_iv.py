"""
DP - Best Time to Buy and Sell Stock IV (hard)

Description:
You are given an integer array prices where prices[i] is the price of a given 
stock on the i_th day, and an integer k.

Find the maximum profit you can achieve. You may complete at most k transactions.

Note: You may not engage in multiple transactions simultaneously (i.e., you must 
sell the stock before you buy again).

Example:
Input: k = 2, prices = [2,4,1]
Output: 2
Explanation: Buy on day 1 (price = 2) and sell on day 2 (price = 4), 
profit = 4-2 = 2.

LeetCode: https://leetcode-cn.com/problems/best-time-to-buy-and-sell-stock-iv/
"""


def max_profit_dp(k:int, prices: list) -> int:
    """ Dynamic Programming

    DP state definition:
    dp[i][k][j] - meaning the maximum profit at i_th day, with k transactions 
    and j represents whether we hold the stock or not (so either 0 or 1). The 
    range of i will be [0, n - 1], n is the length of the input array and k 
    will be in the range of [0, K].

    Initialization:
    For the first day, we can but or not buy a share, but we can't sell, so:
    dp[0][0][0] = 0
    dp[0][1][1] = - prices[0]

    DP state transition:
    # If we do not hold a share today
    dp[i][j][0] = max(
        dp[i - 1][j][0],
        dp[i - 1][j][1] + prices[i],
    )
    # If we hold a share today
    dp[i][j][1] = max(
        dp[i - 1][j][1],
        dp[i - 1][j - 1][0] - prices[i],
    )

    Time Complexity - O(N*K) - Iterate through the list and all possible k.
    Space Complexity - O(N*K) - For DP state array.
    """
    # Edge cases.
    if not prices: return 0

    n = len(prices)
    # A transaction is consisted of buying and selling, so if k is larger 
    # than n/2, it folds into the k = +inf case (using greedy).
    k = min(k, n // 2)
    # State definition.
    dp = [[[0] * 2 for _ in range(k + 1)] for _ in range(n)]

    # Initialization.
    for kk in range(k + 1):
        dp[0][kk][0], dp[0][kk][1] = 0, -prices[0]

    # DP state transition.
    for i in range(1, n):
        for kk in range(1, k + 1):
            dp[i][kk][0] = max(dp[i - 1][kk][0], dp[i - 1][kk][1] + prices[i])
            dp[i][kk][1] = max(dp[i - 1][kk][1], dp[i - 1][kk - 1][0] - prices[i])

    return dp[n-1][k][0] # max(dp[n - 1][kk][0] for kk in range(k + 1))


if __name__ == "__main__":
    k, prices = 2, [2,4,1]
    print(max_profit_dp(k, prices))

    k, prices = 2, [3,2,6,5,0,3]
    print(max_profit_dp(k, prices))

    k, prices = 2, [3,3,5,0,0,3,1,4]
    print(max_profit_dp(k, prices))