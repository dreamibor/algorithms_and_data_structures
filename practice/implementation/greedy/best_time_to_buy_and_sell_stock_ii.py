"""
Greedy - Best Time to Buy and Sell Stock II

Description:
You are given an array prices where prices[i] is the price of a given stock 
on the ith day.

Find the maximum profit you can achieve. You may complete as many transactions 
as you like (i.e., buy one and sell one share of the stock multiple times).

Note: You may not engage in multiple transactions simultaneously (i.e., you 
must sell the stock before you buy again).

Example:
Input: prices = [7,1,5,3,6,4]
Output: 7
Explanation: Buy on day 2 (price = 1) and sell on day 3 (price = 5), 
profit = 5-1 = 4. Then buy on day 4 (price = 3) and sell on day 5 (price = 6), 
profit = 6-3 = 3.

LeetCode: https://leetcode-cn.com/problems/best-time-to-buy-and-sell-stock-ii
"""


def max_profit_greedy(prices:list) -> int:
    """ Greedy

    As long as tomorrow's price is higher than today, then we buy the stock 
    today and sell it tomorrow.

    Time Complexity - O(N) - Iterate the array once.
    Space Complexity - O(1) - Constant space, only require a variable for 
    result.
    """
    profit = 0

    for i in range(len(prices) - 1):
        if prices[i] < prices[i+1]:
            profit += prices[i+1] - prices[i]
    
    return profit

def max_profit_dp(prices:list) -> int:
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
    stock out so the the last dimension shall be 0. 

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

    For this specific problem, as k = +inf, meaning there is no constraint on 
    the number of total transactions. So we can ignore this dimension.
    dp[i][k][0] = max(dp[i-1][k][0], dp[i-1][k][1] + prices[i])
    dp[i][k][1] = max(dp[i-1][k][1], dp[i-1][k-1][0] - prices[i]) 
                = max(dp[i-1][k][1], dp[i-1][k][0] - prices[i])
    
    As k doesn't change, so we don't need k anymore, and we can simplify the 
    equation to be:
    dp[i][0] = max(dp[i-1][0], dp[i-1][1] + prices[i])
    dp[i][1] = max(dp[i-1][1], dp[i-1][0] - prices[i])

    Time Complexity - O(N) - Iterate through the array once.
    Space Complexity - O(N) - For the DP state array.
    """
    # Edge cases
    if not prices: return 0

    n = len(prices)
    # DP state array
    dp = [[0] * 2 for _ in range(n)]
    # Initialization
    dp[0][0], dp[0][1] = 0, - prices[0]

    for i in range(1, n):
        dp[i][0] = max(dp[i-1][0], dp[i-1][1] + prices[i])
        dp[i][1] = max(dp[i-1][1], dp[i-1][0] - prices[i])
    
    return dp[n-1][0]

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
    # DP state array and initialization
    dp_i_0, dp_i_1 = 0, -prices[0]

    for i in range(1, n):
        temp_dp_i_0 = dp_i_0
        dp_i_0 = max(dp_i_0, dp_i_1 + prices[i])
        dp_i_1 = max(dp_i_1, temp_dp_i_0 - prices[i])
    
    return dp_i_0

if __name__ == "__main__":
    prices = [7,1,5,3,6,4]
    print("Max profit: {}".format(max_profit_greedy(prices)))
    print("Max profit: {}".format(max_profit_dp(prices)))
    print("Max profit: {}".format(max_profit_dp_opt(prices)))

    prices = [1,2,3,4,5]
    print("Max profit: {}".format(max_profit_greedy(prices)))
    print("Max profit: {}".format(max_profit_dp(prices)))
    print("Max profit: {}".format(max_profit_dp_opt(prices)))