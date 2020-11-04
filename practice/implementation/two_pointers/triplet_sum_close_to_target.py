"""
Two pointers - Triplet Sum Close to Target (medium)

Description:
Given an array of unsorted numbers and a target number, find a triplet in the 
array whose sum is as close to the target number as possible, return the sum 
of the triplet. If there are more than one such triplet, return the sum of the 
triplet with the smallest sum.

Example:
Input: [-2, 0, 1, 2], target=2
Output: 1
Explanation: The triplet [-2, 1, 2] has the closest sum to the target.

Notes:
1. The array is unsorted.
2. There are negative numbers in the array.

Time Complexity - O(N^2) - N is the total number of elements in the given array. 
Sorting the array will take O(N*logN). Searching triplets will take O(N^2), so in 
total it will be O(N*logN + N^2), it's asymptotically equivalent to O(N^2).
Space Complexity - O(N) - space required for sorting, here ignored the space needed for 
saving result.

LeetCode link: https://leetcode-cn.com/problems/3sum-closest/
"""
import math


def triplet_sum_closest_to_target(arr:list, target:int) -> int:
    # Edge cases - array length shorter than 3.
    if len(arr) < 3:
        return -math.inf

    # The placeholder for smallest difference.
    minimum_diff = math.inf

    # Sort the array.
    arr.sort()

    for i in range(len(arr)):
        # Optimise - Avoid duplicate a (fixed in the outer loop).
        if i > 0 and arr[i] == arr[i-1]:
            continue

        # Begin pair search than are closer to targe - a.
        left = i + 1
        right = len(arr) - 1

        while left < right:
            # Difference between targer and current triplet sum.
            difference = target - arr[i] - arr[left] - arr[right]

            # If we've found a triplet's sum is exactly the target
            if difference == 0:
                # Return sum of all the numbers in the triplet.
                return target - difference
            
            # Handle the smallest sum when we have more than one solution.
            if abs(difference) < abs(minimum_diff):
            #   or (abs(difference) == abs(minimum_diff) and difference > minimum_diff):
                minimum_diff = difference
            
            if difference > 0:
                # We need a triplet with bigger sum.
                left += 1 

                # Optimise - Ignore duplicate left side values.
                while left < right and arr[left] == arr[left - 1]:
                    left += 1
            else:
                # We need a triplet with smaller sum.
                right -= 1
                
                # Optimise - Ignore duplicate right side values.
                while left < right and arr[right] == arr[right+1]:
                    right -= 1

    return target - minimum_diff


if __name__ == "__main__":
    print(triplet_sum_closest_to_target([-2, 0, 1, 2], 2))
    print(triplet_sum_closest_to_target([-3, -1, 1, 2], 1))
    print(triplet_sum_closest_to_target([1, 0, 1, 1], 100))
    print(triplet_sum_closest_to_target([1, 1, 1, 0], -100))
    