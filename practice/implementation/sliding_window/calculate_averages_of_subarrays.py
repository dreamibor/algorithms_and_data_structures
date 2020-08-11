"""
Grokking the Coding Interview: Patterns for Coding Questions
Sliding window - Introduction
Description: Given an array, find the average of all contiguous subarrays of size K in it.
Example: Array: [1, 3, 2, 6, -1, 4, 1, 8, 2], K=5
Output: [2.2, 2.8, 2.4, 3.6, 2.8]
"""


def calculate_averages_of_subarrays(array, k):
    result = []
    window_sum = 0.
    window_start = 0
    for window_end in range(len(array)):
        window_sum += array[window_end]
        if window_end >= k-1:
            result.append(window_sum / k)
            window_sum -= array[window_start]
            window_start += 1
    return result


if __name__ == "__main__":
    result = calculate_averages_of_subarrays([1, 3, 2, 6, -1, 4, 1, 8, 2], k=5)
    print(result)
