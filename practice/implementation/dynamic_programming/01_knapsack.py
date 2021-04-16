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

Reference: https://www.educative.io/courses/grokking-dynamic-programming
-patterns-for-coding-interviews/RM1BDv71V60
"""


