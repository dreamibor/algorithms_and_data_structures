"""
DP - Best Time to Buy and Sell Stock (easy)

Description:
You are given an array prices where prices[i] is the price of a given stock 
on the ith day.

You want to maximize your profit by choosing a single day to buy one stock 
and choosing a different day in the future to sell that stock.

Return the maximum profit you can achieve from this transaction. If you 
cannot achieve any profit, return 0.

Example:
Input: prices = [7,1,5,3,6,4]
Output: 5
Explanation: Buy on day 2 (price = 1) and sell on day 5 (price = 6), 
profit = 6-1 = 5.

Note:
Note that buying on day 2 and selling on day 1 is not allowed because you 
must buy before you sell.

LeetCode: https://leetcode-cn.com/problems/best-time-to-buy-and-sell-stock/
"""


def max_profit_dp(prices: list) -> int:
    """ Dynamic Programming

    Each day we have three options: buy, sell and do nothing (rest).

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

    For this specific problem, as k = 1, so for cases where k = 0, dp[i][0][0] 
    shall be 0, and dp[i][0][0] shall be float("-inf").
    dp[i][1][0] = max(dp[i-1][1][0], dp[i-1][1][1] + prices[i])
    dp[i][1][1] = max(dp[i-1][1][1], dp[i-1][0][0] - prices[i]) 
    Here dp[i-1][0][0] = 0, as k is always 1, so k doesn't affect the state 
    transition, we can simplify to state transition equation to:
    dp[i][0] = max(dp[i-1][0], dp[i-1][1] + prices[i])
    dp[i][1] = max(dp[i-1][1], -prices[i])

    Time Complexity - O(N) - Iterate through the array once.
    Space Complexity - O(N) - For the DP state array.
    """
    if not prices: return 0

    n = len(prices)
    # Define state array
    dp = [[0] * 2 for _ in range(n)]
    # Initialization for day 0.
    dp[0][0], dp[0][1] = 0, -prices[0]

    # DP
    for i in range(1, n):
        dp[i][0] = max(dp[i-1][0], dp[i-1][1] + prices[i])
        dp[i][1] = max(dp[i-1][1], -prices[i])
    
    return dp[n - 1][0]

def max_profit_dp_opt(prices: list) -> int:
    """ Dynamic Programming - Optimized for Space

    Since dp[i][0 or 1] is only related to dp[i-1][ 0 or 1], so can simply 
    use two variables (dp_i_0 and dp_i_1) to track the previous states. 

    Time Complexity - O(N) - Iterate through the array once.
    Space Complexity - O(1) - Constant space for the two variables.
    """
    # Edge cases
    if not prices: return 0

    n = len(prices)
    # Define state array and initialization
    dp_i_0, dp_i_1 = 0, -prices[0]

    # DP
    for i in range(1, n):
        dp_i_0 = max(dp_i_0, dp_i_1 + prices[i])
        dp_i_1 = max(dp_i_1, -prices[i])
    
    return dp_i_0

if __name__ == "__main__":
    prices = [7,1,5,3,6,4]
    print(max_profit_dp(prices))
    print(max_profit_dp_opt(prices))

    prices = [7]
    print(max_profit_dp(prices))
    print(max_profit_dp_opt(prices))