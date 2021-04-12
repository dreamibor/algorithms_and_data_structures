"""
Binary Search - Sqrt(x) (easy)

Description:
Given a non-negative integer x, compute and return the square root of x.

Since the return type is an integer, the decimal digits are truncated, and only 
the integer part of the result is returned.

Example:
Input: x = 4
Output: 2

Constraints: 0 <= x <= 2^31 - 1

LeetCode: https://leetcode-cn.com/problems/sqrtx/
"""


def sqrtx_int(x: int) -> int:
    """ Binary Search

    Time Complexity - OlogN) - For binary search.
    Space Complexity - O(1) - For some variables.
    """
    left, right = 0, x
    res = -1

    while left <= right:
        mid = (left + right) // 2

        # For extremely large numbers.
        if mid == x / mid:
            return mid
        elif mid < x / mid:
            left = mid + 1
            # Record the mid since it's square is smaller than x.
            # We are retruning the integer part of the square root.
            res = mid
        else:
            right = mid - 1
    
    return res

def sqrtx(x: int, precision: float) -> int:
    """


    """
    left, right = 0, x

    while abs(left - right) >= precision:
        mid = (left + right) / 2

        if mid == x / mid:
            return mid
        elif mid < x / mid:
            left = mid
        else:
            right = mid
    
    return (left-right) / 2 + right

def sqrtx_newton_int(x: int) -> int:
    """ Newton's Method

    Given x^2 = C 
    => f(x) = x^2 -C

    Based on Newton's method:
    x_n+1 = x_n - f(x_n) / f'(x_n)
          = x_n - (x_n^2 - C)/ 2 * x_n
          = (x_n^2 + C) / (2 * x_n)
          = 1/2 *(x_n + C / x_n)
    
    Time Complexity - O(logx) - Usually faster than binary search.
    Space Complexity - O(1) - For some variables.
    """
    if x == 0: return 0

    C, x0 = float(x), float(x)
    while True:
        # Newton Iteration.
        xi = 0.5 * (x0 + C / x0)
        # While loop termination when we have reached the precision.
        if abs(x0 - xi) < 1e-9:
            break
        x0 = xi

    return int(x0)


if __name__ == "__main__":
    print(sqrtx_int(8))
    print(sqrtx_int(4))

    print(sqrtx(5, 1e-9))
    print(sqrtx(81, 1e-9))

    print(sqrtx_newton_int(5))
    print(sqrtx_newton_int(81))