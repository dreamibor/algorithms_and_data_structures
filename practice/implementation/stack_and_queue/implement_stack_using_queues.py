"""
Stack - Implement Stack Using Queues (easy)

Implement a last in first out (LIFO) stack using only two queues. The implemented 
stack should support all the functions of a normal queue (push, top, pop, and empty).

Implement the MyStack class:
- void push(int x) Pushes element x to the top of the stack.
- int pop() Removes the element on the top of the stack and returns it.
- int top() Returns the element on the top of the stack.
- boolean empty() Returns true if the stack is empty, false otherwise.

Notes:
You must use only standard operations of a queue, which means only push to back, 
peek/pop from front, size, and is empty operations are valid.
Depending on your language, the queue may not be supported natively. You may simulate 
a queue using a list or deque (double-ended queue), as long as you use only a queue's 
standard operations.

Follow-up: Can you implement the stack such that each operation is amortized O(1) time 
complexity? In other words, performing n operations will take overall O(n) time even if 
one of those operations may take longer.

Example:
Input:
["MyStack", "push", "push", "top", "pop", "empty"]
[[], [1], [2], [], [], []]
Output:
[null, null, null, 2, 2, false]
Explanation:
MyStack myStack = new MyStack();
myStack.push(1);
myStack.push(2);
myStack.top(); // return 2
myStack.pop(); // return 2
myStack.empty(); // return False

Time Complexity:
Push - O(N) - Move all elements in queue, and enqueue.
Pop  - O(1)
Peek - O(1)

Space Complexity - O(N) - For N elements in the stack.

LeetCode Link: https://leetcode-cn.com/problems/implement-stack-using-queues/
"""
from collections import deque


class MyStack:
    def __init__(self):
        """
        Initialize your data structure here.
        """
        self.data = deque()
        self.temp = deque()

    def push(self, x: int) -> None:
        """ Push element x onto stack.

        Two Queues:
        We use queue1 to store all elements for the stack and queue2 to 
        help on push elements to stack.
        When push a element, we can enqueue the element to queue2 first 
        and then move all elements in queue1 into queue2. Then we exchange 
        queue1 and queue2, so that queue1 will be the elements in the stack 
        and its front end is the stack top.

        Time Complexity - O(N) - For moving elements.
        """
        # For using two queues.
        # self.temp.append(x)
        # while self.data:
        #     self.temp.append(self.data.popleft())
        # self.data, self.temp = self.temp, self.data

        # For only using one queue
        n = len(self.data)
        self.data.append(x)
        for _ in range(n):
            self.data.append(self.data.popleft())

    def pop(self) -> int:
        """
        Removes the element on top of the stack and returns that element.
        """
        return self.data.popleft()

    def top(self) -> int:
        """
        Get the top element.
        """
        return self.data[0]

    def empty(self) -> bool:
        """
        Returns whether the stack is empty.
        """
        return not self.data

    def __repr__(self) -> str:
        result = []
        for element in self.data:
            result.append(str(element))
        return ", ".join(result)
    
if __name__ == "__main__":
    myStack = MyStack()
    myStack.push(1)
    print(myStack)
    myStack.push(2)
    print(myStack)
    top = myStack.top()
    print(top)
    poped = myStack.pop()
    print(poped)
    myStack.empty()
    print(myStack)
