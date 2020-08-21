"""
Grokking the Coding Interview: Patterns for Coding Questions
Sliding window - Introduction

Description: Given an array, find the average of all contiguous subarrays of size K in it.

Example: 
Input: [1, 3, 2, 6, -1, 4, 1, 8, 2], K=5
Output: [2.2, 2.8, 2.4, 3.6, 2.8]

Time Complexity - O(N)
Space Complexity - O(N)
"""


def calculate_averages_of_subarrays(array, k):
    result = [] # Store results
    window_sum = 0. # Current window sum
    window_start = 0 # Window start index

    for window_end in range(len(array)):
        window_sum += array[window_end] # Add window end index's number

        if window_end >= k-1: # Assuming index (0, 1), k = 2; so it will be window end (1) >= k - 1.
            result.append(window_sum / k) # Add average number to the result list
            window_sum -= array[window_start] # Remove window start index number, to shift the window
            window_start += 1 # Increase window start 
    
    return result


if __name__ == "__main__":
    result = calculate_averages_of_subarrays([1, 3, 2, 6, -1, 4, 1, 8, 2], k=5)
    print(result)
