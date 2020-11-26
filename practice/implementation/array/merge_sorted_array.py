"""
Array - Merge Sorted Array (easy)

Description:
Given two sorted integer arrays nums1 and nums2, merge 
nums2 into nums1 as one sorted array.

Note:
- Do not return anything, modify nums1 in-place instead.
- The number of elements initialized in nums1 and nums2 are m and n 
respectively.
- You may assume that nums1 has enough space (size that is equal to m + n) 
to hold additional elements from nums2.

Example:
Input:
nums1 = [1,2,3,0,0,0], m = 3
nums2 = [2,5,6],       n = 3

Output: [1,2,2,3,5,6]

LeetCode Link: https://leetcode-cn.com/problems/merge-sorted-array/
"""

def merge_sorted_array(nums1: list, m: int, nums2: list, n: int) -> None:
    """ Merge and Sort
    The most naive method could be merge the two arrays and then sort.
    
    Time Complexity - O((N+M)*log(N+M)) - For sorting after merge.
    Space Complexity - O(1) - If not considering space for sorting.
    """

    # Move all values in nums2 to nums1.
    for i in range(n):
        nums1[m+i] = nums2[i]

    # Sort nums1
    nums1.sort()

    print(nums1)

def merge_two_pointer_front_to_back(nums1: list, m: int, nums2: list, n: int) -> None:
    """ Two Pointers
    We can use two pointers to merge nums2 into nums1. Since nums1 is the 
    output array, we need to save all m elements in nums1 in another place 
    which will require O(m) space.

    Time Complexity - O(N+M) - Iterate through nums1 and nums2 once.
    Space Complexity - O(M) - For the copy of nums1.
    """
    # Make a copy of nums1
    nums1_copy = nums1[:m]

    # Three pointers for getting nums1_copy, nums2, and nums1.
    p1 = 0
    p2 = 0
    p3 = 0
    
    # Compare elements from nums1_copy and nums2, add the smallest
    # one into nums1.
    while p1 < m and p2 < n:
        if nums1_copy[p1] < nums2[p2]:
            nums1[p3] = nums1_copy[p1]
            p1 += 1
        else:
            nums1[p3] = nums2[p2]
            p2 += 1
        p3 += 1

    # For remaining elements in nums1_copy or nums2.
    if p1 < m:
        nums1[p1 + p2:] = nums1_copy[p1:]
    if p2 < n:
        nums1[p1 + p2:] = nums2[p2:]

    print(nums1)

def merge_two_pointer_back_to_front(nums1: list, m: int, nums2: list, n: int) -> None:
    """ Two Pointers From Backward
    We can change values of nums1 from backward since there are 
    n zeros after m elements.

    Time Complexity - O(N+M) - Iterate through nums1 and nums2 once.
    Space Complexity - O(M) - Only for pointers.
    """
    # Pointer for nums1 from backward.
    p = m + n - 1
    # Pointers for nums1 and nums2.
    p1 = m - 1 
    p2 = n - 1

    while p1 >= 0 and p2 >= 0:
        if nums1[p1] < nums2[p2]:
            nums1[p] = nums2[p2]
            p2 -= 1
        else:
            nums1[p] = nums1[p1]
            p1 -= 1
        p -= 1
    
    if p2 >= 0:
        nums1[:p2 + 1] = nums2[:p2 + 1]

    print(nums1)


if __name__ == "__main__":
    nums1 = [1,2,3,0,0,0]
    nums2 = [2,5,6]
    merge_sorted_array(nums1, 3, nums2, 3)
    nums1 = [1,2,3,0,0,0]
    nums2 = [2,5,6]
    merge_two_pointer_front_to_back(nums1, 3, nums2, 3)
    nums1 = [1,2,3,0,0,0]
    nums2 = [2,5,6]
    merge_two_pointer_back_to_front(nums1, 3, nums2, 3)