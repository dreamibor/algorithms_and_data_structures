"""
Circular Linked List

Circular linked lists are a type of linked list in which the last node points 
back to the head of the list, instead of points to None.

Use cases for circular linked lists:
1. Going around each player's turn in a multiplayer game.
2. Managing the application life cycle in operating systems.
2. Implementing a [Fibonacci heap](https://en.wikipedia.org/wiki/Fibonacci_heap)

Advantage:
1. You can traverse the whole list at any node.

We need to define the starting point to traverse the list, otherwise 
we may end up in a infinite loop.
"""

class Node:
    def __init__(self, value, next=None):
        self.value = value
        self.next = next

    def __repr__(self):
        # Return a string containing a printable 
        # representation of an object. 
        return f"{self.value}"

class CircularLinkedList:
    def __init__(self):
        self.head = None

    
    def traverse(self, starting_point=None):
        # Set starting point to head if it's not provided.
        if not starting_point:
            starting_point = self.head
        
        node = starting_point

        while node and node.next != starting_point:
            yield node
            node = node.next
        
        # yield the last node
        yield node


if __name__ == "__main__":
    first = Node(1)
    second = Node(2)
    first.next = second
    third = Node(3)
    second.next = third
    third.next = first

    new_list = CircularLinkedList()
    new_list.head = first

    print(f"Nodes in the linked list: {[node for node in new_list.traverse(second)]}")