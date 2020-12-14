"""
Queue - Sliding Window Maximum (hard)

Description:
You are given an array of integers `nums`, there is a sliding window of size `k` which is 
moving from the very left of the array to the very right. You can only see the `k` numbers 
in the window. Each time the sliding window moves right by one position.

Return the max sliding window.

Follow up: could you solve the problem with linear time complexity O(N)?

Example:
Input: nums = [1,3,-1,-3,5,3,6,7], k = 3
Output: [3,3,5,5,6,7]
Explanation:
Window position                Max
--------------------------    -----
[1  3  -1] -3  5  3  6  7       3
 1 [3  -1  -3] 5  3  6  7       3
 1  3 [-1  -3  5] 3  6  7       5
 1  3  -1 [-3  5  3] 6  7       5
 1  3  -1  -3 [5  3  6] 7       6
 1  3  -1  -3  5 [3  6  7]      7

LeetCode Link: https://leetcode-cn.com/problems/sliding-window-maximum/
"""


def max_sliding_window_brute_force(nums: list, k: int) -> list:
    """ Brute Force
    Sliding the size k window through the array and append all the 
    maximum into a result array.

    Time Complexity - O(N*k) - There are N - k + 1 sliding windows in 
    total, and each window has a size of k, so in total O(Nk).
    Space Complexity - O(N-k+1) - For the output array.
    """
    result = []

    for index in range(len(nums) - k + 1):
        result.append(max(nums[index: index+k]))

    return result


def max_sliding_window_deque(nums: list, k: int) -> list:
    """ Double-ended Queue

    Time Complexity - O(N) - There are N - k + 1 sliding windows in 
    total, and each window has a size of k, so in total O(Nk).
    Space Complexity - O(N-k+1) - For the output array.
    """



if __name__ == "__main__":
    print(max_sliding_window_brute_force(nums = [1,3,-1,-3,5,3,6,7], k = 3))