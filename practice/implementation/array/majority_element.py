"""
Array - Majority Element (easy)

Description:
Given an array of size n, find the majority element. The majority element is the 
element that appears more than ⌊ n/2 ⌋ times.

You may assume that the array is non-empty and the majority element always exist 
in the array.

Example:
Input: [3,2,3]
Output: 3

LeetCode Link: https://leetcode.com/problems/majority-element/
"""

def majority_element_hash_table(nums: list) -> int:
    """ Hash Table
    Time Complexity - O(N) - Iterate through array.
    Space Complexity - O(N) - for hash table.

    We can also using Counter in Python:
        counts = collections.Counter(nums)
        return max(counts.keys(), key=counts.get)
    """
    frequency = {}
    
    for num in nums:
        if num not in frequency:
            frequency[num] = 0
        frequency[num] += 1
    
    for key, value in frequency.items():
        if value > len(nums) // 2:
            return key

def majority_element_sort(nums: list) -> int:
    """ Sort
    If we sort the array (increasing or decreasing), then the element 
    at N//2 will must be the mode.

    Time Complexity - O(N*logN) - For sorting.
    Space Complexity - O(logN) - For the recursion stack space that 
    the sorting algorithm used.
    """
    nums.sort()
    return nums[len(nums) // 2]

def majority_element_divide_and_conquer(nums: list, low=0, high=None) -> int:
    """ Divide and Conquer
    If a is the mode of nums, then if wen split nums into two parts, 
    a must be the mode of at least one of the two parts. 
    
    To prove this, we can use proof by contradiction. 
    Suppose a is not the mode of the left part, neither the mode of the 
    right part, then the times of a appeared is less than l/2 + r/2, where 
    l and r are the length of the left part and the right part. Since 
    l/2 + r/2 <= (l+r)/2, then a will not be the mode for the whole array.

    So we can use divide and conquer to solve this problem: split the array 
    into two parts, get the mode of left and right part, and compare which 
    one appeared more times.

    Time Complexity - O(N*logN) - Each time split the problem into two parts.
    Space Complexity - O(logN) - For recursion.
    """
    def majority_element_recursion(nums, low, high):
        if low == high:
            return nums[low]

        mid = (high - low) // 2 + low
        left = majority_element_recursion(nums, low, mid)
        right = majority_element_recursion(nums, mid+1, high)

        if left == right: return left

        left_count = sum(1 for i in range(low, high+1) if nums[i] == left)
        right_count = sum(1 for i in range(low, high+1) if nums[i] == right)

        return left if left_count > right_count else right
    
    return majority_element_recursion(nums, 0, len(nums) - 1)


def majority_element_voting(nums: list) -> int:
    """ Boyer-Moore Voting
    If we count the mode as +1 while others as -1, if we add them 
    together, the sum is apprently larger than 0.

    The steps for Boyer-Moore Voting algorithm:
    1. We have a variable called candiate and it's count. Initially, 
    candidate could be any value while count is 0.
    2. We iterate through the array, for each element x, if count is 
    0 then we assign x to candidate, and see if x:
        - if x == candidate, then count +1;
        - if x != candidate, then count -1.
    3. After the traversal, candidate will be the mode.

    Time Complexity - O(N) - Only iterate the array once.
    Space Complexity - O(1) - Constant space.
    """
    candidate = None
    count = 0

    for num in nums:
        if count == 0:
            candidate = num
        
        count += (1 if num == candidate else -1)

    return candidate


if __name__ == "__main__":
    nums = [2,2,1,1,1,2,2]
    print(f"Majority element: {majority_element_hash_table(nums)}")

    nums = [2,2,1,1,1,2,2]
    print(f"Majority element: {majority_element_sort(nums)}")

    nums = [2,2,1,1,1,2,2]
    print(f"Majority element: {majority_element_divide_and_conquer(nums)}")

    nums = [2,2,1,1,1,2,2]
    print(f"Majority element: {majority_element_voting(nums)}")



