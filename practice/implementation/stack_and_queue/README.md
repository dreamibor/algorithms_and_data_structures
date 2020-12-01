# Stack and Queue

## Stack
A stack stores items in a **last-in, first-out (LIFO)** order. 
Operations:
- push() - O(1)
- pop()  - O(1)
- peek() - O(1)

All stack operations take O(1) time complexity.
The space complexity for stack is O(N).

You can implement a stack with a linked list or a dynamic array.

Applications:
1. The call stack for functions.
2. Depth First Search (DFS)
3. Web Broswer - move forward and backward.

## Queue
A queue stores items in a **first-in, first-out (FIFO)** order. 
Operations:
- enqueue() - O(1)
- dequeue() - O(1)
- peek()    - O(1)

All queue operations take O(1) time complexity. 
The space complexity for queue is O(N).

You can implement a stack with a linked list:
- To enqueue, insert at the tail of the linked list.
- To dequeue, remove at the head of the linked list.

Applications:
1. Breadth First Search (BFS)
2. Printers - using queues to manage printing jobs.
3. Web Servers - using queues to manage requests.

Problem List:
- [x] [Valid Parentheses](https://leetcode-cn.com/problems/valid-parentheses/)
- [x] [Implement Stack Using Queues](https://leetcode-cn.com/problems/implement-stack-using-queues/)
- [x] [Implement Queue Using Stacks](https://leetcode-cn.com/problems/implement-queue-using-stacks/)
