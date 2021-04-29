"""
Binary Search - Kth Smallest Number in Multiplication Table

Nearly every one have used the Multiplication Table. But could you find out 
the k-th smallest number quickly from the multiplication table?

Given the height `m` and the length `n` of a `m * n` Multiplication Table, 
and a positive integer `k`, you need to return the `k-th` smallest number in 
this table.

Example:
Input: m = 3, n = 3, k = 5
Output: 3.
Explanation: 
The Multiplication Table:
1	2	3
2	4	6
3	6	9
The 5-th smallest number is 3 (1, 2, 2, 3, 3).

Note:
1. The m and n will be in the range [1, 30000].
2.  The k will be in the range [1, m * n].

LeetCode: https://leetcode-cn.com/problems/kth-smallest-number-in-multiplication-table/
"""


def find_kth_smallest(m:int, n:int, k: int) -> int:
    """ Binary Search

    We use binary search to find the target value we want, initially the 
    minimum is 1 and the maximum is m * n. While we are searching, for each 
    step (target) we check whether there are enough k numbers than are 
    smaller than the target (mid). If there are enough numbers, then we 
    decrease the higher bound to make the mid smaller, otherwise, we shall 
    increase the lower bound, to make the mid larger so we can have enough k numbers 
    that are smaller than it (target / mid).

    To count how many numbers are smaller than mid, we can iterate through 
    the Multiplication Table rows. For each row, if the target is larger than 
    i * n, then there are n numbers smaller than the target, otherwise, the 
    amount of numbers that are smaller shall be x // i.

    In summary, the count for each row is equal to:
    count += min(target // i, n)

    If there are enough numbers smaller than target, then we shall update the 
    right bound, to make the mid smaller.

    Time Complexity - O(M*log(M*N)) - For searching through [low, high], the 
    time complexity is O(log(M*N)), for each step, we need to look through m 
    rows, so the total tiem complexity will be O(M*log(M*N)).
    Space Complexity - O(1) - Constant space.
    """
    # Lower and higher bound.
    low, high = 1, m * n
    
    # Bianry search
    while low < high:
        mid = low + (high - low) // 2

        # Count for numbers that are smaller than mid.
        count = 0
        for i in range(1, m + 1):
            count += min(mid // i, n)
        
        # If there is not enough numbers that are smaller than mid, then 
        # update the lower bound to make mid larger.
        if not count >= k:
            low = mid + 1
        else:
            high = mid
    
    return low


if __name__ == "__main__":
    m, n, k =  3, 3, 5
    print(find_kth_smallest(m, n, k))

    m, n, k =  2, 3, 6
    print(find_kth_smallest(m, n, k))