from collections import deque
import unittest

class Stack():
    def __init__(self):
        self.items = deque()

    def push(self, data):
        self.items.append(data)

    def is_empty(self):
        return self.items == deque([])

    def pop(self):
        if not self.is_empty():
            return self.items.pop()
        else:
            raise ValueError("No Elements to Pop Out!")

    def __str__(self):
        out = "[ "
        for i in self.items:
            out += "{} ".format(i)
        out += "]"
        return out

class Queue():
    def __init__(self):
        self.items = deque()

    def enqueue(self, data):
        self.items.append(data)

    def dequeue(self):
        if not self.is_empty():
            return self.items.popleft()
        else:
            raise ValueError("No Elements to Pop Out!")

    def is_empty(self):
        return self.items == deque([])

    def __str__(self):
        out = "[ "
        for i in self.items:
            out += "{} ".format(i)
        out += "]"
        return out

class QueueWithTwoStacks():
    def __init__(self):
        self.stack1 = Stack()
        self.stack2 = Stack()

    def enqueue(self, data):
        self.stack1.push(data)

    def _shift_stack(self):
        if self.stack2.is_empty():
            while not self.stack1.is_empty():
                self.stack2.push(self.stack1.pop())

    def dequeue(self):
        self._shift_stack()
        return self.stack2.pop()

stack = Stack()
stack.push(56)
stack.push(45)
stack.push("a")
print("After Push In Three Elements: {}".format(stack))
stack.pop()
stack.pop()
print("After Pop Out Two Elements: {}".format(stack))

queue = Queue()
queue.enqueue(56)
queue.enqueue(67)
queue.enqueue("a")
print(queue)
queue.dequeue()
print(queue)

stack_queue = QueueWithTwoStacks()
stack_queue.enqueue(56)
stack_queue.enqueue(89)

print(stack_queue.dequeue())
print(stack_queue.dequeue())


def balancedParentheses(test_str):
    parens = {'}':'{', ']':'[', ')':'('}
    stack = Stack()
    for i in test_str:
        if i in parens.values():
            stack.push(i)
        else:
            if stack.is_empty() or parens[i]!= stack.pop():
                return False
    return stack.is_empty()

print(balancedParentheses("{[()[]]}"))
print(balancedParentheses("{[])}"))



class TestStackQueue(unittest.TestCase):
    def setUp(self):
        self.stack = Stack()
        self.queue = Queue()
        self.stack.push(56)
        self.stack.push(37)
        self.queue.enqueue(89)
        self.queue.enqueue(78)

    def test_pop(self):
        self.assertEqual(self.stack.pop(), 37)

    def test_dequeue(self):
        self.assertEqual(self.queue.dequeue(), 89)

    def test_empty(self):
        self.assertTrue(not self.stack.is_empty())
        self.assertTrue(not self.queue.is_empty())

if __name__ == "__main__":
    unittest.main()        