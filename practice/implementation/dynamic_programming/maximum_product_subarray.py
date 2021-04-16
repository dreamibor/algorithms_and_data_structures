"""
DP - Maximum Product Subarray (medium)

Description:
Given an integer array nums, find a contiguous non-empty subarray within 
the array that has the largest product, and return the product.

It is guaranteed that the answer will fit in a 32-bit integer.

A subarray is a contiguous subsequence of the array.

Example:
Input: nums = [2,3,-2,4]
Output: 6
Explanation: [2,3] has the largest product 6.

LeetCode: https://leetcode-cn.com/problems/maximum-product-subarray
"""


def max_prod_recursion(nums: list) -> int:
    """ Recursion

    For each step, there are two choices, include or not include the 
    current step's (index) value into the final product. So we can 
    enumerate all possible combinations and return the maximum result.

    Reference: https://leetcode-cn.com/problems/maximum-product-subarray
    /solution/hui-su-di-gui-dong-tai-gui-hua-liang-chong-suan-fa/
    
    Time Complexity - O(2^N) - For recursion, each step, we have 
    two choices.
    Space Complexity - O(N) - For recursion call stack 
    """
    def helper(index: int, prod) -> int:
        nonlocal maximum
        # Recursion termination
        if index >= len(nums) - 1:
            maximum = max(maximum, prod)
            return
        
        # nonlocal maximum
        maximum = max(maximum, prod)
        # Drill down
        helper(index + 1, prod * nums[index + 1])
        helper(index + 1, nums[index + 1])
    
    # Edge cases
    if len(nums) == 0: return -1
    if len(nums) == 1: return nums[0]

    # Result variable
    maximum = nums[0]
    helper(0, nums[0])
    return maximum

def max_prod_dp(nums: list) -> int:
    """ Dynamic Programming

    State definition:
    2D array, dp[n][2], the second dimension means we store max and 
    min values for each index.

    State transition equation:
    dp[i][0] = max(dp[i-1][0]*nums[i], dp[i-1][1]*nums[i], nums[i])
    dp[i][1] = min(dp[i-1][0]*nums[i], dp[i-1][1]*nums[i], nums[i])

    Time Complexity - O(N) - Iterate the array only once.
    Space Complexity - O(N) - For DP state array.
    """
    # Edge cases
    if not nums: return -1
    # State - storing max and min at the current index. 
    n = len(nums)
    dp = [[0]*2 for _ in range(n)]

    dp[0][1], dp[0][0] = nums[0], nums[0]
    res = nums[0]

    for i in range(1, n):
        dp[i][0] = max(dp[i-1][0]*nums[i], dp[i-1][1]*nums[i], nums[i])
        dp[i][1] = min(dp[i-1][0]*nums[i], dp[i-1][1]*nums[i], nums[i])
        res = max(res, dp[i][0])
    
    return res

def max_prod_dp_opt(nums: list) -> int:
    """ Dynamic Programming 

    Optimised for space, we can use only two variables to track the max 
    and min for the previous states.

    Time Complexity - O(N) - Iterate the array only once.
    Space Complexity - O(1) - Constant space for the DP state.
    """
    # Edge cases
    if not nums: return -1

    # DP status and initialization.
    res, cur_max, cur_min = nums[0], nums[0], nums[0]

    for i in range(1, len(nums)):
        # Calculate the value before assign, otherwise use temp variable.
        cur_max, cur_min = cur_max * nums[i], cur_min * nums[i]
        cur_max, cur_min = max(cur_max, cur_min, nums[i]),\
                            min(cur_max, cur_min, nums[i])
        
        res = max(cur_max, res)
        
    return res

if __name__ == "__main__":
    nums = [2,3,-2,4]
    print(max_prod_recursion(nums))
    print(max_prod_dp(nums))
    print(max_prod_dp_opt(nums))

    nums = [-2, 0, -1]
    print(max_prod_recursion(nums))
    print(max_prod_dp(nums))
    print(max_prod_dp_opt(nums))

    nums = [-4,-3,-2]
    print(max_prod_recursion(nums))
    print(max_prod_dp(nums))
    print(max_prod_dp_opt(nums))