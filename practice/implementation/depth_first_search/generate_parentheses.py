"""
Generate Parentheses (medium)

Description:
Given n pairs of parentheses, write a function to generate all combinations of 
well-formed parentheses.

Constraints: 1 <= n <= 8

Example:
Input: n = 3
Output: ["((()))","(()())","(())()","()(())","()()()"]

LeetCode: https://leetcode-cn.com/problems/generate-parentheses/
"""


def generate_parentheses(n: int) -> list:
    """ Recursion / DFS / Back-tracking with Pruning

    Brute Force - the length of the output string will be equal to 2*n, each char in the 
    string has two states, left parentheses or right parenthesis. In total, there will be 
    2^2n cases, and then we can validate whether each of them is valid or not. However, 
    the time complexity will be O(2^2N).

    To improve the algorithm, we can prune invalid cases:
    1. Local invalid case, stop recursion - such as right parentheses at the beginning.
    2. The amount of left and right parentheses shall be equal to n. As long as the number 
    of left or right parentheses is larger than n, then stop.

    Time Complexity - O(4^N / sqrt(N)) - related to [Catalan number](https://en.wikipedia.org/wiki/Catalan_number). 
    Space Complexity - O(N) - For recursion stack.
    """
    def _gen(left, right, n, string=""):
        """
        :params left - the number of left parentheses "(" used.
        :params right - the number of right parentheses ")" used.
        :params n - the input - the number of pairs of parentheses.
        :params string - the current string.
        """
        # Recursion termination, left and right parentheses have been used.
        if left == n and right == n:
            result.append(string)
            return 
        
        # When there are remaining left parentheses, add it into the string.
        if left < n:
            _gen(left + 1, right, n, string + "(")
        # Apart from remaining right parentheses, the number of current right 
        # parentheses shall be less than the number of left parentheses.
        if left > right: # and right < n:
            _gen(left, right + 1, n, string + ")")
    
    result = []
    # Call the recursion functon.
    _gen(0, 0, n,"")

    return result


if __name__ == "__main__":
    print(generate_parentheses(1))
    print(generate_parentheses(3))
