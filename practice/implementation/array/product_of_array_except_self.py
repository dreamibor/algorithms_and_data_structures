"""
Array - Product of Array Except Self

Description:
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
    """ Left and Right Product List

    The result product on index i is determined by the numbers on its left 
    and right (prefix and suffix), so we can use two arrays L and R to 
    memorize the product of left and right side of i.
    
    1. Initialize L and R, for given index i, calculate the product on the 
    left and right of it.
    2. Fill L and R, L[0] shall be 1 as there is no element on the left of 
    the first element. L[i] = L[i-1] * nums[i-1]
    3. The same for R, R[n-1] shall be 1, and R[i] = R[i+1] * nums[i+1]
    4. Using L and R to calculate the result, L[i] * R[i].

    Time Complexity - O(N) - N is the number of elements in nums.
    Space Complexity - O(N) - For L and R array.
    """
    # Edge cases
    if not nums: return nums
    
    n = len(nums)

    # Initialize L, R and the result array.
    l, r, res = [0] * n, [0] * n, [0] * n
    
    # Fill L, L[i] is the product of left side elements of i.
    # Since there is no element on the left of index 0, so L[0] = 1
    l[0] = 1
    for i in range(1, n):
        l[i] = nums[i-1] * l[i-1]
    
    # The same for R, R[n-1] shall be 1.
    r[n - 1] = 1
    for i in reversed(range(n - 1)):
        r[i] = nums[i+1] * r[i+1]

    # Calculate the result for index i, where res[i] = L[i] * R[i].
    for i in range(n):
        res[i] = l[i] * r[i]

    return res

def prod_excep_self_opt(nums: list) -> int:
    """ Optimised for Space

    As the result array is not counted in the space complexity, we can use 
    it as the L array and construct R dynamically.

    1. Initialize res array, for give index i, res[i] represents the product 
    of all the elements on the left side of i.
    2. res[i] = res[i] * R
    3. R = R * nums[i], meaning the product of all the elements on the right 
    side of i.

    Time Complexity - O(N) - N is the number of elements in nums.
    Space Complexity - O(1) - Constant space as we don't count the result 
    array.
    """
    # Edge cases
    if not nums: return nums

    n = len(nums)

    # Initialize the result array and use it as L.
    res = [0] * n

    # Update result array as L, where res[i] represents the product of all 
    # the elements of the left of i. res[0] = 1 here as there is no element 
    # on the left of the first element. 
    res[0] = 1
    for i in range(1, n):
        res[i] = res[i-1] * nums[i-1]
    
    # R represents the product of all the elements of the right of i.
    r = 1
    for i in reversed(range(n)):
        # For given index i, the left product is res[i], the right is R.
        res[i] = res[i] * r
        # Update R for the next round.
        r *= nums[i]

    return res


if __name__ == "__main__":
    nums = [1,2,3,4]
    print(prod_excep_self(nums))
    print(prod_excep_self_opt(nums))

    nums = []
    print(prod_excep_self(nums))
    print(prod_excep_self_opt(nums))