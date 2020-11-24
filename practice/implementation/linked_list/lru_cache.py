"""
Linked List - LRU Cache (medium)

Description:
Design a data structure that follows the constraints of a Least Recently Used (LRU) cache.

Implement the LRUCache class:
* LRUCache(int capacity) - Initialize the LRU cache with positive size capacity.
* int get(int key) - Return the value of the key if the key exists, otherwise return -1.
* void put(int key, int value) - Update the value of the key if the key exists. 
Otherwise, add the key-value pair to the cache. If the number of keys exceeds the capacity 
from this operation, evict the least recently used key.

Example:
Input:
["LRUCache", "put", "put", "get", "put", "get", "put", "get", "get", "get"]
[[2], [1, 1], [2, 2], [1], [3, 3], [2], [4, 4], [1], [3], [4]]
Output:
[null, null, null, 1, null, -1, null, -1, 3, 4]

Explanation:
LRUCache lRUCache = new LRUCache(2);
lRUCache.put(1, 1); // cache is {1=1}
lRUCache.put(2, 2); // cache is {1=1, 2=2}
lRUCache.get(1);    // return 1
lRUCache.put(3, 3); // LRU key was 2, evicts key 2, cache is {1=1, 3=3}
lRUCache.get(2);    // returns -1 (not found)
lRUCache.put(4, 4); // LRU key was 1, evicts key 1, cache is {4=4, 3=3}
lRUCache.get(1);    // return -1 (not found)
lRUCache.get(3);    // return 3
lRUCache.get(4);    // return 4

Notes:
Could you do get and put in O(1) time complexity?

LeetCode link: https://leetcode-cn.com/problems/lru-cache/
"""
class DoublyListNode:
    def __init__(self, key = 0, value = 0):
        self.key = key
        self.value = value
        self.prev = None
        self.next = None

class LRUCache:
    """ To implement a LRU cache, we need to use a hash table and a doubly linked list.
    In Python, there is a data structure called OrderedDict which already combines hash 
    table and doubly linked list. But usually, in an interview, we'll be asked to implement
    a doubly linked list by ourselves.

    Doubly linked list is used to store key-value pairs in the order of use (access). The node
    at the head is most recently used, while the node at the end is least recently used (LRU).

    We use hash table to store the data's key and it's location on the doubly linked list.

    When an element is accessed, we use hash table to locate it and then move the element to 
    the head of the list. 

    For the get() operation, first we check whether the key exist or not:
    1. If key doesn't exist, then return -1.
    2. If key exist, then the node corresponding to key will be the most recently used node,
    we use hash table to locate where the node is and then move it to the head of the list, and 
    finally return the value of the node.

    For the put() operation, we check whether the key exist or not as well:
    1. If the key doesn't exist, then create a key-value pair node and move it to the head. Also 
    save the key and the node into hash table, and we can see whether the number of nodes has 
    exceeded the capacity, if yes, we shall delete the node at the end, and delete the corresponding 
    item in hash table.
    2. If the key exists, then locate the node through hash table and update the value of the node 
    with new value, and move the node to the head.

    Note: We can ise a dummy head and a dummy tail to mark the bound, so that we don't need to check 
    whethere a neighbour node exist or not.

    Time Complexity - O(1) - For put() and get(), O(1) to access hash table, O(1) to add a node at 
    head and remove the node at tail. To move a node to head, there are two steps: 1. delete the node 
    and 2. add the node to head, both of them can be done with O(1).
    Space Complexity - O(capacity) - Since hash table and doubly linked list could save at most 
    capacity + 1 elements.
    """
    def __init__(self, capacity: int):
        self.capacity = capacity
        self.cache = {} # Hash table to store nodes.
        self.size = 0 # Actual size of elements.

        # Dummy head and dummy tail.
        self.head = DoublyListNode()
        self.tail = DoublyListNode()
        # Connect head and tail.
        self.head.next = self.tail
        self.tail.prev = self.head
    
    def __repr__(self) -> str:
        result = []
        for key, value in self.cache.items():
            result.append(f"[{key} - {value.value}]")
        return ", ".join(result)

    def get(self, key: int) -> int:
        if key not in self.cache: 
            return -1

        # If key exists, find it using hash table and then move it to head.
        node = self.cache[key]
        self.move_to_head(node)
        return node.value

    def put(self, key: int, value: int) -> None:
        if key not in self.cache:
            # If key doesn't exist, then create a new node.
            node = DoublyListNode(key, value)
            # Add the new node into hash table.
            self.cache[key] = node
            # Add it to head as it's most recently used.
            self.add_to_head(node)
            self.size += 1

            # Handle situation when current size is over capacity
            if self.size > self.capacity:
                # Remove the tail node
                removed = self.remove_tail()
                # Delete the tail node from hash table
                self.cache.pop(removed.key)
                self.size -= 1
        else:
            # If the key exist, then get the node and update the value.
            node = self.cache[key]
            node.value = value
            self.move_to_head(node)
    
    def add_to_head(self, node):
        """ Add a node to head position (with dummy head). """
        node.prev = self.head
        node.next = self.head.next
        self.head.next.prev = node
        self.head.next = node

    def remove_node(self, node):
        """ Remove a node from a doubly linked list. """
        node.prev.next = node.next
        node.next.prev = node.prev

    def move_to_head(self, node):
        """ Move a current node to head, it could be split into two steps:
            1. Remove the current node.
            2. Add it to head.
        """
        self.remove_node(node)
        self.add_to_head(node)
    
    def remove_tail(self):
        """ Remove tail node. """
        node = self.tail.prev
        self.remove_node(node)
        return node


if __name__ == "__main__":
    lru_cache = LRUCache(2)
    lru_cache.put(1, 1)  # cache is {1=1}
    print(lru_cache)
    lru_cache.put(2, 2)  # cache is {1=1, 2=2}
    lru_cache.get(1)     # return 1
    print(lru_cache)
    lru_cache.put(3, 3)  # LRU key was 2, evicts key 2, cache is {1=1, 3=3}
    print(lru_cache)
    lru_cache.get(2)     # returns -1 (not found)
    print(lru_cache)
    lru_cache.put(4, 4)  # LRU key was 1, evicts key 1, cache is {4=4, 3=3}
    lru_cache.get(1)     # return -1 (not found)
    lru_cache.get(3)     # return 3
    lru_cache.get(4)     # return 4
    print(lru_cache)