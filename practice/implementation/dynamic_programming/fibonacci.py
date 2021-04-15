"""
DP / Recursion / Math - Fibonacci (easy)

Description:
The Fibonacci numbers, commonly denoted F(n) form a sequence, called the 
Fibonacci sequence, such that each number is the sum of the two preceding 
ones, starting from 0 and 1. That is,

F(0) = 0, F(1) = 1
F(n) = F(n - 1) + F(n - 2), for n > 1.

Given n, calculate F(n).

Example:
Input: n = 2
Output: 1
Explanation: F(2) = F(1) + F(0) = 1 + 0 = 1.

LeetCode: https://leetcode-cn.com/problems/fibonacci-number/
"""
import numpy as np


def fibonacci_recursion(n: int) -> int:
    """ Recursion 

    Time Complexity - O(2^N) - For all repeated nodes.
    Space Complexity - O(N) - For recursion call stack. 
    """ 
    if n <= 1: return n

    return fibonacci_recursion(n - 1)  + fibonacci_recursion(n - 2)

def fibonacci_recursion_with_memo(n: int) -> int:
    """ Recursion with Memorization

    In this approach, we try to solve the bigger problem by recursively 
    finding the solution to smaller sub-problems. Whenever we solve a 
    sub-problem, we cache its result so that we don’t end up solving it 
    repeatedly if it’s called multiple times. Instead, we can just return 
    the saved result. This technique of storing the results of already 
    solved subproblems is called Memoization.

    Time Complexity - O(N) - For all repeated nodes.
    Space Complexity - O(N) - For memorization and recursion call stack.
    """
    def helper(n: int, memo:list) -> int:
        if n <= 1: return n

        # If we've have already solved the sub-problem, return the 
        # result from cache directly.
        if memo[n] >= 0:
            return memo[n]
        
        memo[n] = helper(n - 1, memo) + helper(n - 2, memo)
            
        return memo[n]
    
    # Using an array to record all solved sub-problems.
    memo = [-1 for i in range(n+1)]

    return helper(n, memo)

def fibonacci_dp(n: int) -> int:
    """ DP - Bottom-up with Tabulation

    Tabulation is the opposite of the top-down approach and avoids recursion. 
    In this approach, we solve the problem “bottom-up” (i.e. by solving all 
    the related sub-problems first). This is typically done by filling up an 
    n-dimensional table. Based on the results in the table, the solution to 
    the top / original problem is then computed.

    Tabulation is the opposite of Memoization, as in Memoization we solve the 
    problem and maintain a map of already solved sub-problems. In other words, 
    in memoization, we do it top-down in the sense that we solve the top 
    problem first (which typically recurses down to solve the sub-problems).

    Time Complexity - O(N) - Iterate through 0 to n.
    Space Complexity - O(N) - For extra dp list.
    """
    # Initialization
    dp = [0, 1]

    # Bottom up - starting with 2 until n.
    # If n is less than 2, then the for loop will not execute.
    for i in range(2, n + 1):
        dp.append(dp[i - 1] + dp[i - 2])
    
    return dp[n]

def fibonacci_dp_simp(n: int) -> int:
    """ Simplified DP with constant space.

    Actually, we only need to track the previous two elements, so there is no 
    need to have an array to track all numbers.

    Time Complexity - O(N) - Iterate through 0 to n.
    Space Complexity - O(1) - Constant space.
    """
    # For edge cases 0 and 1.
    if n < 2: return n

    a, b = 0, 1

    for _ in range(1, n):
        a, b = b, a + b
    
    return b

