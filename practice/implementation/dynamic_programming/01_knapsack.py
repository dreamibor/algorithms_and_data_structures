"""
DP - 0/1 Knapsack

Description:
Given two integer arrays to represent weights and profits of ‘N’ items, 
we need to find a subset of these items which will give us maximum profit 
such that their cumulative weight is not more than a given number ‘C’. 
Each item can only be selected once, which means either we put an item in 
the knapsack or skip it.

Example:
Items: { Apple, Orange, Banana, Melon }
Weights: { 2, 3, 1, 4 }
Profits: { 4, 5, 3, 7 }
Knapsack capacity: 5

Output: Banana + Melon (total weight 5) => 10 profit

LintCode: https://www.lintcode.com/problem/backpack-ii/description

Reference: https://www.educative.io/courses/grokking-dynamic-programming
-patterns-for-coding-interviews/RM1BDv71V60
"""


def knapsack_dp_opt(profits: list, weights: list, capacity: int) -> int:
    """ DP with Optimised Space Complexity.

    For the state transition equaton, we only need two values from the 
    previous iteration: dp[i-1][c] and dpdp[i-1][c - weights[i]]. So we 
    can simplify the state array to 1D.

    For the inner loop iterating over c (0 -> capacity), when we access 
    dp[c], it has not been overidden for the current iteration, so we 
    can use it directly. For dp[c - weights[i]], it might be overriden 
    if weights[i] > 0, so we can't use it.

    To solve the problem, we can change the inner loop to iterate in the 
    reverse direction (capacity -> 0).

    Time Complexity - O(N*C) - N represents the number of total items, and 
    C is the maximum capacity.
    Space Complexity - O(C) - For the optimised 1D DP state array.
    """
    n = len(profits)
    # Edge cases
    if capacity <= 0 or n == 0 or len(weights) != n:
        return 0
    
    # DP state array
    dp = [0 for _ in range(capacity + 1)] 

    # Initialization
    # If we only have the first item, we can take it if its weight is 
    # under or equal to the capacity. 
    for c in range(capacity + 1):
        if weights[0] <= c:
            dp[c] = profits[0]
    
    # DP
    for i in range(1, n):
        for c in range(capacity, -1, -1):
            profit_with, profit_without = 0, 0
            # Include the item if it's not more than the capacity.
            if weights[i] <= c:
                profit_with = profits[i] + dp[c - weights[i]]
            # Exclude the item.
            profit_without = dp[c]
            # Take the maximum between with and without the item.
            dp[c] = max(profit_with, profit_without)

    return dp[capacity]

def knapsack_dp(profits: list, weights: list, capacity: int) -> int:
    """ Dynamic Programming

    We want to find the maximum profit for every sub-array and for every 
    possible capacity.

    State definition:
    dp[i][c] will represent the maximum knapsack profit for capacity `c` 
    calculated from the first `i` items.

    For each item at index `i` (0 <= i < items.length) and capacity `c` 
    (0 <= c <= capacity), we have two options:
    1. Exclude the item, dp[i][c] = dp[i-1][c].
    2. Include the item, if its weight is not more than the capacity, 
    dp[i][c] = profits[i] + dp[i-1][c - weights[i]].

    Initialization:
    c = 0, dp[i][0] = 0 | i ∈ the number of items, len(profits).
    With 0 capacity, maximum profit we can have for every subarray is 0.

    index = 0, capacity ∈ {1...C}, i.e., if we consider the sub-array till 
    index 0, this means we have only one item to put in the knapsack, we 
    will take it if it is not more than the capacity.

    State transition equation:
    dp[i][c] = max (dp[i - 1][c], profits[i] + dp[i - 1][c - weights[i]])

    The final profit is at the bottom-right corner.
    
    Time Complexity - O(N*C) - N represents the number of total items, and 
    C is the maximum capacity.
    Space Complexity - O(N*C) - For the 2D DP state array.
    """
    n = len(profits)
    # Edge cases
    if capacity <= 0 or n == 0 or len(weights) != n:
        return 0
    
    # DP state array
    dp = [[0 for _ in range(capacity + 1)] for _ in range(n)]

    # Initialization
    # Capacity = 0, will have 0 profit.
    for i in range(n): dp[i][0] = 0
    # If we only have the first item, we can take it if its weight is 
    # under or equal to the capacity. 
    for c in range(capacity + 1):
        if weights[0] <= c:
            dp[0][c] = profits[0]
    
    # DP
    for i in range(1, n):
        for c in range(1, capacity + 1):
            profit_with, profit_without = 0, 0
            # Include the item if it's not more than the capacity.
            if weights[i] <= c:
                profit_with = profits[i] + dp[i-1][c - weights[i]]
            # Exclude the item.
            profit_without = dp[i-1][c]
            # Take the maximum between with and without the item.
            dp[i][c] = max(profit_with, profit_without)

    return dp[n - 1][capacity]

