"""
Two Pointers - Three Sum (medium)

Description:
The problem is also called Triplet Sum to Zero.
Given an array of unsorted numbers, find all unique triplets in it that add up to zero.

Example:
Input: [-3, 0, 1, 2, -1, 1, -2]
Output: [-3, 1, 2], [-2, 0, 2], [-2, 1, 1], [-1, 0, 1]
Explanation: There are four unique triplets whose sum is equal to zero.

Notes:
1. The array is not sorted.
2. There must be negative numbers in the array (or all zeros).
3. We need to find all unique triplets, so we have to skip any duplicate numbers.

Reference:
https://leetcode-cn.com/problems/3sum/solution/yi-ge-fang-fa-tuan-mie-by-labuladong/

LeetCode link: https://leetcode-cn.com/problems/3sum/
"""

def three_sum(nums: list, target: int) -> list:
    """ Two Pointers - Based on Two Sum Pairs

    The target is to find a triplet a + b + c = 0.

    We can sort the array first, and the fix one number (a) on the left, scanning 
    numbers on the right side of the array using the same technique as in Two Sum 
    Pairs problem.

    Time Complexity - O(N^2) - N is the total number of elements in the given array.
    Sorting the array will take O(N*logN). Searching for pairs will take O(N), and 
    we are searching pairs for each number in the input array, so in total it 
    will be O(N*logN + N^2), it's asymptotically equivalent to O(N^2).

    Space Complexity - O(N) - space required for sorting, ignore the space needed for 
    saving result.
    """
    length = len(nums)
    
    # Edge cases - nums has less than three elements.
    if length < 3: return []

    result = []

    # Sort the array, O(N*logN)
    nums.sort()

    for i in range(length - 2):
        # ONLY FOR TARGET IS ZERO.
        # If `a` is larger than 0, then it's infeasible to find b + c 
        # pairs that will meet the requirement of a + b + c = 0.
        if nums[i] > 0: break

        # Skip duplicate elements for `a`.
        if i > 0 and nums[i] == nums[i-1]: continue

        # Two pointers for searching pairs, same as in Two Sum.
        left = i + 1
        right = length - 1

        while left < right:
            cur_sum = nums[i] + nums[left] + nums[right]

            if cur_sum == target:
                result.append([nums[i], nums[left], nums[right]])

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
    print(three_sum([-3, 0, 1, 2, -1, 1, -2], 0))
    print(three_sum([-5, 2, -1, -2, 3], 0))
    print(three_sum([-1,0,1,2,-1,-4], 0))
    # All zeros
    print(three_sum([0, 0, 0, 0], 0))
    # Test edge cases
    print(three_sum([0], 0))
    print(three_sum([], 0))