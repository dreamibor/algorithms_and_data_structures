"""
Grokking the Coding Interview: Patterns for Coding Questions
Smallest Subarray with a given sum (easy)

Given an array of positive numbers and a positive number ‘S’,
find the length of the smallest contiguous subarray whose sum
is greater than or equal to ‘S’. Return 0, if no such subarray exists.

Input: [2, 1, 5, 2, 3, 2], S=7
Output: 2
Explanation: The smallest subarray with a sum great than or equal to '7' is [5, 2].
"""


def smallest_subarray_with_given_sum(arr, s):
    collection = []
    for window_size in range(1, len(arr) + 1):
        window_sum = 0
        window_start = 0

        for window_end in range(len(arr)):
            window_sum += arr[window_end]
            if window_end >= (window_size - 1):
                if window_sum >= s:
                    return window_size
                window_sum -= arr[window_start]
                window_start += 1

    return 0


result = smallest_subarray_with_given_sum([2, 1, 5, 2, 3, 2], 7)
print(result)