def fibonacci_matrix(n: int) -> int:
    """ Convert the Fibonacci recurrence formula to matrix multiplication.

    For each F_n, there is:
    | F_n   | = | 1  1 | * | F_n-1 |
    | F_n-1 |   | 1  0 |   | F_n-2 | 
    so, 
    | F_n   | = | 1  1 | ^ N-1 * | 1 |
    | F_n-1 |   | 1  0 |         | 0 | 
    assume,
    m = | 1  1 |
        | 1  0 |

    We only need to calculate the power of the matrix m, and then we 
    can calculate the F_n quickly. The naive method of calculating the 
    power of the matrix will be O(N), but we can use exponentiating by 
    squaring (快速幂) to accelerate the process to be O(logN).

    Time Complexity - O(logN) - For exponentiating by squaring.
    Space Complexity - O(1) - Constant space.
    """
    def matrix_mutiply(a: list, b: list) -> list:
        """ Matrix multiplication. """
        c = [[0, 0], [0, 0]]
        for i in range(2):
            for j in range(2):
                c[i][j] = a[i][0] * b[0][j] + a[i][1] * b[1][j]
        return c
    
    def matrix_pow(a: list, n: int) -> list:
        """ Exponentiating by squaring for matrix. """
        ret = [[1, 0], [0, 1]] # Identity matrix

        while n > 0:
            if n & 1:
                ret = matrix_mutiply(ret, a)
            n >>= 1
            a = matrix_mutiply(a, a)

        return ret

    # Edge cases
    if n < 2: return n

    m = [[1, 1], [1, 0]]
    # M^(N-1)
    res = matrix_pow(m, n - 1)

    # The result is the same as the first element in the result matrix.
    # | a b | * | 1 | = | a |
    # | c d |   | 0 |   | c |
    # Here a is F_n, and c is F_n-1
    return res[0][0]

def fibonacci_matrix_numpy(n: int) -> int:
    """ Matrix multiplication with numpy

    Time Complexity - O(logN) - For exponentiating by squaring.
    Space Complexity - O(1) - Constant space.
    """
    m = np.array([[1, 1], [1, 0]])
    res = np.linalg.matrix_power(m, n - 1)
    return res[0][0]

def fibonacci_math(n: int) -> int:
    """ General term formula
    
    Assuming there is a geometric sequence (等比数列) {x^n} whose common 
    ratio (公比) is x, and x is non-zero, the first term is 1, and it comply 
    with Fibonacci's recurrence formula, so that:
    x^(n+2) = x^(n+1) + x^n, 
    taking the common factor out, we will have:
    (x^2 - x - 1) x^n = 0, 
    since x^n != 0, so 
    x^2 - x - 1 = 0.
    Solving the quadratic equation, we can get two roots:
    x_1 = (1 + sqrt(5)) / 2, x_2 = (1 - sqrt(5)) / 2

    So geometric sequence {x_1 ^ n} and {x_2 ^ n} are the solutions for the 
    Fibonacci's recurrence formula. Their linear combination will be the 
    general term formula for Fibinacci sequence.

    We can take x_1 and x_2 in a linear combination and calculate their
    factors by solving the equation for n == 1 and n == 2:
    c_1 * (1 + sqrt(5)) / 2 + c_2 * (1 - sqrt(5)) / 2 = 1
    c_1 * ((1 + sqrt(5)) / 2)^2 + c_2 * ((1 - sqrt(5)) / 2)^2 = 1
    c_1 and c_2 will be 1 / sqrt(5) and -1 / sqrt(5).

    Finally, the general term formula for Fibonacci is:
    F_n = 1 / sqrt(5) * (((1 + sqrt(5)) / 2)^n - * ((1 - sqrt(5)) / 2)^n)

    Time Complexity - O(logN) - For exponentiating by squaring. Here 
    ((1 + sqrt(5)) / 2)^n and ((1 - sqrt(5)) / 2)^n need to be calculated by 
    power.
    Space Complexity - O(1) - Constant space.
    """
    # Calculate sqrt(5)
    sqrt5 = 5 ** 0.5

    res = ((1 + sqrt5) / 2) ** n - ((1 - sqrt5) / 2) ** n
    return round(res / sqrt5)


if __name__ == "__main__":
    print(fibonacci_recursion(5))
    print(fibonacci_recursion_with_memo(5))
    print(fibonacci_dp(5))
    print(fibonacci_dp_simp(5))
    print(fibonacci_matrix(5))
    print(fibonacci_matrix_numpy(5))
    print(fibonacci_math(5))