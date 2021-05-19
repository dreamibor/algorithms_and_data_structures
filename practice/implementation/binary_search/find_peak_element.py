"""
Binary Search - Find Peak Element (medium)

Description:
A peak element is an element that is strictly greater than its neighbors.

Given an integer array nums, find a peak element, and return its index. If 
the array contains multiple peaks, return the index to any of the peaks.

You may imagine that nums[-1] = nums[n] = -∞.

You must write an algorithm that runs in O(logn) time.

Example:
Input: nums = [1,2,3,1]
Output: 2
Explanation: 3 is a peak element and your function should return the index 
number 2.

LeetCode: https://leetcode-cn.com/problems/find-peak-element/
"""

def find_peak(nums: list) -> int:
    """ Linear Traverse

    Fact: any two adjacent elements will not equal. With this fact, we can 
    iterate the array from beginning, and whenever we found that nums[i] > 
    nums[i+1],we can return i, as it's a peak.

    We can understand this problem with three situations:
    1. If all the numbers are organized as decending order, then the first 
    element will be the peak. When we check the current value will be larger
    than the next element, the first element already meet the requirement.
    2. If all the numbers are organized as increasing order, then the last 
    element will be the peak. 
    3. If peak is the middle of the array, then when we check the increasing 
    part, it will be the same as situation 2, when we reached to the point of 
    the peak, nums[i] > nums[i+1]. We don't need to compare nums[i] and 
    nums[i-1] as if we can iterate until here already improves that there is 
    no pairs before meet the requirement of nums[i] > nums[i+1]. 

    Time Complexity - O(N) - Iterate the array once.
    Space Complexity - O(1) - Constant space.
    """
    for i, num in enumerate(nums):
        if num > nums[i+1]:
            return i
    
    return len(nums) - 1


def find_peak_bs(nums: list) -> int:
    """ Binary Search

    We can treat all the elements in the array as a combination of increasing 
    or descending sub-array. We can then use binary search to find the peak.

    Firstly, we will find the middile element with index mid.

    Then if the element is in a descending sequence, it means the peak will 
    be at the left side of mid, we shal shrink the search space to be the 
    left size of mid (including mid).

    Otehrwise, if the element is in a increasing sequence, then the peak will 
    be on the right of mid (from mid + 1). mid is apparently not the peak as 
    it's smaller than nums[mid + 1]. We can search the right side of mid and 
    repeat the process.

    Time Complexity - O(logN) - For binary search.
    Space Complexity - O(1) - Constant Space.
    """
    left, right = 0, len(nums) - 1

    while left < right:
        mid = (left+ right) // 2

        # Found a peak
        if nums[mid - 1] > nums[mid] < nums[mid + 1]:
            return mid
        # mid in a decreasing sequence, peak on the left (including mid).
        elif nums[mid] > nums[mid + 1]:
            right = mid
        # mid in a increasing sequence, peak on the right.
        else:
            left = mid + 1
    
    return left


if __name__ == "__main__":
    nums = [1,2,3,1]
    print(find_peak(nums))
    print(find_peak_bs(nums))