"""
Linked List

The main difference between arrays and linked lists is arrays are stored in a 
continuous memory block while linked lists hold their own references to next 
element.

Each element of a linked list is called a `node`. For a singly linked list, 
each node has two fields: 
1. value - where the actual data is stored.
2. next - contains a reference to the next node on the list.

The first node is called `head`, as it's the starting point for the list. 
The last node will have a next reference as `None` to end the list.

Advantage comparing to arrays:
1. Insertion and Deletion - Constant time complexity O(1) - Since the better 
performance on insertion and deletion, linked lists could be used to implement 
queue (FIFO), in which elements are continuously inserted and removed at the 
beginning of the list. However, linked lists will perform similarly to an array 
when implementing a stack (LIFO), in which elements are inserted and removed at 
the end of the list.

Disadvantage comparing to arrays:
1. Retrieval of Elements - Arrays perform much better than linked lists, since 
arrays will take O(1) while for linked lists, the time complexity will be O(N). 

When searching for a specific element, both arrays and linked lists will take 
O(N), since in both cases, we need to iterate through the entire list to find 
the element we are looking for.

Reference: https://realpython.com/linked-lists-python/
"""


# Define Singly Linked List Node
class Node:
    def __init__(self, value, next=None):
        self.value = value
        self.next = next

    def __repr__(self):
        # Return a string containing a printable 
        # representation of an object. 
        return f"{self.value}"

# Define Singly Linked List
class LinkedList:
    def __init__(self, nodes=None):
        self.head = None
        
        # Quickly create linked lists with a list
        if nodes:
            node = Node(nodes.pop(0))
            self.head = node

            for element in nodes:
                node.next = Node(element)
                node = node.next
        
    def __repr__(self):
        """ Return a string representing the linked list.
        For example: a -> b -> c -> None
        """
        node = self.head
        nodes = []

        while node:
            # Convert the node value to string
            # so it can be `join`ed later.
            nodes.append(f"{node.value}")
            node = node.next
        
        nodes.append("None")
        return " -> ".join(nodes)

    def __iter__(self):
        """ Traverse - iterate through the linked list
        """
        node = self.head
        while node:
            yield node
            node = node.next

    def append_start(self, node):
        """ Add a node at the beginning of the linked list.
        """
        node.next = self.head
        self.head = node
    
    def append_end(self, node):
        """ Add a node at the end of the linked list. 
        """
        # If head is None
        if not self.head:
            self.head = node

        current = self.head
        while current.next:
            current = current.next

        current.next = node

    def insert(self, index, node):
        current = self.head

        while index:
            current = current.next
            index -= 1
       
        node.next = current.next
        current.next = node

    def remove(self, data):
        # Handle empty lise
        if not self.head:
            raise Exception("Empty list!")
        
        # If head' value is as the input value.
        if self.head.value == data:
            self.head = self.head.next

        current = self.head
        while current.next:
            if current.next.value == data:
                current.next = current.next.next
                break
            current = current.next




if __name__=="__main__":
    new_list = LinkedList([1,2,3,4,5,6])
    print(f"Linked List: {new_list}")
    print(f"Nodes in the linked list: {[node for node in new_list]}")
    new_list.append_start(Node(0))
    print(f"Linked List: {new_list}")
    new_list.append_end(Node(7))
    print(f"Linked List: {new_list}")
    new_list.insert(3, Node(9))
    print(f"Linked List: {new_list}")
    new_list.remove(9)
    print(f"Linked List: {new_list}")

