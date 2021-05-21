"""
Array - Product of Array Except Self

Given an integer array nums, return an array answer such that answer[i] is 
equal to the product of all the elements of nums except nums[i].

The product of any prefix or suffix of nums is guaranteed to fit in a 32-bit 
integer.

You must write an algorithm that runs in O(n) time and without using the 
division operation.

Example:
Input: nums = [1,2,3,4]
Output: [24,12,8,6]

LeetCode: 
https://leetcode-cn.com/problems/product-of-array-except-self/
https://leetcode-cn.com/problems/gou-jian-cheng-ji-shu-zu-lcof/
"""


def prod_excep_self(nums: list) -> int:
    n = len(nums)

    l, r, res = [0] * n, [0] * n, [0] * n

    l[0] = 1
    for i in range(1, n):
        l[i] = nums[i-1] * l[i-1]
    
    r[n - 1] = 1
    for i in reversed(range(n - 1)):
        r[i] = nums[i+1] * r[i+1]

    for i in range(n):
        res[i] = l[i] * r[i]

    return res

if __name__ == "__main__":
    nums = [1,2,3,4]
    print(prod_excep_self(nums))