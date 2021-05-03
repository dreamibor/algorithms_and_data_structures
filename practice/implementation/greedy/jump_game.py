"""
Greedy - Jump Game (medium)

Description:
Given an array of non-negative integers nums, you are initially positioned 
at the first index of the array.

Each element in the array represents your maximum jump length at that 
position.

Determine if you are able to reach the last index.

Example:
Input: nums = [2,3,1,1,4]
Output: true
Explanation: Jump 1 step from index 0 to 1, then 3 steps to the last index.

LeetCode: https://leetcode-cn.com/problems/jump-game/
"""


def jump_game(nums: list) -> bool:
    """ Greedy

    As long as there is an index x which x + nums[x] is larger than or equal 
    to the length of the array, then it means we can reach the last index.

    We iterate through the array, and update the farthest position we can 
    arrive. We need to check whether the current position is with in the 
    range of previous farthest position, meaning whether we can actually 
    arrive the current position.

    Time Complexity - O(N) - Iterate through the array once.
    Space Complexity - O(1) - Constant space.
    """
    n = len(nums)
    # Track the farthest position we can arrive.
    right_most = 0

    for i, num in enumerate(nums):
        # Check if the current index is with the range of previous 
        # farthest position, or whether we can actually arrive here.
        if i <= right_most:
            # Update the farthest position.
            right_most = max(right_most, i + num)
            # If we can reach the last index, then return True.
            if right_most >= n - 1:
                return True

    return False

def jump_game_dp(nums: list) -> bool:
    """ Dynamic Programming

    State Definition:
    dp[i] - the farthest position we can jump from position before and 
    including i (j <= i).

    Initialization:
    dp[0] = nums[0] # For first position

    DP State Transition:
    If we can arrive position i from previous positions [0, i-1], meaning 
    dp[i-1] >= i, then:
    dp[i] = max(dp[i-1], i + nums[i])
    otherwise:
    dp[i] = dp[i-1] # For cases we can't arrive position i.

    Since dp[i] is only related to dp[i-1], so we can simply the DP array 
    into a single variable.

    Time Complexity - O(N) - Iterate through the array once.
    Space Complexity - O(1) - Constant space.
    """
    # Edge cases
    if not nums: return 0

    n = len(nums)
    # # Define DP state array
    # dp = [0 for _ in range(n)]
    # # Initialization
    # dp[0] = nums[0]

    # # DP state transition
    # for i in range(1, n):
    #     if dp[i-1] >= i:
    #         dp[i] = max(dp[i-1], i + nums[i])
    #     else:
    #         dp[i] = dp[i-1]
    
    # return dp[-1] >= n - 1

    max_pos = nums[0]

    for i in range(1, n):
        if max_pos >= i:
            max_len = max(max_len, i + nums[i])
        
    return max_len >= n - 1


if __name__ == "__main__":
    nums = [2,3,1,1,4]
    print(jump_game(nums))

    nums = [3,2,1,0,4]
    print(jump_game(nums))