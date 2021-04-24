"""
Binary Search - Median of Two Sorted Arrays (hard)

Given two sorted arrays nums1 and nums2 of size m and n respectively, return 
the median of the two sorted arrays.

Example:
Input: nums1 = [1,3], nums2 = [2]
Output: 2.00000
Explanation: merged array = [1,2,3] and median is 2.

Follow up: The overall run time complexity should be O(log (m+n)).

LeetCode: https://leetcode-cn.com/problems/median-of-two-sorted-arrays/
"""


def find_median(nums1: list, nums2: list) -> float:
    """ Binary Search

    According to the definition of median, assuming the length of the two 
    arrays are `m` and `n`, when `m + n` is odd, the median will be the 
    element at index of (m+n)/2. When `m+n` is even, then the median will 
    be the average of numbers at (m+n)/2 and (m+n)/2+1.

    The problem can be trasferred to finding the k_th smallest number in 
    the two given sorted arrays, where k is (m+n)/2 or (m+n)/2 + 1.
    """
    pass



if __name__ == "__main__":
    nums1, nums2 = [1,3], [2]
    res = find_median(nums1, nums2)