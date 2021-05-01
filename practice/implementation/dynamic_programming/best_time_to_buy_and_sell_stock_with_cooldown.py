"""
DP - Best Time to Buy and Sell Stock with Cooldown (medium)

Decription:
You are given an array `prices` where `prices[i]` is the price of a given 
stock on the i_th day.

Find the maximum profit you can achieve. You may complete as many transactions 
as you like (i.e., buy one and sell one share of the stock multiple times) 
with the following restrictions:

* After you sell your stock, you cannot buy stock on the next day (i.e., 
cooldown one day).

Note: You may not engage in multiple transactions simultaneously (i.e., you 
must sell the stock before you buy again).

Example:
Input: prices = [1,2,3,0,2]
Output: 3
Explanation: transactions = [buy, sell, cooldown, buy, sell]

LeetCode: https://leetcode-cn.com/problems/best-time-to-buy-and-sell-stock-with-cooldown
"""


def max_profit_dp(prices: list) -> int:
    """
    Each day we have three options: buy, sell and do nothing (rest). Here 
    the option of today will depend on the day before since we need to 
    cooldown for at least 1 day.

    DP State Definition:
    dp[i][k][0 or 1] - meaning the maximum profit we can achieve on day i 
    with k transactions, 0 or 1 represents we hold or not the stock. i is 
    in the range of [0, n), and k is in the range of [1, K]. n is the 
    number of days or the length of the input array. K is the maximum 
    amount of transactions. So in total, we have n * K * 2 states.

    For example, dp[3][2][1] means the maximum profit we can achieve on the 
    third day, with a stock at hand, and did at most 2 transactions.

    The final answer will be dp[n-1][K][0], here we shall always sell the 
    stock out, the the last dimension shall be 0. 

    Initialization:
    dp[0][0][0] = 0
    dp[0][0][1] = float("-inf")

    DP State Transition:
    # If we do NOT hold a share today
    dp[i][k][0] = max(
        dp[i - 1][k][0], # Do nothing and we also don't have stock yesterday.
        # Sell the stock, it's k here as we are finishing the same transaction.
        dp[i - 1][k][1] + prices[i],
    )
    # If we hold a share today
    dp[i][k][1] = max(
        dp[i - 1][k][1], # Hold the stock from yesterday and do nothing.
        # Buy the stock, it's k - 1 here as we are starting a new transaction.
        dp[i - 1][k - 1][0] - prices[i], 
    )

    For this specific problem, as k = +infinity, meaning there is no constraint 
    on the number of total transactions. So we can ignore this dimension.
    dp[i][k][0] = max(dp[i-1][k][0], dp[i-1][k][1] + prices[i])
    dp[i][k][1] = max(dp[i-1][k][1], dp[i-1][k-1][0] - prices[i]) 
                = max(dp[i-1][k][1], dp[i-1][k][0] - prices[i])
    
    As k doesn't change, so we don't need k anymore, and we can simplify the 
    equation to be:
    dp[i][0] = max(dp[i-1][0], dp[i-1][1] + prices[i])
    dp[i][1] = max(dp[i-1][1], dp[i-1][0] - prices[i])

    Also, in the specific problem, we need to cool down for at least one day 
    after selling the stock, so the transition equation will be:
    dp[i][0] = max(dp[i-1][0], dp[i-1][1] + prices[i])
    dp[i][1] = max(dp[i-1][1], dp[i-2][0] - prices[i])
    # When we but on i_th day, we need to transit from i-2 rather than i -1. 

    Time Complexity - O(N) - Iterate through the array once.
    Space Complexity - O(N) - For the DP state array.
    """
    # Edge cases
    if not prices or len(prices) == 1: return 0

    n = len(prices)
    # DP state array
    dp = [[0] * 2 for _ in range(n)]
    # Initialization
    dp[0][0], dp[0][1] = 0, - prices[0]
    dp[1][0], dp[1][1] = max(0, dp[0][1] + prices[1]), max(dp[0][1], 0 - prices[1])

    for i in range(2, n):
        dp[i][0] = max(dp[i-1][0], dp[i-1][1] + prices[i])
        dp[i][1] = max(dp[i-1][1], dp[i-2][0] - prices[i])

    return dp[n-1][0]

def max_profit_dp_opt(prices: list) -> int:
    """ Dynamic Programming - Optimized for Space

    Since dp[i][0 or 1] is only related to dp[i-1][ 0 or 1] and dp[i-2][0], 
    so can simply use three variables (dp_i_0, dp_i_1 and dp_prev_i_0) to 
    track the previous states. 

    Time Complexity - O(N) - Iterate through the array once.
    Space Complexity - O(1) - Constant space for the two variables.
    """
    # Edge cases
    if not prices or len(prices) == 1: return 0

    n = len(prices)
    # DP state variable and initialization
    dp_i_0, dp_i_1 = 0, -prices[0]
    dp_prev_i_0 = 0 # Represents dp[i-2][0]

    for i in range(n):
        temp = dp_i_0
        dp_i_0 = max(dp_i_0, dp_i_1 + prices[i])
        dp_i_1 = max(dp_i_1, dp_prev_i_0 - prices[i])
        dp_prev_i_0 = temp
    
    return dp_i_0


if __name__ == "__main__":
    prices = [1,2,3,0,2]
    print(max_profit_dp(prices))
    print(max_profit_dp_opt(prices))

    prices = [1]
    print(max_profit_dp(prices))
    print(max_profit_dp_opt(prices))

