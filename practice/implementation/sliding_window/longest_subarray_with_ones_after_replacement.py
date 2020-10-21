"""
Sliding window - Longest Subarray with Ones after Replacement (hard)

Description:
Given an array containing 0s and 1s, if you are allowed to replace no more than ‘k’ 0s with 1s, find the length of the longest contiguous subarray having all 1s.

Input: Array=[0, 1, 1, 0, 0, 0, 1, 1, 0, 1, 1], k=2
Output: 6
Explanation: Replace the '0' at index 5 and 8 to have the longest contiguous subarray of 1s having length 6.

Time Complexity - O(N)
Space Complexity - O(1)

LeetCode link (Similar): https://leetcode-cn.com/problems/longest-subarray-of-1s-after-deleting-one-element/
"""


def length_of_longest_subarray(arr, k):
    window_start = 0
    max_ones_count = 0
    max_length = 0

    for window_end in range(len(arr)):
        if arr[window_end] == 1:
            max_ones_count += 1

        if (window_end - window_start + 1 - max_ones_count) > k:
            if arr[window_start] == 1:
                max_ones_count -=1
            window_start += 1
        max_length = max(max_length, window_end - window_start + 1)

    return max_length


if __name__ == "__main__":
  print(f"Length of the longest subarray {length_of_longest_subarray([0, 1, 1, 0, 0, 0, 1, 1, 0, 1, 1], 2)}")
  print(f"Length of the longest subarray {length_of_longest_subarray([0, 1, 0, 0, 1, 1, 0, 1, 1, 0, 0, 1, 1], 3)}")

