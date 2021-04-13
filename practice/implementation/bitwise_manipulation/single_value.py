"""
Bitwise XOR - Single Number (easy)

Description:
Given a non-empty array of integers nums, every element appears twice 
except for one. Find that single one.

Follow up: Could you implement a solution with a linear runtime complexity 
and without using extra memory?

Example:
Input: nums = [2,2,1]
Output: 1

LeetCode: https://leetcode-cn.com/problems/single-number
"""
from functools import reduce


def single_value(nums: list) -> int:
    """ XOR 

    Properties of XOR:
    1. a XOR with 0 is still a. a ^ 0 = a
    2. a XOR with a is 0. a ^ a = 0
    3. Commutative and associative laws: a ^ b ^ a = b ^ a ^ a = b ^ (a ^ a) = b ^ 0 = b

    Time Complexity - O(N) - Loop through the array once.
    Space Complexity - O(1) - Constant space for variable.
    """
    result = nums[0]
    for i in range(1, len(nums)):
        result ^= nums[i]
    return result


def single_value_reduce(nums: list) -> int:
    """ XOR with reduce.

    Time Complexity - O(N) - Loop through the array once.
    Space Complexity - O(1) - Constant space for variable.
    """
    return reduce(lambda x,y :x^ y, nums)

if __name__ == "__main__":
    nums = [2, 2, 1]
    print(single_value(nums))
    print(single_value_reduce(nums))

    nums = [4,1,2,1,2]
    print(single_value(nums))
    print(single_value_reduce(nums))

    nums = [1]
    print(single_value(nums))
    print(single_value_reduce(nums))