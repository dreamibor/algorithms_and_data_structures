"""
Array / Hash Table - Two Sum (easy)

Description:
Given an array of integers `nums` and an integer `target`, return indices of 
the two numbers such that they add up to `target`.

You may assume that each input would have exactly one solution, and you may 
not use the same element twice.

You can return the answer in any order.

Example:
Input: nums = [2,7,11,15], target = 9
Output: [0,1]
Explanation: Because nums[0] + nums[1] == 9, we return [0, 1].

LeetCode link: https://leetcode-cn.com/problems/two-sum/
"""

def two_sum(nums: list, target: int) -> list:
    """ Hash Table
    Since we are looking for target - x, then we can use a hash table 
    since it has a better look-up performance O(1).

    Process:
    1. For each element, we look up whether target - x is already in 
    the hash table, if yes return the indices.
    2. If not, we add this element into the hash table and start next 
    iteration.

    Time Comlexity - For N elements in the array.
    Space Complexity - For hash table, worst case, storing N elements.
    """
    seen = {}

    for index, num in enumerate(nums):
        res = target - num
        if res in seen:
            return [seen[res], index]
        else:
            seen[num] = index
    
    return []

if __name__ == "__main__":
    nums = [2,7,11,15]
    result = two_sum(nums, target=9)
    print(result)