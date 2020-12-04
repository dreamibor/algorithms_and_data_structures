"""
Queue - Implement Queue Using Stacks (easy)

Description:
Implement a first in first out (FIFO) queue using only two stacks. The 
implemented queue should support all the functions of a normal queue 
(push, peek, pop, and empty).

Implement the MyQueue class:
- void push(int x) Pushes element x to the back of the queue.
- int pop() Removes the element from the front of the queue and returns it.
- int peek() Returns the element at the front of the queue.
- boolean empty() Returns true if the queue is empty, false otherwise.

Notes:
You must use only standard operations of a stack, which means only push to top, 
peek/pop from top, size, and is empty operations are valid.
Depending on your language, the stack may not be supported natively. You may 
simulate a stack using a list or deque (double-ended queue) as long as you use 
only a stack's standard operations.

Follow-up: 
Can you implement the queue such that each operation is amortized O(1) time 
complexity? In other words, performing n operations will take overall O(n) time 
even if one of those operations may take longer.

Example:
Input:
["MyQueue", "push", "push", "peek", "pop", "empty"]
[[], [1], [2], [], [], []]
Output:
[null, null, null, 1, 1, false]

Explanation:
MyQueue myQueue = new MyQueue();
myQueue.push(1); // queue is: [1]
myQueue.push(2); // queue is: [1, 2] (leftmost is front of the queue)
myQueue.peek(); // return 1
myQueue.pop(); // return 1, queue is [2]
myQueue.empty(); // return false

LeetCode Link: https://leetcode-cn.com/problems/implement-queue-using-stacks/
"""


############################################################
#         Two Stacks - Enqueue O(N) Dequeue O(1)           #
############################################################
class MyQueue:
    def __init__(self):
        """ Initialize your data structure here. """
        self.data = []
        self.temp = []

    def push(self, x: int) -> None:
        """ Push element x to the back of queue.
        A newly pushed element shall be at the bottom of the `data` stack. To do so, 
        we need to pop all elements in `data` stack to `temp` stack and then add the 
        new element, and then pop all elements in `temp` stack into `data` stack so 
        that the newly pushed element is at the bottom while the first element to 
        be dequeued is at the top of the `data` stack.

        Time Complexity - O(N) - All elements are pushed twice and poped twice.
        Space Complexity - O(N) - Extra temp stack for storing all elements in the queue.
        """
        # Pop all elements in data stack into temp stack.
        while self.data:
            self.temp.append(self.data.pop())

        # Add the pushed element into temp stack.
        self.temp.append(x)

        # Pop all elements in temp stack back into data stack.
        while self.temp:
            self.data.append(self.temp.pop())

    def pop(self) -> int:
        """ Removes the element from in front of queue and returns that element.
        Time Complexity - O(1)
        Space Complexity - O(1)
        """
        if not self.empty():
            return self.data.pop()
        else:
            raise ValueError("No Elements in the Queue.")

    def peek(self) -> int:
        """ Get the front element.
        Time Complexity - O(1)
        Space Complexity - O(1)
        """
        if not self.empty():
            return self.data[-1]
        else:
            raise ValueError("Index Out of Range.")

    def empty(self) -> bool:
        """ Returns whether the queue is empty.
        Since `data` stack stores all the elements, so we only need to check `data`.
        Time Complexity - O(1)
        Space Complexity - O(1)
        """
        return not self.data

    def __repr__(self) -> str:
        result = []
        for element in self.data:
            result.append(str(element))
        return ", ".join(result)


############################################################
#  Two Stacks - Enqueue O(1) Dequeue with Amortized O(1)   #
############################################################
class MyAmortizedQueue:
    def __init__(self):
        """ Initialize your data structure here. """
        self.data = []
        self.temp = []

    def push(self, x: int) -> None:
        """ Push element x to the back of queue. """
        # Enqueue all elements into `data` stack.
        self.data.append(x)

    def pop(self) -> int:
        """ Removes the element from in front of queue and returns that element.
        Using `temp` stack to store elements to be poped.
        When dequeing elements, we need to check whether `temp` is empty, if not 
        we can return the top of `temp` stack, otherwise, we are going to pop out 
        all elements in `data` stack into `temp` stack and then return the top 
        element of `temp` stack.

        Time Complexity - Amortized O(1) - Since we move all elements from A to B
        once, then until all elements in B are poped, we don't need to do anything. 
        A is `data` stack here while B is the `temp` stack.

        Space Complexity - O(N) - Extra `temp` stack for storing all elements in the 
        queue.
        """
        # If the queue is empty, then raise error.
        if self.empty():
            raise ValueError("No Elements in the Queue.")

        # If there are no elements in temp stack then move all elements from 
        # data to temp.
        if not self.temp:
            while self.data:
                self.temp.append(self.data.pop())

        # Pop the element from temp stack.
        return self.temp.pop()

    def peek(self) -> int:
        """ Get the front element. """
        # If the queue is empty, then raise error.
        if self.empty():
            raise ValueError("No Elements in the Queue.")

        # Same as the pop() function, check if B is empty, if yes, pop out all 
        # elements in data stack into temp stack and the return the peek (front)
        # of the queue.
        if not self.temp:
            while self.data:
                self.temp.append(self.data.pop())
        
        return self.temp[-1]

    def empty(self) -> bool:
        """ Returns whether the queue is empty. """
        # Different from the normal method, we need to check whether both 
        # data and temp are empty to be sure the queue is empty.
        return not self.data and not self.temp

    def __repr__(self) -> str:
        """ Return the queue in string format, i.e. 
        end -> 2 -> 3 -> 1 -> front (to be dequeued).
        """
        result = []

        # All elements in data stack in reversed order.
        for element in self.data:
            result.insert(0, f"{element}")
        
        # All elements in temp stack
        for element in self.temp:
            result.append(f"{element}")

        return ", ".join(result)


if __name__ == "__main__":
    # For MyQueue with O(N) Enqueue
    my_quque = MyQueue()
    my_quque.push(1)
    my_quque.push(2)
    print(my_quque)
    peek = my_quque.peek()
    print(f"Peek: {peek}")
    poped = my_quque.pop()
    print(f"Poped Element: {poped}")
    print(my_quque)
    print(f"Check empty: {my_quque.empty()}")

    # For MyAmortizedQueue with O(1) Enqueue and Amortized O(1) Dequeue
    my_amortized_quque = MyAmortizedQueue()
    my_amortized_quque.push(1)
    my_amortized_quque.push(2)
    print(my_amortized_quque)
    peek = my_amortized_quque.peek()
    print(f"Peek: {peek}")
    poped = my_amortized_quque.pop()
    print(f"Poped Element: {poped}")
    print(my_amortized_quque)
    print(f"Check empty: {my_amortized_quque.empty()}")

