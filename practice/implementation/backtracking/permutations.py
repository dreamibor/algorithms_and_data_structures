"""
Backtracking - Permutations

Given an array nums of distinct integers, return all the possible 
permutations. You can return the answer in any order.

Example:
Input: nums = [1,2,3]
Output: [[1,2,3],[1,3,2],[2,1,3],[2,3,1],[3,1,2],[3,2,1]]

LeetCode: https://leetcode-cn.com/problems/permutations/
"""

def permute(nums: list) -> list:
    """ Backtracking - remove 

    Time Complexity - O(N * N!) - The number of backtracking calling times 
    is equal relevant to the total number of permutations which is O(N!). 
    Each time, we need O(N) to remove and recover the current number used. 
    So in total, the complexity will be O(N * N!).
    Space Complexity - O(N) - Apart from the result array, we need O(N) 
    space for recursion stack.  
    """
    def backtracking(nums: list, cur_arr: list):
        # Recursion termination
        if not nums:
            result.append(cur_arr)
        
        # Drill down
        for index, num in enumerate(nums):
            nums.remove(num)
            backtracking(nums, cur_arr+[num])
            # Recover the array
            nums.insert(index, num)

    result = []
    backtracking(nums, [])
    return result

def permute_1(nums: list) -> list:
    """ Backtracking - cutting array.

    Same as above.
    """
    def backtracking(nums: list, cur_arr: list):
        # Recursion termination
        if not nums:
            result.append(cur_arr)

        # Drill down
        for i in range(len(nums)):
            backtracking(nums[:i] + nums[i+1:], cur_arr + [nums[i]])

    result = []
    backtracking(nums, [])
    return result

def permute_2(nums: list) -> list:
    """ Backtracking - In-place Tracking

    We can use an index to track the chosen numbers, for example, we have 
    a variable called `first` to split the array, on the left [0, first-1], 
    the array store numbers have been chosen, on the right [first, n - 1],
    stores unchosen numbers. 

    Same as above.
    """
    def backtracking(first):
        # Recursion termination
        if first == n:
            result.append(nums[:])

        for i in range(first, n):
            # Swap first and i to increase the chosen indices by one.
            nums[first], nums[i] = nums[i], nums[first]
            # Drill down
            backtracking(first + 1)
            # Recover the array.
            nums[first], nums[i] = nums[i], nums[first]
    
    n = len(nums)
    result = []
    backtracking(0)
    return result

if __name__ == "__main__":
    nums = [1,2,3]
    result = permute(nums)
    print(result)
    result = permute_1(nums)
    print(result)
    result = permute_2(nums)
    print(result)

    nums = [1]
    result = permute(nums)
    print(result)
    result = permute_1(nums)
    print(result)
    result = permute_2(nums)
    print(result)