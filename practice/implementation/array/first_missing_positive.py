"""
Array - First Missing Positive (hard)

Description:
Given an unsorted integer array nums, find the smallest missing positive integer.

Follow up: 
Could you implement an algorithm that runs in O(n) time and uses constant extra space?

Example:
Input: nums = [1,2,0]
Output: 3

Solutions:
1. Hash table, we can store all the elements in the array into a hash table, and then 
enumerating all positive numbers and check if they are in the hash table. The time 
complexity will be O(N) and space complexity will be O(N).

2. Traverse array, we can enumerating all positive numbers and then check if it's in 
the array by traversal. The time complexity will be O(N^2) while the space complexity 
will be O(1).

Bear in mind that if we can't modify the original array, then it's infeasible to meet 
the requirement of O(N) time and O(1) space.

3. In-place hash table (using array), we can use the given array as a replacement of a 
hash table. 
For a given array with length N, the smallest missing positive value will must be within 
[1, N+1], where if [1, N] all appeared then the answer is N+1, otherwise, it will be a 
number between [1, N].
We can iterate through the array, for each number x, if it's within 
the range of [1, N], then we can mark the position x-1. After the traversal, if all the 
elements are marked, then the answer will be N+1, otherwise, it's the smallest index 
without mark plus 1.
Since we only care about numbers between [1,N], we can traverse the array and change any 
values not in [1, N] to a number larger than N (such as N+1). In this case, all numbers 
in the array will be positive and we can mark numbers with negative symbol.
The process will be:
(1). Change all values <= 0 to N+1.
(2). We can traverse the array, for each element x, it could be already marked, so the 
original number is |x|, and if |x| is within [1,N], then we mark |x| - 1 as negative. If 
it's already negative, then we don't need to add negative symbol.
(3). After traversal, if all elements are negative, then return N+1, otherwise, return the 
first positive position + 1.
Time complexity - O(N) - Though traversed three times, but all in linear.
Space Complexity - O(1)

4. Replacement - we can also replace numbers to their position, if x is in [1,N] then after 
replacement, it shall be moved to postion x - 1. After replacement, the array shall look 
like [1,2,...,N], there are some places will be wrong, and each wrong position represent a 
missing positive number. For example, for [3,4,-1,1], after replacement, it will be 
[1,-1,3,4], so we will know the missing number is 2.
To replace elements, we can traverse the array, for number nums[i]=x, if x is within [1,N] 
then x shall be on the postion of x - 1, so we shall exchange nums[i] and nums[x-1]. After 
exchange, nums[i] may still in the range of [1,N], so we need to continue exchange it.
Be careful that we could end in a dead loop, if nums[i] == nums[x-1], if that happens, it 
means x is already on the right postion, so we can skip it and iterate next element.
Time complexity - O(N) - We may exchange at most N times, so time complexity is O(N).
Space Complexity - O(1)

LeetCode Link: https://leetcode.com/problems/first-missing-positive/
"""


def find_missing_positive(nums: list) -> int:
    length = len(nums)

    # Change all values <= 0 to N+1.
    for i in range(length):
        if nums[i] <= 0: 
            nums[i] = length + 1
    
    # Mark the number as negative if it's in [1,N]
    for i in range(length):
        num = abs(nums[i])
        if num <= length:
            nums[num - 1] = - abs(nums[num - 1])
    
    # Check if numbers are marked, if not, it's the first missing number.
    # Otherwise return N+1.
    for i in range(length):
        if nums[i] > 0: 
            return i + 1
    
    return length + 1

def find_missing_positive_replacement(nums: list) -> int:
    length = len(nums)
    
    # Replace numbers to their index. x => nums[x-1]
    for i in range(length):
        while 1 <= nums[i] <= length and nums[nums[i] - 1] != nums[i]:
            nums[nums[i] - 1], nums[i] = nums[i], nums[nums[i] - 1]
    
    # Check if the number is correctly corresponding to the index.
    for i in range(length):
        if nums[i] != i + 1:
            return i + 1

    return length + 1


if __name__ == "__main__":
    nums = [1,2,0]
    print(f"First missing positive: {find_missing_positive(nums)}")

    nums = [3,4,-1,1]
    print(f"First missing positive: {find_missing_positive(nums)}")

    nums = [3,4,-1,1]
    print(f"First missing positive: {find_missing_positive_replacement(nums)}")