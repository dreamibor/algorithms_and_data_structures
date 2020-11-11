""" 
Doubly Linked List

Doubly linked list have two references to other nodes:
1. The previous reference pointing to the previous node.
2. The next reference pointing to the next node.

Advantage:
With doubly linked list, we can insert at the end or at the beginning
of the linked list with constant time complexity - O(1).

"""

# Defince doubly linked list
class DoublyListNode:
    def __init__(self, value, prev=None, next=None):
        self.value = value
        self.prev = prev
        self.next = next

