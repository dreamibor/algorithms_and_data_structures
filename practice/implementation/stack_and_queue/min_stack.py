"""
Stack - Min Stack (easy)

Description:
Design a stack that supports push, pop, top, and retrieving the minimum 
element in constant time.
- push(x) -- Push element x onto stack.
- pop() -- Removes the element on top of the stack.
- top() -- Get the top element.
- getMin() -- Retrieve the minimum element in the stack.

Example:
Input:
["MinStack","push","push","push","getMin","pop","top","getMin"]
[[],[-2],[0],[-3],[],[],[],[]]

Output:
[null,null,null,null,-3,null,0,-2]

Explanation:
MinStack minStack = new MinStack();
minStack.push(-2);
minStack.push(0);
minStack.push(-3);
minStack.getMin(); // return -3
minStack.pop();
minStack.top();    // return 0
minStack.getMin(); // return -2

LeetCode Link: https://leetcode-cn.com/problems/min-stack/
"""
import math


class MinStack:
    """ Solution - helper stack
    We can have an extra stack to help memorise the min value for the current
    value and the elements pushed before it. The process is as follows:
    1. When an element is pushed into the stack, we get the smaller value between 
    the element and the min value before it, and add this min value into helper
    stack.
    2. When pop an element, pop the corresponding helper stack element as well.
    3. At any time, the value at the top of helper stack is the min value of the 
    stack.

    Time Complexity - O(1) - for all operations.
    Space Complexity - O(N) - N is the total elements.
    """
    def __init__(self):
        """ Initialize your data structure here. """
        self.data = []
        self.min_stack = [math.inf]

    def push(self, x: int) -> None:
        self.data.append(x)
        # Add the min value to helper stack.
        self.min_stack.append(min(x, self.min_stack[-1]))

    def pop(self) -> None:
        # Pop the helper stack element as well.
        self.min_stack.pop()
        return self.data.pop()

    def top(self) -> int:
        return self.data[-1]

    def getMin(self) -> int:
        return self.min_stack[-1]

    def __repr__(self) -> str:
        result = []
        for element in self.data:
            result.append(f"{element}")
        return ", ".join(result)


if __name__ == "__main__":
    min_stack = MinStack()
    min_stack.push(-2)
    min_stack.push(0)
    min_stack.push(-3)
    print(min_stack)
    min_value = min_stack.getMin()
    print(min_value)
    min_stack.pop()
    min_stack.pop()
    print(min_stack)
    min_value = min_stack.getMin()
    print(min_value)