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


def length_of_lis_dp(nums: list) -> int:
    """ Dynamic Programming

    Longest Increasing Subsequence (LIS)

    State definition:
    dp[i] - the length of longest increasing sub-sequence until (including) 
    node j.
    dp[i] 表示以 nums[i] 这个数结尾的最长递增子序列的长度。

    Initilization:
    All numbers in the DP state array shall be 1, meaning only contain itself
    as the length of sub-sequence.

    State transition equation:
    dp[i] = max{ dp[j] | j ∈ [0,i - 1]} + 1, where nums[j] < nums[i].

    举例而言，如果我们有数组 [1, 4, 3, 4, 2, 3]，此时要计算 dp[5]（值为 3），既然是
    递增子序列，我们只要找到前面那些结尾比 3 小的子序列，然后把 3 接到最后，就可以形成一
    个新的递增子序列，而且这个新的子序列长度加一。

    可能形成很多种新的子序列，但是我们只选择最长的那一个，把最长子序列的长度作为 dp[5] 
    的值即可。

    Result:
    According to the definition, the result is the maximum of the dp array.
    ``` Python
    res = 0
    for in in range(len(dp)):
        res = max(res, dp[i])
    return res

    Time Complexity - O(N^2) - Two nested for-loops.
    Space Complexity - O(N) - For DP state array.
    ```
    """
    # Edge cases
    if not nums: return 0

    n = len(nums)
    # DP state array and initialization.
    dp = [1] * n
    # Variable to store the maximum length.
    res = 1

    for i in range(n):
        for j in range(i):
            # Check if nums[j] < nums[i] to keep increasing.
            if nums[j] < nums[i]:
                dp[i] = max(dp[i], dp[j] + 1)
        # Memorize the maximum along the way.
        res = max(res, dp[i])

    return res

def length_of_lis_bs(nums: list) -> int:
    """ Binary Search

    Longest Increasing Subsequence (LIS)

    Using an array to track the LIS, for each new element from the array, 
    we try to insert the element into LIS, where we find the first number 
    larger than it, and replace the number with the new element. To find 
    the place to replace the element, we can use binary search whose time 
    complexity is O(logN). If the replacement index is at the end of the 
    array, we can just append the new element into the array.

    Time Complexity - O(N*logN) - One outer loop and bianry search.
    Space Complexity - O(N) - For the LIS array.
    """
    def bisect_left(array, target):
        """ Binary Search - Finding the left bound to insert target. """ 
        left, right = 0, len(array)

        while left < right:
            mid = (left + right) // 2
            if array[mid] > target:
                right = mid
            elif array[mid] < target:
                left = mid + 1
            else:
                right = mid
        
        return left

    # LIS array
    lis = []

    for index, num in enumerate(nums):
        # Get the position to insert the number.
        # from bisect import bisect_left
        pos = bisect_left(lis, num)
        
        # If the position is at the end, we just append the new element 
        # into the array.
        if pos == len(lis):
            lis.append(num)
        # Otherwise, replace the number on the index with the new element.
        else:
            lis[pos] = num

    return len(lis)


if __name__ == "__main__":
    nums = [10, 9, 2, 5, 3, 7, 101, 18, 20]
    print(length_of_lis_dp(nums))
    print(length_of_lis_bs(nums))

    nums = [7,7,7,7,7,7,7]
    print(length_of_lis_dp(nums))
    print(length_of_lis_bs(nums))