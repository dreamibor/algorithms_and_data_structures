"""
Stack - Evaluate Reverse Polish Notation (medium)

Description:
Evaluate the value of an arithmetic expression in Reverse Polish Notation.
Valid operators are +, -, *, /. Each operand may be an integer or another expression.

Note:
- Division between two integers should truncate toward zero.
- The given RPN expression is always valid. That means the expression would always 
evaluate to a result and there won't be any divide by zero operation.

Example:
Input: ["2", "1", "+", "3", "*"]
Output: 9
Explanation: ((2 + 1) * 3) = 9

LeetCode Link: https://leetcode-cn.com/problems/evaluate-reverse-polish-notation/
"""

def eval_rpn(tokens: list) -> int:
    stack = []

    for token in tokens:
        if token not in "+-*/":
            # If the token is not an operator, then push it to stack.
            stack.append(int(token))
        else:
            # a, b is poped in sequence, b is after a.
            a, b = stack.pop(), stack.pop()
            if token == "+":
                stack.append(a + b)
            elif token == "-":
                # Be careful about the order.
                stack.append(b - a)
            elif token == "*":
                stack.append(a * b)
            else:
                # Be careful about the order.
                stack.append(int(b / a))

    return stack.pop()

if __name__ == "__main__":
    array = ["2", "1", "+", "3", "*"]
    print(f"{eval_rpn(array)}")

    array = ["10", "6", "9", "3", "+", "-11", "*", "/", "*", "17", "+", "5", "+"]
    print(f"{eval_rpn(array)}")