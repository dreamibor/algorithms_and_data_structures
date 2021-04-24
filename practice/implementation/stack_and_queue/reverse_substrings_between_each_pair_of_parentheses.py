"""
Stack - Reverse Substrings Between Each Pair of Parentheses (medium)

You are given a string `s` that consists of lower case English letters and 
brackets. 
Reverse the strings in each pair of matching parentheses, starting from the 
innermost one.
Your result should not contain any brackets.

Example 3:

Input: s = "(ed(et(oc))el)"
Output: "leetcode"
Explanation: First, we reverse the substring "oc", then "etco", and finally, 
the whole string.

LeetCode: https://leetcode-cn.com/problems/reverse-substrings-between-each-pair-of-parentheses
"""


def reverse_substring(s: str) -> str:
    """ Stack

    Time Complexity - O(N) - Iterate through the string only once.
    Space Complexity - O(N) - For the stack.
    """
    stack = []

    for i, char in enumerate(s):
        # Whence we encounter a right parenthesis, pop out all characters 
        # before a left parenthesis.
        if char == ")":
            temp_str = []
            # Pop out all all characters before a left parenthesis.
            while stack and stack[-1] != "(":
                temp_str.append(stack.pop())
            # Pop out the left parenthesis "(".
            stack.pop()
            # Add the temp string into the stack again.
            stack += temp_str
        else:
            stack.append(char)

    return "".join(stack)


if __name__ == "__main__":
    s = "(ed(et(oc))el)"
    print(reverse_substring(s))
    
    s = "a(bcdefghijkl(mno)p)q"
    print(reverse_substring(s))