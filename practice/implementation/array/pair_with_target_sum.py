"""
Two pointers - Pair with Target Sum (easy)

Description:
Given an array of sorted numbers and a target sum, find all the pairs in the array 
whose sum is equal to the given target.
The solution set must not contain duplicate pairs.

Example:
Input: [1, 2, 3, 4, 6], target=6
Output: [[1, 3]]

Notes:
1. The array shall be sorted.
2. The solution shall not contain duplicates.

LeetCode link: https://leetcode-cn.com/problems/he-wei-sde-liang-ge-shu-zi-lcof/
"""

def two_sum(nums:list, target:int) -> list:
    """ Two Pointers
    When the array is sorted, we can use two pointers to find 
    the pairs. But to avoid duplicates, we need to move pointers 
    to skip same elements in the array.

    Time Complexity - O(N*logN) - For sorting.
    Space Complexity - O(1) - For pointers.
    """
    result = []

    # Sort the array
    nums.sort()

    left = 0
    right = len(nums) - 1

    while left < right:
        cur_sum = nums[left] + nums[right]
        if cur_sum == target:
            # If we sum == target, append it to result.
            # Move left and right pointer
            result.append([nums[left], nums[right]])
            left += 1
            right -= 1
            while left < right and nums[left] == nums[left-1]:
                left += 1
            while left < right and nums[right] == nums[right+1]:
                right -= 1
        elif cur_sum < target:
            # Since sum is smaller than target, we need a larger
            # number, so increase left.
            left += 1
            while left < right and nums[left] == nums[left-1]:
                left += 1
        else:
            # Since sum is larger than target, we need a smaller
            # number, so decrease right.
            right -= 1
            while left < right and nums[right] == nums[right+1]:
                right -= 1

    return result


if __name__ == "__main__":
    nums =  [1,1,1,2,2,3,3]
    result = two_sum(nums, target=4)
    print(result)

    nums =  [0,0,0,0,0,0]
    result = two_sum(nums, target=0)
    print(result)