"""
DP - Maximum Subarray (easy)

Description:
Given an integer array nums, find the contiguous subarray (containing at 
least one number) which has the largest sum and return its sum.

Example:
Input: nums = [-2,1,-3,4,-1,2,1,-5,4]
Output: 6
Explanation: [4,-1,2,1] has the largest sum = 6.

LeetCode: https://leetcode-cn.com/problems/maximum-subarray/
"""


def max_subarray(nums: list) -> int:
    """ Dynamic Programming

    State definition:
    dp[i] - the maximum sum until index i.

    Initialization:
    dp[-1] = 0 or dp[0] = nums[0]

    State transition:
    dp[i] = max(dp[i-1] + nums[i], nums[i])
    
    We can take concatenate the current value with the previous 
    maximum subarray dp[i-1], or it can be a new piece.

    Since dp[i] is only related to the previous state dp[i-1], so we 
    can use a variable to replace the DP state array.
    dpi = max(dpi + nums[i], nums[i])
    So we can optimize the space complexity to O(1).

    Time Complexity - O(N) - Iterate through the array once.
    Space Complexity - O(1) - Constant space.
    """
    # Edge cases
    if not nums: return 0

    # DP state variable and result (maximum sum).
    dpi, res = 0, nums[0]

    for num in nums:
        # Either concatenate with previous maximum subarray, 
        # or start with the current value as a new subarray. 
        dpi = max(dpi + num, num)
        res = max(dpi, res)
    
    return res


if __name__ == "__main__":
    nums = [-2,1,-3,4,-1,2,1,-5,4]
    print(max_subarray(nums))

    nums = [1]
    print(max_subarray(nums))

    nums = [5,4,-1,7,8]
    print(max_subarray(nums))