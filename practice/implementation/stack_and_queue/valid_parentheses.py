"""
Stack - Valid Parentheses (easy)

Description:
Given a string `s` containing just the characters '(', ')', '{', '}', '[' and ']', 
determine if the input string is valid.

An input string is valid if:
1. Open brackets must be closed by the same type of brackets.
2. Open brackets must be closed in the correct order.

Example:
Input: s = "()[]{}"
Output: true

LeetCode Link: https://leetcode-cn.com/problems/valid-parentheses/
"""

def valid_parentheses(s: str) -> bool:
    """ Stack
    Time Complexity - O(N) - Iterate string once.
    Space Complexity - O(N+M) - M is the amount of vocabulary (3 here).
    """
    # For odd number of chars, it must be False.
    if len(s) % 2 == 1: return False

    paren_map = {")":"(", "}":"{", "]":"["}
    stack = []

    for char in s:
        # If char is left parentheses, then add it to stack.
        if char not in paren_map:
            stack.append(char)
        else:
            # If the stack is empty, meaning there is no parentheses  
            # to compare or the last stack element (pop) is not the 
            # same as the right parentheses, then return False.
            if not stack or stack[-1] != paren_map[char]:
                return False
            stack.pop()

    # For cases such as "((", if there are still elements in the stack
    # then it's not valid, return False.
    return not stack


if __name__ == "__main__":
    s = "(())"
    result = valid_parentheses(s)
    print(result)

