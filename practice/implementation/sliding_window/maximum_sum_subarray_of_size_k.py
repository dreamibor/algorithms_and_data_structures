"""
Grokking the Coding Interview: Patterns for Coding Questions
Sliding window - Maximum Sum Subarray of Size K (easy)

Description: Given an array of positive numbers and a positive number ‘k’, find the maximum sum of any contiguous subarray of size ‘k’.

Example:
Input: [2, 1, 5, 1, 3, 2], k=3
Output: 9
Explanation: Subarray with maximum sum is [5, 1, 3].

Time Complexity - O(N)
Space Complexity - O(1)
"""


def maximum_sum_subarray_of_size_k(arr, k):
    maximum = -1 # Return -1 for edge cases (less than k elements)
    window_start = 0
    current_sum = 0

    for window_end in range(len(arr)):
        current_sum += arr[window_end]

        if window_end >= k-1:
            if current_sum > maximum:
                maximum = current_sum # maximum = max(current_sum, maximum)
            current_sum -= arr[window_start]
            window_start += 1

    return maximum


if __name__ == "__main__":
    maximum = maximum_sum_subarray_of_size_k([2, 1, 3, 5, 1, 3, 2], k=3)
    print(maximum)