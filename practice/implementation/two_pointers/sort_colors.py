"""
Two pointers - Sort Colours / Dutch National Flag Problem (medium)

Description:
Given an array containing 0s, 1s and 2s, sort the array in-place. You should treat numbers 
of the array as objects, hence, we can’t count 0s, 1s, and 2s to recreate the array.

The flag of the Netherlands consists of three colors: red, white and blue; and since our 
input array also consists of three different numbers that is why it is called Dutch National 
Flag problem. It's first proposed by computer scientist Edsger Wybe Dijkstra.

Example:
Input:  [2, 0, 2, 1, 1, 0]
Output: [0, 0, 1, 1, 2, 2]

Notes:
1. We shall modify the array in-place.

Time Complexity - O(N) - N is the total number of elements in the given array.
Space Complexity - O(1) - Constant space complexity.

LeetCode link: https://leetcode-cn.com/problems/sort-colors/
"""


def sort_colours(nums:list) -> list:
    """ Two pointers - similar to the idea of `partition` in quick sort.
    Initially, we set two pointers called `low` and `high` which are pointing at the first 
    element and the last element in the array. 
    While iterating, we will move all 0s before low and all 2s after high, so in the end, 
    all 1s will be between low and high.
    Since the high pointer is moving from right to left, so when we iterate the array from
    left to right, if we've passed the position of high, then the iteration shall stop.
    It's worthy to note that if we've found 2 and exchanged the position, we don't need to 
    increment i since the exchanged value to index i could be 0, 1 or 2, so we need to check
    it again.
    """
    low = 0
    high = len(nums) - 1

    i = 0
    while i <= high:
        if nums[i] == 0:
            nums[i], nums[low] = nums[low], nums[i]
            # Increment low and i
            low += 1
            i += 1
        elif nums[i] == 2:
            nums[i], nums[high] = nums[high], nums[i]
            # Decrement only high, since after swap, the number at index
            # i could be 0, 1, 2, so we will go through another loop.
            high -= 1
        else:
            # numss[i] == 1
            i += 1 

    return nums


if __name__ == "__main__":
    print(sort_colours([1, 0, 2, 1, 0]))
    print(sort_colours([2, 2, 0, 1, 2, 0]))
