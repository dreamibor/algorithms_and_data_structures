"""
Divide and Conquer - Pow(x, n)

Implement pow(x, n), which calculates x raised to the power n (i.e., x^n).

Example:
Input: x = 2.00000, n = 10
Output: 1024.00000

Note:
n could be negative, such as n = -2, for example:
Input: x = 2.00000, n = -2
Output: 0.25000
Explanation: 2^-2 = 1/2^2 = 1/4 = 0.25

LeetCode: https://leetcode-cn.com/problems/powx-n/
"""


def pow_recursion(x: float, n: int) -> float:
    """ Divide and Conquer - Recursion
    """
    # Recursion termination.
    if n == 0:
        return 1
    
    # For n is negative.
    if n < 0:
        return 1 / pow_recursion(x, -n)
    
    # For n are odd cases.
    if n % 2:
        return x * pow_recursion(x, n - 1)

    # For n are even cases.
    return pow_recursion(x*x, n / 2)

def pow(x: float, n: int) -> float:
    """ Divide and Conquer - Non-recursion

    """
    # For n are negative cases.
    if n < 0:
        x = 1 / x
        n = -n

    # For the final result
    result = 1

    while n:
        # For n are odd cases.
        if n % 2 == 1:
            result *= x
        # Double up x and half n.
        x *= x
        n = n // 2

    return result 


if __name__ == "__main__":
    # Recursion
    x, n = 2.00000, 10
    print(pow_recursion(x, n))
    x, n = 2.00000, -2
    print(pow_recursion(x, n))

    # Non-recursion
    x, n = 2.00000, 10
    print(pow(x, n))
    x, n = 2.00000, -2
    print(pow(x, n))