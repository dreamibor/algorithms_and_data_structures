"""
DP - Longest Increasing Subsequence (medium)

Description:
Given an integer array nums, return the length of the longest strictly 
increasing subsequence.

A subsequence is a sequence that can be derived from an array by deleting 
some or no elements without changing the order of the remaining elements. 
For example, [3,6,2,7] is a subsequence of the array [0,3,1,6,2,2,7].

Example:
Input: nums = [10,9,2,5,3,7,101,18]
Output: 4
Explanation: The longest increasing subsequence is [2,3,7,101], therefore 
the length is 4.

Follow up:
1. Could you come up with a O(n^2) solution?
2. Could you improve it to O(n*log(n)) time complexity?

LeetCode: https://leetcode-cn.com/problems/longest-increasing-subsequence
"""


def lis(nums: list) -> int:
    """ 
    Longest Increasing Subsequence (LIS)

    """

    pass



if __name__ == "__main__":
    nums = [10, 9, 2, 5, 3, 7, 101, 18]
    print(lis(nums))

    nums = [7,7,7,7,7,7,7]