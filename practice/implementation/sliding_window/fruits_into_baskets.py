"""
Grokking the Coding Interview: Patterns for Coding Questions
Sliding window - Fruits into Baskets (medium)

Description:
Given an array of characters where each character represents a fruit tree, you are given two baskets 
and your goal is to put maximum number of fruits in each basket. The only restriction is that each 
basket can have only one type of fruit.

You can start with any tree, but once you have started you can’t skip a tree. You will pick one 
fruit from each tree until you cannot, i.e., you will stop when you have to pick from a third fruit type.

Write a function to return the maximum number of fruits in both the baskets.

Input: Fruit=['A', 'B', 'C', 'A', 'C']
Output: 3
Explanation: We can put 2 'C' in one basket and one 'A' in the other from the subarray ['C', 'A', 'C']

Time Complexity - O(N)
Space Complexity - O(1)

LeetCode link: https://leetcode-cn.com/problems/fruit-into-baskets/
"""

def fruits_into_baskets(fruits):
    window_start = 0
    max_num = 0
    current_fruit_num = set()

    for window_end in range(len(fruits)):
        current_fruit_num.add(fruits[window_end])

    while len(current_fruit_num) > 2:
        window_start += 1
        current_fruit_num = set(fruits[window_start:window_end+1])

    max_num = max(max_num, window_end-window_start+1)

    return max_num

if __name__=="__main__":
    print("Maximum number of fruits: " + str(fruits_into_baskets(['A', 'B', 'C', 'A', 'C'])))
    print("Maximum number of fruits: " + str(fruits_into_baskets(['A', 'B', 'C', 'B', 'B', 'C'])))