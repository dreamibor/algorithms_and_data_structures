"""
Two pointers - Four Sum (medium)

Description:
Given an array `nums` of n integers and an integer `target`, are there elements 
a, b, c, and d in nums such that a + b + c + d = target? Find all unique 
quadruplets in the array which gives the sum of target.

Notice that the solution set must not contain duplicate quadruplets.

Example:
Input: nums = [1,0,-1,0,-2,2], target = 0
Output: [[-2,-1,1,2],[-2,0,0,2],[-1,0,0,1]]

Notes:
1. The array is not sorted.
2. We need to find all unique triplets, so we have to skip any duplicate numbers.

Reference:
https://leetcode-cn.com/problems/3sum/solution/yi-ge-fang-fa-tuan-mie-by-labuladong/

LeetCode link: https://leetcode-cn.com/problems/4sum
"""

def four_sum(nums: list, target: int) -> list:
    """ Two Pointers - Based on Three Sum (Two Sum Pairs)
    
    The target is to find a triplet a + b + c + d = target.

    We can sort the array first, and the fix one number (a) on the left, scanning 
    numbers on the right side of the array using the same technique as in Two Sum 
    Pairs problem.

    Time Complexity - O(N^3) - N is the total number of elements in the given array.
    Sorting the array will take O(N*logN). Searching for triplets will take O(N^2), 
    and searching for pairs will tale O(N), we are searching triplets for each element 
    in the array, so in total the time complexity will be O(N*logN + N^2), and it's 
    asymptotically equivalent to O(N^3).

    Space Complexity - O(N) - space required for sorting, ignore the space needed for 
    saving result.
    """
    arr_len = len(nums)

    # Edge case - array has less than 4 elements.
    if arr_len < 4: return []

    result = []

    # Sort the array, O(N*logN)
    nums.sort()

    for i in range(arr_len - 3):
        # Remove duplicates for `a`.
        if i > 0 and nums[i] == nums[i-1]: continue

        for j in range(i+1, arr_len - 2):
            # Remove duplicates for `b`, be careful it's 
            # j > i + 1 rather than j > 0, otherwise, it 
            # will fail for case [0, 0, 0, 0].
            if j > i+1 and nums[j] == nums[j-1]: continue

            left = j + 1
            right = arr_len - 1

            # Begin searching for pairs with two pointers.
            while left < right:
                cur_sum = nums[i] + nums[j] + nums[left] + nums[right]

                if cur_sum == target:
                    result.append([nums[i], nums[j], nums[left], nums[right]])

                    # Move both left and right one step further.
                    left += 1
                    right -= 1

                    # Skip duplicates for left and right.
                    while left < right and nums[left] == nums[left - 1]:
                        left += 1
                    
                    while left < right and nums[right] == nums[right + 1]:
                        right -= 1
                elif cur_sum < target:
                    # Move left forward as we need a larger sum.
                    left += 1
                    while left < right and nums[left] == nums[left - 1]:
                        left += 1
                else:
                    # Move right backward as we need a smaller sum.
                    right -= 1
                    while left < right and nums[right] == nums[right + 1]:
                        right -= 1
    
    return result


if __name__ == "__main__":
    nums = [1,0,-1,0,-2,2]
    result = four_sum(nums, target=0)
    print(result)

    nums = [0,0,0,0]
    result = four_sum(nums, target=0)
    print(result)

