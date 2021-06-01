"""
DP - Backpack (medium)

Description:
Given n items with size A_i​ an integer m denotes the size of a backpack. How 
full you can fill this backpack?

You can not divide any item into small pieces.

Example:
Input:
array = [3,4,8,5]
backpack size = 10
Output: 9

Challenge:
1. O(n x m) time and O(m) memory.
2. O(n x m) memory is also acceptable if you do not know how to optimize 
memory.

LintCode: https://www.lintcode.com/problem/backpack/description
"""


def backpack_dp(items: list, size: int) -> int:
    """ Dynamic Programming

    Here we are assuming that:
    1. Each kind has only one item.
    2. Each item can only be chosen once.

    DP state definition:
    dp[i][j] - The maximum loaded space with first i items and capacity j.

    Initialization:
    1. Initialize first column:
    For the first column, where the capacity is 0, no matter what items we 
    got, the maximum loaded space will be 0.

    2. Initialize first row:
    For the first row, when the capacity is larger than the first item, we 
    can put the first item in, otherwise 0. 

    DP state transition:
    if j - A[i] >= 0:
        dp[i][j] = max(dp[i-1][j-A[i]] + A[i], dp[i-1][j])
    else:
        dp[i][j] = dp[i-1][j]

    Reference: 
    1. https://blog.csdn.net/wutingyehe/article/details/46910103
    2. https://cloud.tencent.com/developer/article/1192746

    Time Complexity - O(M*N) - For the DP state transition flow.
    Space Complexity - O(M*N) - For the DP state array.
    """
    # Edge cases
    if not items or not size: return 0

    n = len(items)
    m = size

    # DP state array
    dp = [[0] * (m + 1) for _ in range(n)]

    # Initialization
    # First column, capacity = 0, all elements shall be 0.
    for i in range(n): 
        dp[i][0] = 0
    # First row, if capacity is larger than the first item, then it shall be 
    # the weight of first item, otherwise 0.
    for j in range(1, m + 1):
        if j >= items[0]:
            # We can put the first item into the backpack.
            dp[0][j] = items[0]
        else:
            # We can't put the first item into the backpack, so 0.
            dp[0][j] = 0

    # DP state transition
    for i in range(1, n):
        for j in range(1, m + 1):
            if j >= items[i]:
                # When the item takes space less than the capacity, we can 
                # put the item in, it could make the occupied space larger or 
                # smaller, so we shall take the maximum of put it in or not.
                dp[i][j] = max(dp[i-1][j], dp[i-1][j - items[i]] + items[i])
            else:
                # A[i] > j here, meaning the item occupies a space even 
                # larger than the capacity, so we can't put the item in.
                dp[i][j] = dp[i-1][j]

    return dp[n - 1][m]

def backpack_dp_opt(items: list, size: int) -> int:
    """ Dynamic Programming Optmized for Space

    Given the DP state transition equation:
    dp[i][j] = max(dp[i-1][j-A[i]] + A[i], dp[i-1][j])
    We can see that the current state only relates to the state above it and 
    the state at top-left (in previous row), so we can optimise the space 
    with rolling array.

    We shall update the DP array backwards, and the DP state transition 
    equation will be:
    if j >= A[i]:
        dp[j] = max(dp[j], dp[j - A[i]] + A[i])

    Time Complexity - O(M*N) - For the DP state transition flow.
    Space Complexity - O(M) - Optimised space for DP state array.
    """
    # Edge cases
    if not items or size == 0: return 0

    n = len(items)
    m = size

    # DP state array
    dp = [0] * (m + 1)

    for i in range(n):
        # Traverse j backwards.
        # for j in reversed(range(m + 1)):
        #     # If the capacity is larger than or equal to the item space, 
        #     # then take the maximum between put the item in or not.           
        #     if j >= items[i]:
        #         dp[j] = max(dp[j], dp[j - items[i]] + items[i])

        # The above inner loop can be further simplified to:
        for j in reversed(range(items[i], m + 1)):
            dp[j] = max(dp[j], dp[j - items[i]] + items[i])

    return dp[m]

if __name__== "__main__":
    items, size = [3,4,8,5], 10
    print(backpack_dp(items, size))
    print(backpack_dp_opt(items, size))