"""
DP - Best Time to Buy and Sell Stock III (hard)

Description:
You are given an array prices where prices[i] is the price of a given stock 
on the ith day.

Find the maximum profit you can achieve. You may complete at most two 
transactions.

Note: You may not engage in multiple transactions simultaneously (i.e., you 
must sell the stock before you buy again).

Example:
Input: prices = [3,3,5,0,0,3,1,4]
Output: 6
Explanation: Buy on day 4 (price = 0) and sell on day 6 (price = 3), profit 
= 3-0 = 3. Then buy on day 7 (price = 1) and sell on day 8 (price = 4), 
profit = 4-1 = 3.

LeetCode: https://leetcode-cn.com/problems/best-time-to-buy-and-sell-stock-iii/
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

    Here k = 2, so need to iterate through K as well.

    Reference: https://leetcode-cn.com/problems/best-time-to-buy-and-sell-stock-iii/
    solution/tong-su-yi-dong-de-dong-tai-gui-hua-jie-fa-by-marc/

    Time Complexity - O(N) - Iterate through the array once, k = 2 is constant.
    Space Complexity - O(N) - For the DP state array, k = 2 is constant.
    """ 
    # Edge cases
    if not prices: return 0

    n = len(prices)
    max_k = 2
    # DP state array
    dp = [[[0] * 2 for _ in range(max_k + 1)] for _ in range(n)]
    # Initialization
    dp[0][0][0], dp[0][0][1] = 0, -prices[0]
    dp[0][1][0], dp[0][1][1] = float("-inf"), float("-inf")
    dp[0][2][0], dp[0][2][1] = float("-inf"), float("-inf")

    # DP transition
    for i in range(1, n):
        # for k in range(1, max_k + 1):
        #     dp[i][k][0] = max(dp[i-1][k][0], dp[i-1][k][1] + prices[i])
        #     dp[i][k][1] = max(dp[i-1][k][1], dp[i-1][k - 1][0] - prices[i])
        
        # Since k = 2, we can list all the possible cases.
        # Never sold out the stock, and doesn't hold a share, so profit shall be 0.
        dp[i][0][0] = 0 # equivalent to dp[i-1][0][0]
        # Never sold out the stock, but hold a share, so buy it today or before.
        dp[i][0][1] = max(dp[i-1][0][1], dp[i-1][0][0] - prices[i])
        # Sold out one share, and doesn't hold a share, sell it today or before.
        dp[i][1][0] = max(dp[i-1][1][0], dp[i-1][0][1] + prices[i])
        # Sold out one share, and still have a share, so buy it today or before.
        dp[i][1][1] = max(dp[i-1][1][1], dp[i-1][1][0] - prices[i])
        # Sold out two shares, and doesn't hold a share, sell it today or before.
        dp[i][2][0] = max(dp[i-1][2][0], dp[i-1][1][1] + prices[i])
        # Beyond two transactions, invalid.
        dp[i][2][1] = float("-inf")

    return max(dp[n - 1][0][0], dp[n - 1][1][0], dp[n - 1][2][0])

def max_profit_dp_opt(prices: list) -> int:
    """ Dynamic Programming - Optimized for Space

    Since k is constant and equals to 2, we can list all the possible cases, and 
    the DP state transition equation only depends on the previous day, we can 
    remove the first dimension as well, so we can use four variables to track 
    the DP state.

    Time Complexity - O(N) - Iterate through the array once, k = 2 is constant.
    Space Complexity - O(1) - Constant space.
    """
    # Edge cases
    if not prices: return 0

    n = len(prices)
    # DP state array (variable) and initialization.
    dp_i_1_0, dp_i_1_1 = 0, float("-inf")
    dp_i_2_0, dp_i_2_1 = 0, float("-inf")

    # DP state transition
    # dp[i][2][0] = max(dp[i-1][2][0], dp[i-1][2][1] + prices[i])
    # dp[i][2][1] = max(dp[i-1][2][1], dp[i-1][1][0] - prices[i])
    # dp[i][1][0] = max(dp[i-1][1][0], dp[i-1][1][1] + prices[i])
    # dp[i][1][1] = max(dp[i-1][1][1], -prices[i])
    for price in prices:
        # The maximumi if we've just sold 2nd stock so far.
        dp_i_2_0 = max(dp_i_2_0, dp_i_2_1 + price)
        # The maximumi if we've just buy  2nd stock so far.
        dp_i_2_1 = max(dp_i_2_1, dp_i_1_0 - price)
         # The maximumi if we've just sold 1st stock so far.
        dp_i_1_0 = max(dp_i_1_0, dp_i_1_1 + price)
         # The maximumi if we've just buy  1st stock so far.
        dp_i_1_1 = max(dp_i_1_1, -price)
    
    return dp_i_2_0

if __name__ == "__main__":
    prices = [3,3,5,0,0,3,1,4]
    print(max_profit_dp(prices))
    print(max_profit_dp_opt(prices))