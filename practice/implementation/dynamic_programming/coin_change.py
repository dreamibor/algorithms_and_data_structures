"""
DP -  Coin Change (medium)

Description:
You are given an integer array coins representing coins of different 
denominations and an integer amount representing a total amount of money.

Return the fewest number of coins that you need to make up that amount. 
If that amount of money cannot be made up by any combination of the coins, 
return -1.

You may assume that you have an infinite number of each kind of coin.

Example:
Input: coins = [1,2,5], amount = 11
Output: 3
Explanation: 11 = 5 + 5 + 1

LeetCode: https://leetcode-cn.com/problems/coin-change/
"""


def coin_change(coins: list, amount: int) -> int:
    """ Dynamic Programming

    State definition:
    dp[i] - the minimum number of coins for i_th amount.

    dp 数组的定义：当目标金额为 i 时，至少需要 dp[i] 枚硬币凑出。
   
    Assuming we want to know the minimum number of coins for the amount of 
    10, we only need to know the minimum number of coins for 9, 8 and 5, 
    which means we use one 1, 2 or 5 coin here, so we can get the state 
    transition equation as:
    dp[i] = min{ dp[i - coin] + 1 | coin ∈ coins }

    Time Complexity - O(K*N) - Iterate through N and with a inner lopp for 
    choosing all coins.
    Space Complexity - O(N) - DP state array, length = the amount.
    """
    # DP state array, `amount + 1` is equivalent to positive infinity here 
    # as the largest number of coins will be `amount`, meaning only using 
    # the coin wiht value 1.
    dp = [amount + 1] * (amount + 1)
    # Initialization, when the amount is 0, we shall return 0.
    dp[0] = 0

    # DP
    for i in range(1, amount + 1):
        for coin in coins:
            # Check whether (i - coin) is out of range, which means
            #  there is no solution to that amount, such as -1.
            if i - coin >= 0:
                dp[i] = min(dp[i], dp[i - coin] + 1)

    # Check whether dp[amount]'s value has been modified, if not then 
    # there is no solution to this amount.
    return -1 if dp[amount] == (amount + 1) else dp[amount] 

def coin_change_recursion(coins: list, amount: int) -> int:
    """ Naive Recursion

    Time Complexity - O(K * N^K) - For recursion, the complexity is the 
    number of recursion nodes (or the number of sub-problems) times the 
    time complexity for each sub-problem, here the sub-proble's complexity 
    is related to the number of coin types, assuming it's K here, so the 
    time complexity of each sub-problem is O(K) and the number of 
    sub-problems is O(N^K), so in total O(K * N^K).
    Space Complexity - O(N) - For recursion stack.
    """
    def helper(n: int):
        # Recursion termination / base case.
        if n == 0: return 0
        # No solution, exceed the range, return -1.
        if n < 0: return -1

        res = float("inf")

        # Drill down
        for coin in coins:
            subproblem = helper(n - coin)
            if subproblem == -1: continue
            # Get the minimum number of coins.
            res = min(res, 1 + subproblem)
        
        # If the minimum number of coins doesn't exist, return -1.
        return res if res != float("inf") else -1

    return helper(amount)

def coin_change_recur_memo(coins: list, amount: int) -> int:
    """ Recursion with Memorization

    Time Complexity - O(K*N) - K is the number of coin tyoes, N is the amount, 
    comparing to naive recursion, we heavily reduced the number of sub-problems 
    to O(N) now, for each sub-problem, the time complexity is still O(K), so in 
    total O(K * N).
    Space Complexity - O(N) - For recursion stack.
    """
    def helper(n: int):
        # Recursion termination / base case.
        if n == 0: return 0
        # No solution, exceed the range, return -1.
        if n < 0: return -1
        # Check if the value has been calculated.
        if n in memo: return memo[n]

        res = float("inf")

        # Drill down
        for coin in coins:
            subproblem = helper(n - coin)
            if subproblem == -1: continue
            # Get the minimum number of coins.
            res = min(res, 1 + subproblem)
        
        # If the minimum number of coins doesn't exist, return -1.
        # Memorize the calculated value.
        memo[n] = res if res != float("inf") else -1
        return memo[n]

    memo = {}
    return helper(amount)

if __name__ == "__main__":
    coins, amount = [1, 2, 5], 11
    print(coin_change(coins, amount))
    print(coin_change_recursion(coins, amount))
    print(coin_change_recur_memo(coins, amount))