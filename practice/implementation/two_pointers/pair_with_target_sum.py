"""
Two pointers - Pair with Target Sum (easy)

Description:
Given an array of sorted numbers and a target sum, find a pair in the array whose sum is 
equal to the given target.
Write a function to return the indices of the two numbers (i.e. the pair) such that they 
add up to the given target.

Example:
Input: [1, 2, 3, 4, 6], target=6
Output: [1, 3]
Explanation: The numbers at index 1 and 3 add up to 6: 2+4=6

Notes:
1. Only need to return one pair.

Time Complexity - O(N) - N is the total number of elements in the given array.
Space Complexity - O(1)

LeetCode link: https://leetcode-cn.com/problems/he-wei-sde-liang-ge-shu-zi-lcof/
"""


def pair_with_target_sum(arr:list, target:int) -> list:
    left = 0
    right = len(arr) - 1

    while left < right:
        current_sum = arr[left] + arr[right]
        if current_sum > target:
            right -= 1 # Need a smaller number, move the right pointer to left
        elif current_sum < target:
            left += 1 # Need a larger number, move the left pointer to right
        else:
            return [left, right]

    return []

def pair_with_target_sum_hash_table(arr:list, target:int) -> list:
    """ Using a hash table to search for required pair.
    Iterate through the array, store element and it's index.
    Try to find whether (target - num) is already in the hash table.
    Time Complexity - O(N) - N is the number of elements in the given array.
    Space Complexitu - O(N) - worst case, pushing all N numbers into the hash table.
    """
    nums = {}
    for i, num in enumerate(arr):
        # Whether (target - num) is already in the hash table
        if target - num in nums:
            return [nums[target - num], i]
        # Store numbers in the hash table.
        nums[num] = i
        
    return []

if __name__ == "__main__":
    print(pair_with_target_sum([1, 2, 3, 4, 6], 6))
    print(pair_with_target_sum([2, 5, 9, 11], 11))
    print(pair_with_target_sum([2, 7, 11, 15], 9))
    print(pair_with_target_sum([10, 26, 30, 31, 47, 60], 40))
    # For finding pairs using hash table.
    print(pair_with_target_sum_hash_table([1, 2, 3, 4, 6], 6))
    print(pair_with_target_sum_hash_table([2, 5, 9, 11], 11))
    print(pair_with_target_sum_hash_table([2, 7, 11, 15], 9))
    print(pair_with_target_sum_hash_table([10, 26, 30, 31, 47, 60], 40))