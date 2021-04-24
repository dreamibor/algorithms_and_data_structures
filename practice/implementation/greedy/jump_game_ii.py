"""
Greedy - Jump Game II (medium)

Description:
Given an array of non-negative integers nums, you are initially positioned 
at the first index of the array.
Each element in the array represents your maximum jump length at that 
position.
Your goal is to reach the last index in the minimum number of jumps.
You can assume that you can always reach the last index.

Example:
Input: nums = [2,3,1,1,4]
Output: 2
Explanation: The minimum number of jumps to reach the last index is 2. 
Jump 1 step from index 0 to 1, then 3 steps to the last index.

LeetCode: https://leetcode-cn.com/problems/jump-game-ii/
"""


def jump_game(nums: list) -> int:
    """ Greedy

    Iterate through the array, for each index we can find the farthest 
    position we can arrive. Each time, we choose the position which can jump 
    the farthest as the new jump starting point.

    每次在上次能跳到的范围（end）内选择一个能跳的最远的位置（也就是能跳到 max_far 位置的
    点）作为下次的起跳点。

    For example, for the array [2,3,1,1,4], at index 0, we can jump to index 
    1 and 2. The farthest position we can arrive with these two positions is 
    4 (1 + 3), meaning at index 1 and jump 3. So we choose 3 as the next 
    starting point, and update the boundary to be the current farthest 
    position.

    Time Complexity - O(N) - Iterate through the array once.
    Space Complexity - O(1) - Constant space.
    """
    # max_position - The current farthest position we can arrive.
    # end - record the right boundary we can arrive for last time.
    # steps - count the jump times.
    max_position, end, steps = 0, 0, 0

    # Skip n - 1 
    for i in range(len(nums) - 1):
        # Update the farthest position we can arrive.
        max_position = max(max_position, nums[i] + i)

        # Arriving the right boundary we can arrive last time.
        if i == end:
            # The farthest position we can arrive currently becomes the new
            # right boundary for next jump.
            end = max_position
            steps += 1 # Enter next jump.

    return steps 


if __name__ == "__main__":
    nums = [2,3,1,1,4]
    print(jump_game(nums))

    nums = [2,3,0,1,4,3,2,1]
    print(jump_game(nums))