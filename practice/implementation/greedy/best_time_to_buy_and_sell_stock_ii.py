"""
Greedy - Best Time to Buy and Sell Stock II

Description:
You are given an array prices where prices[i] is the price of a given stock on the ith day.

Find the maximum profit you can achieve. You may complete as many transactions as you like (i.e., buy one 
and sell one share of the stock multiple times).

Note: You may not engage in multiple transactions simultaneously (i.e., you must sell the stock before you 
buy again).

Example:
Input: prices = [7,1,5,3,6,4]
Output: 7
Explanation: Buy on day 2 (price = 1) and sell on day 3 (price = 5), profit = 5-1 = 4.
Then buy on day 4 (price = 3) and sell on day 5 (price = 6), profit = 6-3 = 3.

LeetCode: https://leetcode-cn.com/problems/best-time-to-buy-and-sell-stock-ii
"""


def max_profit_greedy(prices:list) -> int:
    """ Greedy

    As long as the price of tomorrow is higher than today, then we buy the stock today
    and sell the stock tomorrow.

    Time Complexity - O(N) - Iterate the array once.
    Space Complexity - O(1) - Constant space, only require a variable for result.
    """
    profit = 0

    for i in range(len(prices) - 1):
        if prices[i] < prices[i+1]:
            profit += prices[i+1] - prices[i]
    
    return profit

def max_profit_dp(prices:list) -> int:
    """ Dynamic Programming

    Time Complexity - O(N) - 
    Space Complexity - O(N) -
    """
    pass

if __name__ == "__main__":
    prices = [7,1,5,3,6,4]
    print("Max profit: {}".format(max_profit_greedy(prices)))