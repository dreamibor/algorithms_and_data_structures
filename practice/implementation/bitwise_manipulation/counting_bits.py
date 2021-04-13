"""
Bitwise Manipulation - Counting Bits (medium)

Description:
Given an integer num, return an array of the number of 1's in the binary 
representation of every number in the range [0, num].

Example:
Input: num = 2
Output: [0,1,1]
Explanation:
0 --> 0
1 --> 1
2 --> 10

LeetCode: https://leetcode-cn.com/problems/counting-bits
"""

def counting_bits_naive(n: int) -> list:
    """ Hamming Weight Loop

    Check each number's hamming weight with a for loop.

    Time Complexity - O(K*N) - K is the number of bits for the binary format,
    for example, 32. While N is the amount of number from 0 to num. 
    Time Complexity - O(1) - Constant space except the return array. 
    """
    result = []

    for i in range(n + 1):
        # Hamming weight
        count = 0
        while i:
            count += 1
            i &= i - 1
        # Append the hamming weight into the result.
        result.append(count)

    return result


def counting_bits(n: int) -> list:
    """ DP with Bit Manipulation
    
    Assuming y = x & (x - 1), where y is the number after removing the 
    last bit with 1 in x. 0 <= y < x, bits[x] = bits[y] + 1.

    For each positive integer, there is:
    count[i] = count[i & (i - 1)] + 1

    So we need to iterate through 1 to num, and calculate the count of 
    bits for each number.

    Why it works?
    For each positive number, there must be some bits are 1, so the the 
    number of bits with 1 shall be the number of bits with 1 for the 
    number that removed the last bit with 1 plus 1 (as it's the current) 
    one. So that's why we get the DP recurrence formula as above.

    For example, for the integer 5, it's bianry format is (101), after  
    removing the last bit with 1, the number will be (100), which is 
    actually 4 in decimal system, and we can get the number of bits with 
    1 in integer 4 from previous calculation, and what we need to do in 
    the recurrence formula is just plus one.

    Time Complexity - O(N) - O(1) for each number, in total N numbers.
    Time Complexity - O(1) - Constant space except the return array. 
    """
    result = [0]

    for i in range(1, n + 1):
        print(i & (i - 1))
        result.append(result[i & (i - 1)] + 1)
        print(result)

    return result



if __name__ == "__main__":
    print(counting_bits_naive(2))
    print(counting_bits(2))
    print(counting_bits_naive(5))
    print(counting_bits(5))
