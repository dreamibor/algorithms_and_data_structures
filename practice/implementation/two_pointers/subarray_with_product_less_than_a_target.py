"""
Two pointers - Subarrays with Product Less than a Target (medium)

Description:
Given an array with positive numbers and a target number, find all of its contiguous 
subarrays whose product is less than the target number.

Example:
Input: [2, 5, 3, 10], target=30 
Output: [2], [5], [2, 5], [3], [5, 3], [10]
Explanation: There are six contiguous subarrays whose product is less than the target.

Notes:
1. The subarrays shall be continuous.
2. The input array is not sorted.

Time Complexity - O(N^2) - Managing sliding window takes O(N), creating sub-arrays takes
another O(N), so in total, O(N^2).
Space Complexity - O(N) - Ignoring the space for output list, the temp list takes O(N).

LeetCode link: https://leetcode-cn.com/problems/subarray-product-less-than-k/
"""


def subarray_product_less_than_target(arr:list, target:int) -> list:
    # Edge cases
    if target <= 1: return []
    if not arr: return []

    result = []
    cur_prod = 1
    left = 0

    for right in range(len(arr)):
        cur_prod *= arr[right]

        while cur_prod >= target and left < len(arr):
            cur_prod /= arr[left]
            left += 1
        
        # Since the product of all numbers from left to right is smaller than 
        # the target, so all subarrays from left to right will have a product
        # less than the target as well.
        for i in range(left, right+1):
            result.append(arr[i:right+1])

        # Another method to add those subarrays.
        # We can't use list as temp here, as a temp list will change with
        # more values into it.

        # from collections import deque
        # temp_list = deque()
        # for i in range(right, left-1, -1):
        #     temp_list.appendleft(arr[i])
        #     result.append(list(temp_list))

    return result


def subarray_count_product_less_than_target(arr:list, target:int) -> int:
    """ Returning subarrays' count
    Time Complexity - O(N) - only iterate from left to right once.
    Space Complexity - O(1)
    """
    # Edge cases
    if target <= 1: return 0
    if not arr: return

    count = 0
    product = 1
    left = 0

    for right in range(len(arr)):
        # Cumulative product
        product *= arr[right]

        # While product is larger than the target, shrink the window.
        while product >= target:
            product /= arr[left]
            left += 1
        
        # From left to right, all subarrays shall be counted. For example:
        # For [1,2,3,4], there are four subarrays: [1,2,3,4], [2,3,4], [3,4]
        # and [4], so it shall be right-left+1=3-0+1=4.
        count += right - left + 1

    return count


if __name__ == "__main__":
    # For returning subarrays
    print(subarray_product_less_than_target([2, 5, 3, 10], 30))
    print(subarray_product_less_than_target([8, 2, 6, 5], 50))
    # For returning subarrays' count
    print(subarray_count_product_less_than_target([2, 5, 3, 10], 30))
    print(subarray_count_product_less_than_target([8, 2, 6, 5], 50))
    print(subarray_count_product_less_than_target([10,5,2,6], 100)) 