def knapsack_recur_memo(profits: list, weights: list, capacity: int) -> int:
    """ Recursion with Memorization

    Since we have two chaning values, cur_index and cur_capacity, sp we need 
    two dimensional array to store the results of sub-problems.
    Here we define a 2D array with the shape: (number of items * capacity)

    Time Complexity - O(N*C) - N is the number of items and C is the knapsack 
    capacity, since we store the results for all sub-problems, so the time 
    complexity is O(N*C).
    Space Complexity - O(N*C) - For the memorization array + O(N) space for 
    the recursion call stack, in total O(N * C + N), simplified to O(N * C).
    """
    def helper(cur_capcity, cur_index):
        # Recursion termination, check if the capacity runs out or the 
        # index is out of range (items have been traversed).
        if cur_capcity <= 0 or cur_index >= len(profits):
            return 0

        # Value already calculated, just return.
        if memo[cur_index][cur_capcity] != -1:
            return memo[cur_index][cur_capcity]
        
        # Drill down, two cases: with or without the current item.
        profit_with = 0
        if weights[cur_index] <= cur_capcity:
            # With the current item, update current capacity.
            profit_with = profits[cur_index] + \
                helper(cur_capcity - weights[cur_index], cur_index + 1)
        
        profit_without = helper(cur_capcity, cur_index + 1)

        # Write down to memorization.
        memo[cur_index][cur_capcity] = max(profit_with, profit_without)
        return memo[cur_index][cur_capcity]
    
    memo = [[-1 for _ in range(capacity + 1)] for _ in range(len(profits))]

    return helper(capacity, 0)

def knapsack_recur(profits: list, weights: list, capacity: int) -> int:
    """ Naive Recursion

    Drawback: overlapping sub-problems.

    Time Complexity - O(2^N) - Each step, we have two choices. N represents 
    the total number of items here.
    Space Complexity - O(N) - For the recursion call stack.
    """
    def helper(cur_capcity, cur_index):
        # Recursion termination, check if the capacity runs out or the 
        # index is out of range (items have been traversed).
        if cur_capcity <= 0 or cur_index >= len(profits):
            return 0
        
        # Drill down, two cases: with or without the current item.
        profit_with = 0
        if weights[cur_index] <= cur_capcity:
            # With the current item, update current capacity.
            profit_with = profits[cur_index] + \
                helper(cur_capcity - weights[cur_index], cur_index + 1)
        
        profit_without = helper(cur_capcity, cur_index + 1)

        return max(profit_with, profit_without)
    
    return helper(capacity, 0)

if __name__ == "__main__":
    profits, weights, capacity = [1, 6, 10, 16], [1, 2, 3, 5], 7
    print(knapsack_dp_opt(profits, weights, capacity))
    print(knapsack_dp(profits, weights, capacity))
    print(knapsack_recur_memo(profits, weights, capacity))
    print(knapsack_recur(profits, weights, capacity))

    profits, weights, capacity = [1, 6, 10, 16], [1, 2, 3, 5], 6
    print(knapsack_dp_opt(profits, weights, capacity))
    print(knapsack_dp(profits, weights, capacity))
    print(knapsack_recur_memo(profits, weights, capacity))
    print(knapsack_recur(profits, weights, capacity))