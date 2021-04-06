"""
Hash Table / Divide and Conquer - Majority Element

Description:
Given an array nums of size n, return the majority element.

The majority element is the element that appears more than ⌊n / 2⌋ times. 
You may assume that the majority element always exists in the array.

Example:
Input: nums = [3,2,3]
Output: 3

Follow-up: Could you solve the problem in linear time and in O(1) space?

LeetCode: https://leetcode-cn.com/problems/majority-element/
"""
from collections import defaultdict

def majority_element_hash_map(nums: list) -> int:
    """ Count the elements with hash map and return the number with the 
    largest frequerncy.

    Time Complexity - O(N) - Iterate the array and hash map once.
    Space Complexity - O(N) - For storing hash map.
    """
    frequency = defaultdict(int)

    for num in nums:
        frequency[num] += 1 

    return max(frequency, key = lambda x: frequency[x]) # max(frequency, key=frequency.get)


def majority_element_sort(nums: list) -> int:
    """ Sort and return the middle number.
    
    Time Complexity - O(N*logN) - For sorting the array.
    Space Complexity - O(1) - Constant space ignoring the sorting required space.
    """
    nums.sort()
    return nums[len(nums) // 2]


if __name__ == "__main__":
    # Hash map
    nums = [2,2,1,1,1,1,1,2,2]
    majority = majority_element_hash_map(nums)
    print(majority)

    # Sort
    nums = [2,2,1,1,1,1,1,2,2]
    majority = majority_element_sort(nums)
    print(majority)