"""
Bitwise Manipulation - Number of 1 Bits (easy)

Description:
Write a function that takes an unsigned integer and returns the number of '1' 
bits it has (also known as the Hamming weight).

Note:
* Note that in some languages, such as Java, there is no unsigned integer type. 
In this case, the input will be given as a signed integer type. It should not 
affect your implementation, as the integer's internal binary representation is 
the same, whether it is signed or unsigned.
* In Java, the compiler represents the signed integers using 2's complement 
notation. Therefore, in Example 3, the input represents the signed integer -3.

Example:

Input: n = 00000000000000000000000000001011
Output: 3
Explanation: The input binary string 00000000000000000000000000001011 has a total of three '1' bits.

LeetCode: https://leetcode-cn.com/problems/number-of-1-bits
"""


def hamming_weight(n: int) -> int:
    """ X & (X-1)

    X & (X-1) remove the last bit with 1 in the number.
    For example:
      10010
    & 10000
    -------
      10000
    We've removed the last bit with 1 in 10010_2.

    Time Complexity - O(logN) - The time complexity is related to the number 
    of bits of 1. The worst case will be all of the bits are 1, which we need 
    to loop for logN times (logN bits to represent N).
    Space Complexity - O(1) - Constant space.
    """
    count = 0

    while n:
        count += 1
        # Remove the last bit with 1.
        n &= n -1

    return count

def hamming_weight_right_shift(n: int) -> int:
    """ Check the last bit and right shift 1 bit.

    Time Complexity - O(K) - K is the number of bits representing the integer 
    number, for example, for 32-bit integer, it's O(32).
    Space Complexity - O(1) - Constant space.
    """
    count = 0

    while n:
        if n % 2 == 1: # Check the last bit is one or not.
            count += 1
        n >>= 1 # right shift by 1-bit.
    
    # One line code:
    # return sum(1 for i in range(32) if n & (1 << i))
    return count


if __name__ == "__main__":
    n = int("00000000000000000000000000001011", base=2)
    print(hamming_weight(n))
    print(hamming_weight_right_shift(n))

    n = int("00000000000000000000000010000000", base=2)
    print(hamming_weight(n))
    print(hamming_weight_right_shift(n))