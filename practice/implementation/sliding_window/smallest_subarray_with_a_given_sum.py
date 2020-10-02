"""
Sliding window - Smallest Subarray with a given sum (easy)

Description:
Given an array of positive numbers and a positive number ‘S’,
find the length of the smallest contiguous subarray whose sum
is greater than or equal to ‘S’. Return 0, if no such subarray exists.

Example：
Input: [2, 1, 5, 2, 3, 2], S=7
Output: 2
Explanation: The smallest subarray with a sum great than or equal to '7' is [5, 2].

Time Complexity - O(N)
Space Complexity - O(1)

Relevatn LeetCode link (Hard): https://leetcode.com/problems/shortest-subarray-with-sum-at-least-k/
"""

def smallest_subarray_with_given_sum(s, arr):
    window_sum = 0
    window_start = 0
    minimum_length = len(arr) + 1

    for window_end in range(len(arr)):
        window_sum += arr[window_end]

        while window_sum >= s:
            minimum_length = min(minimum_length, window_end - window_start + 1)
            window_sum -= arr[window_start]
            window_start += 1

    if minimum_length == len(arr) + 1:
        return 0
    return minimum_length


if __name__=="__main__":
    print("Smallest subarray length: " + str(smallest_subarray_with_given_sum(7, [2, 1, 5, 2, 3, 2])))
    print("Smallest subarray length: " + str(smallest_subarray_with_given_sum(7, [2, 1, 5, 2, 8])))
    print("Smallest subarray length: " + str(smallest_subarray_with_given_sum(8, [3, 4, 1, 1, 6])))