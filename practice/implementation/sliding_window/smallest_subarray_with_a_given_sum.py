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

LeetCode link: https://leetcode-cn.com/problems/minimum-size-subarray-sum/
"""
import bisect


def smallest_subarray_with_given_sum(s, arr):
    """ Sliding window or two pointers.
    """
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


def minimum_size_subarray_sum(s, arr):
    """ Prefix sum + binary search
    A naive method is to fix a left index i, and then find a minimum j 
    so that the sum from i to j will be >= s and the window size will 
    be 'j - i + 1'. However, the time complexity will be O(N^2).

    We can optimise this method by using binary search to find j.

    To use binary search, we need to create an extra array 'prefix_sums' 
    to store the prefix sums of 'arr', where prefix_sums[i] means the sum
    from arr[0] to arr[i-1].

    Once we have the prefix sums, we can the use binart search to find the
    minimum 'bound' for starting index i, where 
    prefix_sums[bound] - prefix_sums[i-1] >= s, and then update the minimum length
    as 'bound - (i - 1)'.

    Note: In this problem, all elements are positive, so the prefix sums are
    increasing, and this guarantee we can use binary search.

    Time Complexity - O(N*logN)
    Space Complexity - O(N)
    """
    if not arr:
        return 0
    
    min_len = len(arr) + 1
    prefix_sums = [0]

    # Get the prefix sums array for input array.
    for i in range(len(arr)):
        prefix_sums.append(prefix_sums[-1] + arr[i])
    
    for i in range(1, len(arr)+1):
        target = s + prefix_sums[i - 1]
        # Binary search for index where
        # prefix_sums[bound] >= target + prefix_sums[i - 1]
        bound = bisect.bisect_left(prefix_sums, target)
        if bound != len(prefix_sums):
            min_len = min(min_len, bound - (i - 1))

    return 0 if min_len == len(arr) + 1 else min_len


if __name__=="__main__":
    print("Smallest subarray length: " + str(smallest_subarray_with_given_sum(7, [2, 1, 5, 2, 3, 2])))
    print("Smallest subarray length: " + str(smallest_subarray_with_given_sum(7, [2, 1, 5, 2, 8])))
    print("Smallest subarray length: " + str(smallest_subarray_with_given_sum(8, [3, 4, 1, 1, 6])))
    print("Smallest subarray length: " + str(minimum_size_subarray_sum(7, [2, 1, 5, 2, 3, 2])))
    print("Smallest subarray length: " + str(minimum_size_subarray_sum(7, [2, 1, 5, 2, 8])))
    print("Smallest subarray length: " + str(minimum_size_subarray_sum(8, [3, 4, 1, 1, 6])))