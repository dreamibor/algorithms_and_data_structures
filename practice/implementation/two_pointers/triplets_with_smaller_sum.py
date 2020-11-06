"""
Two pointers - Triplets with Smaller Sum (medium)

Description:
Given an array `arr` of unsorted numbers and a target sum, count all triplets in it 
such that arr[i] + arr[j] + arr[k] < target where i, j, and k are three different 
indices. Write a function to return the count of such triplets.

Example:
Input: [-1, 0, 2, 3], target=3 
Output: 2
Explanation: There are two triplets whose sum is less than 
the target: [-1, 0, 3], [-1, 0, 2].

Notes:
1. The array is unsorted.
2. There are negative numbers in the array.

Time Complexity - O(N^2) - N is the total number of elements in the given array. 
Sorting the array will take O(N*logN). Searching triplets will take O(N^2), so in 
total it will be O(N*logN + N^2), it's asymptotically equivalent to O(N^2).
Space Complexity - O(N) - space required for sorting, here ignored the space needed for 
saving result.

LeetCode link: https://leetcode-cn.com/problems/3sum-smaller/
"""


def triplet_with_smaller_sum(arr:list, target:int) -> int:
    # Edge cases
    if len(arr) < 3: return 0

    # Count for smaller triplets
    count = 0

    # Sort the array
    arr.sort()

    # Search triplets
    for i in range(len(arr)):
        left = i + 1
        right = len(arr) - 1

        while left < right:
            current_sum = arr[i] + arr[left] + arr[right]
            
            # Found a triplet
            if current_sum < target:
                # Trick here: since arr[right] >= arr[left], we can replace arr[right] by
                # any number between left and right to get a sum less than the target sum.
                count += right - left
                left += 1
            else:
                right -= 1

    return count

""" Similar Problem:
Write a function to return the list of all such triplets instead of the count. How 
will the time complexity change in this case?

Solution:
Following a similar approach we can create a list containing all the triplets. 

Time Complexity - O(N^3) - N is the total number of elements in the given array. 
Sorting the array will take O(N*logN). Searching triplets will take O(N^3), so in 
total it will be O(N*logN + N^3), it's asymptotically equivalent to O(N^3).
Space Complexity - O(N) - space required for sorting, here ignored the space needed for 
saving result.
"""

def triplets_with_smaller_sum(arr:list, target:int) -> int:
    # Edge cases
    if len(arr) < 3: return []

    result = []

    # Sort the array
    arr.sort()

    for i in range(len(arr)):
        left = i + 1
        right = len(arr) - 1

        while left < right:
            cur_sum = arr[i] + arr[left] + arr[right]

            if cur_sum < target:
                for k in range(left+1, right+1):
                    result.append([arr[i], arr[left], arr[k]])
                left += 1
            else:
                right -= 1

    return result





if __name__ == "__main__":
    # For returning the count.
    print(triplet_with_smaller_sum([-1, 0, 2, 3], 3))
    print(triplet_with_smaller_sum([-1, 4, 2, 1, 3], 5))
    # Expected 151
    print(triplet_with_smaller_sum([3,2,-2,6,2,-2,6,-2,-4,2,3,0,4,4,1], 3))

    # For returning the triplets array.
    print(triplets_with_smaller_sum([-1, 0, 2, 3], 3))
    print(triplets_with_smaller_sum([-1, 4, 2, 1, 3], 5))
    print(triplets_with_smaller_sum([3,2,-2,6,2,-2,6,-2,-4,2,3,0,4,4,1], 3))


