"""
DP - Best Time to Buy and Sell Stock with Transaction Fee (medium)

Decription:

You are given an array prices where prices[i] is the price of a given stock 
on the ith day, and an integer fee representing a transaction fee.

Find the maximum profit you can achieve. You may complete as many transactions 
as you like, but you need to pay the transaction fee for each transaction.

Note: You may not engage in multiple transactions simultaneously (i.e., you 
must sell the stock before you buy again).

Example:
Input: prices = [1,3,2,8,4,9], fee = 2
Output: 8
Explanation: The maximum profit can be achieved by:
- Buying at prices[0] = 1
- Selling at prices[3] = 8
- Buying at prices[4] = 4
- Selling at prices[5] = 9
The total profit is ((8 - 1) - 2) + ((9 - 4) - 2) = 8.

LeetCode: https://leetcode-cn.com/problems/best-time-to-buy-and-sell-stock-with-transaction-fee
"""


def max_profit(prices: list) -> int:
    pass


if __name__ == "__main__":
    prices = [1,2,3,0,2]
    print(max_profit(prices))