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

When n is negative, we can calculate (1 / x) ^ (-n) or 1 / x ^ (-n).

LeetCode: https://leetcode-cn.com/problems/powx-n/
"""


def pow_recursion(x: float, n: int) -> float:
    """ Divide and Conquer - Recursion
    
    Exponentiation by squaring (or in Chinese 快速幂)
    
    1. When we are calculating x^n, we can calculate x^[n/2] recursively 
    first, [a] meaning rounding down to integer.
    2. In the recursion process, if n is even, then we calculate x^2, if 
    n is odd number then we calculate x * recursion(x, n - 1).
    3. The termination condition will be n == 0, since any number's power 
    of 0 is 1. 

    Time Complexity - O(logN) - For recursion.
    Space Complexity - O(logN) - For recursion.
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

    Recursion will need extra stack space, so we can write the divide 
    and conquer program with iteration.

    We can represent n in the binary format, check power_x_n.png .

    For example, 3 ^ 21, where 21 could be represent in bianry format 
    as (10101)2, for where the binary digit is 1, we shall mutliple the 
    current x into the result. 

    Reference: https://www.cnblogs.com/mjios/p/12690097.html

    Time Complexity - O(logN) - Since for each while loop, n >>= 1, so the 
    value of n will be halfed.
    Space Complexity - O(1) - Constant space.
    """
    # For n are negative cases, convert the problem to (1 / x) ^ (-n).
    if n < 0:
        x = 1 / x
        n = -n

    # For the final result
    result = 1

    while n:
        # For binary digit is 1.
        if n & 1:
            result *= x
        
        # Double up x and move n right by 1 digit.
        x *= x
        n >>= 1

    return result 


if __name__ == "__main__":
    # Recursion
    x, n = 2.00000, 10
    print(pow_recursion(x, n))
    x, n = 2.00000, -2
    print(pow_recursion(x, n))

    # Non-recursion
    x, n = 2.00000, 11
    print(pow(x, n))
    x, n = 2.00000, -2
    print(pow(x, n))