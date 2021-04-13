"""
Bitwise Manipulation - Power of Two (easy)

Description:
Given an integer n, return true if it is a power of two. Otherwise, return 
false.

An integer n is a power of two, if there exists an integer x such that 
n == 2x.

Example:
Input: n = 1
Output: true
Explanation: 20 = 1

LeetCode: https://leetcode-cn.com/problems/power-of-two/
"""


def power_of_two_naive(n: int) -> bool:
    """ Naive method
    
    Check if the number has removed all zeros after the single bit with 
    1 is 1.

    Time Complexity - O(logN) - logN for bits to save N in binary format.
    Space Complexity - O(1) - Constant space.
    """
    # Edge case
    if n == 0: return False

    # Remove all the zeros after the bit with 1.
    while n % 2 == 0:
        n >>= 1
    # Check if the number that has removed all zeros after the bit 
    # with 1 is still 1.
    return n == 1   

def power_of_two(n: int) -> bool:
    """ Bit Manipulation

    Properties of numbers are power of two: there is one and only one bit 
    is 1 in the binary format, other bits are must 0s.

    Time Complexity - O(1) - Constant time.
    Space Complexity - O(1) - Constant space.
    """
    # n shall be larger than 1 and the number that 
    # removed the last bit with 1 (set to 0) shall be 0.
    return n > 0 and not (n & n -1)


if __name__ == "__main__":
    print(power_of_two(1))
    print(power_of_two_naive(1))
    print(power_of_two(16))
    print(power_of_two_naive(16))
    print(power_of_two(3))
    print(power_of_two_naive(3))
    print(power_of_two(5))
    print(power_of_two_naive(5))