"""
DP - Target Sum (medium)

Description:
You are given an integer array nums and an integer target.
You want to build an expression out of nums by adding one of the symbols 
'+' and '-' before each integer in nums and then concatenate all the 
integers.

For example, if nums = [2, 1], you can add a '+' before 2 and a '-' before 
1 and concatenate them to build the expression "+2-1".

Return the number of different expressions that you can build, which 
evaluates to target.

Example:
Input: nums = [1,1,1,1,1], target = 3
Output: 5
Explanation: There are 5 ways to assign symbols to make the sum of nums be 
target 3.
-1 + 1 + 1 + 1 + 1 = 3
+1 - 1 + 1 + 1 + 1 = 3
+1 + 1 - 1 + 1 + 1 = 3
+1 + 1 + 1 - 1 + 1 = 3
+1 + 1 + 1 + 1 - 1 = 3

Hints:
* 1 <= nums.length <= 20
* 0 <= nums[i] <= 1000
* 0 <= sum(nums[i]) <= 1000
* -1000 <= target <= 100

LeetCode: https://leetcode-cn.com/problems/target-sum/
"""


def target_sum_dp_opt(nums: list, target: int) -> int:
    """ Dynamic Programming Optimised for Space

    Since dp[i][...] is only related to dp[i-1][...], so we can use two 1D 
    arrays to reduce the space complexity.

    Time Complexity - O(N * Max_Sum) - N is the number of elements in the 
    array. Max_Sum is the the absolute number when we use all plus or minus.
    Space Complexity - O(Max_Sum) - For the 1D DP state array.
    """
    # The absolute sum of using all plus or minus.
    max_sum = sum(nums)

    # Edge cases, for target larger than the maximum sum, we can't get there.
    if target > max_sum: return 0
    
    # DP state array
    n = len(nums)
    # The width contains negative, zero and positive part.
    # max_sum is corresponding to zero here.
    width = 2 * max_sum + 1
    dp = [0] * width

    # Initialization
    if nums[0] == 0:
        # For the first element is 0, there are two ways to get zero,
        # either plus or minus zero will get zero.
        dp[max_sum] = 2
    else:
        # For non-zero first element, we can update the DP array accordingly.
        dp[max_sum + nums[0]] = 1
        dp[max_sum - nums[0]] = 1

    # DP state transition
    for i in range(1, n):
        # Temp DP array to save current row result.
        temp = [0] * width
        for j in range(width):
            # Handling boundary cases, if the number doesn't exist, return 0.
            l = dp[j - nums[i]] if (j - nums[i]) >= 0 else 0
            r = dp[j + nums[i]] if (j + nums[i]) < width else 0
            temp[j] = l + r

        # Exchange the temp values into DP state array.
        dp = temp

    return dp[max_sum + target]

def target_sum_dp(nums: list, target: int) -> int:
    """ Dynamic Programming

    DP state definition:
    dp[i][j] - the number of methods to get j using elements from first i 
    elements  with plus (+) and minus (-).

    Initialization:
    For cases where nums[0] = 0, there are two ways to get there (plus or 
    minus), so dp[0][sum] shall be 2 rather than 0. 
    Since array index could not be negative, so we start from sum here.

    DP state transition:
    dp[i][j] = dp[i - 1][j - nums[i]] + dp[i - 1][j + nums[i]]
    There are two methods to get j, either plus nums[i] or minus nums[i].

    DP table:
    Different from usual DP table, here the DP table will be split into three 
    parts, negative / zero / positive. The table width will be 2 * sum + 1. 
    sum is the absolute number when we use all plus or minus, and 1 is for 
    the zero in the middle.
    For reference: ![Target Sum DP Table](assets/target_sum.png)

    The final will be dp[n - 1][sum + target].

    Time Complexity - O(N * Max_Sum) - N is the number of elements in the 
    array. Max_Sum is the the absolute number when we use all plus or minus.
    Space Complexity - O(N * Max_Sum) - For the DP state array.
    """
    # The absolute sum of using all plus or minus.
    max_sum = sum(nums)

    # Edge cases, for target larger than the maximum sum, we can't get there.
    if target > max_sum: return 0
    
    # DP state array
    n = len(nums)
    # The width contains negative, zero and positive part.
    # max_sum is corresponding to zero here.
    width = 2 * max_sum + 1
    dp = [[0] * width for _ in range(n)]

    # Initialization
    if nums[0] == 0:
        # For the first element is 0, there are two ways to get zero,
        # either plus or minus zero will get zero.
        dp[0][max_sum] = 2
    else:
        # For non-zero first element, we can update the DP array accordingly.
        dp[0][max_sum + nums[0]] = 1
        dp[0][max_sum - nums[0]] = 1

    # DP state transition
    for i in range(1, n):
        for j in range(width):
            # Handling boundary cases, if the number doesn't exist, return 0.
            l = dp[i - 1][j - nums[i]] if (j - nums[i]) >= 0 else 0
            r = dp[i - 1][j + nums[i]] if (j + nums[i]) < width else 0
            dp[i][j] = l + r
    
    return dp[n - 1][max_sum + target]

def target_sum_backtracking(nums: list, target: int) -> int:
    """ Backtracking

    We can use recursion to enumerate all possible cases. When we are 
    processing the i_th number, we can add + or -, and recusively search for 
    these two cases. When we reach the N_th number, we can check if the sum 
    is equal to the target, if yes, add the count by one.

    Time Complexity - O(2^N) - N is the number of elements in the array. 
    Space Complexity - O(N) - For the recursion stack.
    """
    # Edge cases
    if sum(nums) < target:
        return 0

    def helper(nums, i, cur_sum):
        """ Recursion helper function. 
        params: nums - the input array.
        params: i - the current number index.
        parmas: cur_sum - the current sum until i_th number.
        """
        nonlocal count

        # Recursion termination
        if i == len(nums):
            # If the sum is equal to target, then add the count by 1.
            if cur_sum == target:
                count += 1
        else:
            # Drill down into two cases, + or -.
            helper(nums, i + 1, cur_sum+nums[i])
            helper(nums, i + 1, cur_sum-nums[i])

    count = 0
    helper(nums, 0, 0)
    return count


if __name__ == "__main__":
    nums, target = [1, 1, 1, 2, 3], 4
    print(target_sum_dp(nums, target))
    print(target_sum_dp_opt(nums, target))
    print(target_sum_backtracking(nums, target))

    nums, target = [1, 1, 1, 1, 1], 3
    print(target_sum_dp(nums, target))
    print(target_sum_dp_opt(nums, target))
    print(target_sum_backtracking(nums, target))
