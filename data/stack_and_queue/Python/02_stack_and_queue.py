from __future__ import print_function
class Stack:
    def __init__(self):
        self.items = []

    def push(self,item):
        self.items.append(item)

    def pop(self):
        return self.items.pop()

    def peek(self):
        return self.items[self.size() - 1]

    def is_empty(self):
        return self.items == []

    def size(self):
        return len(self.items)


class Queue:
    def __init__(self):
        self.items = []

    def enqueue(self,item):
        self.items.insert(0,item)

    def dequeue(self):
        return self.items.pop()

    def is_empty(self):
        return self.items == []

    def size(self):
        return len(self.items)


class Deque:
    def __init__(self):
        self.items = []

    def add_front(self, item):
        self.items.append(item)

    def add_rear(self, item):
        self.items.insert(0, item)

    def remove_front(self):
        return self.items.pop()

    def remove_rear(self):
        return self.items.pop(0)

    def is_empty(self):
        return self.items == []

    def size(self):
        return len(self.items)

if __name__ == '__main__':
    print('Stack test:')
    stack = Stack()
    stack.push(2)
    stack.push(5)
    stack.push(10)
    print('peek of Stack: {}'.format(stack.peek()))
    print('Orginal Stack: {}'.format(stack.items))
    stack.pop()
    print('Poped Stack: {}'.format(stack.items))

    print('\nQueue test:')
    queue = Queue()
    queue.enqueue(2)
    queue.enqueue(5)
    queue.enqueue(10)
    print('Orginal Queue: {}'.format(queue.items))
    print('Dequeued Elemnet: {}'.format(queue.dequeue()))
    print('Dequeued Queue: {}'.format(queue.items))

    print('\nDeque test:')
    deque = Deque()
    deque.add_front(2)
    deque.add_rear(5)
    deque.add_rear(10)
    print('Orginal Deque: {}'.format(deque.items))
    deque.remove_rear()
    print('Removed Rear Deque: {}'.format(deque.items))
    deque.remove_front()
    print('Removed Front Deque: {}'.format(deque.items))
