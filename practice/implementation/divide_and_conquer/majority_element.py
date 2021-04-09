"""
Hash Table / Divide and Conquer - Majority Element

Description:
Given an array nums of size n, return the majority element.

The majority element is the element that appears more than ⌊n / 2⌋ times. 
You may assume that the majority element always exists in the array.

Example:
Input: nums = [3,2,3]
Output: 3

Follow-up: Could you solve the problem in linear time and in O(1) space?

LeetCode: https://leetcode-cn.com/problems/majority-element/
"""
from collections import defaultdict, Counter


def majority_element_hash_map(nums: list) -> int:
    """ Count the elements with hash map and return the number with the 
    largest frequerncy.

    Time Complexity - O(N) - Iterate the array and hash map once.
    Space Complexity - O(N) - For storing hash map.
    """
    # counts = Counter(nums)
    # # return counts.most_common()[0][0]
    # return max(counts, key=counts.get)

    frequency = defaultdict(int)

    for num in nums:
        frequency[num] += 1 

    return max(frequency, key = lambda x: frequency[x]) # max(frequency, key=frequency.get)

def majority_element_sort(nums: list) -> int:
    """ Sort and return the middle number.
    
    Time Complexity - O(N*logN) - For sorting the array.
    Space Complexity - O(1) - Constant space ignoring the space required by sorting.
    """
    nums.sort()
    return nums[len(nums) // 2]

def majority_element_daq(nums: list) -> int:
    """ Divide and Conquer

    If a is the majority of nums, then if we split nums into two halves, then a 
    will be the model of at least of one half.

    Time Complexity - O(N*logN) - For each array, we split it into two sub-problems 
    and scanning the array twice, so the time complexity will be:
    T(n) = 2T(n/2) + 2n, which based on the [master therom case 2](https://en.wikipedia.org
    /wiki/Master_theorem_(analysis_of_algorithms)#Case_2_example), the time complexity 
    will be equal to O(N*logN).

    Space Complexity - O(logN) - For recursion stack.
    """
    def helper(low, high) -> int:
        # Base case, there is only one element in the array and it's the majority.
        if low == high:
            return nums[low]
        
        # Recursion on left and right halves.
        mid = (high - low) // 2 + low
        left = helper(low, mid)
        right = helper(mid + 1, high)

        # If the two halves agree on the majprity, then return it.
        if left == right:
            return left
        
        # Otherwise, count each element and return the winner.
        left_count = sum(1 for i in range(low, high + 1) if nums[i] == left)
        right_count = sum(1 for i in range(low, high + 1) if nums[i] ==right)

        return left if left_count > right_count else right

    return helper(0, len(nums) - 1)


if __name__ == "__main__":
    # Hash map
    nums = [2,2,1,1,1,1,1,2,2]
    majority = majority_element_hash_map(nums)
    print(majority)

    # Sort
    nums = [2,2,1,1,1,1,1,2,2]
    majority = majority_element_sort(nums)
    print(majority)

    # Divide and Conquer
    nums = [2,2,1,1,1,1,1,2,2]
    majority = majority_element_daq(nums)
    print(majority)
