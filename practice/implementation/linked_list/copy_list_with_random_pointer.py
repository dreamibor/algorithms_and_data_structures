"""
Linked List - Partition List (medium)

Description:
A linked list is given such that each node contains an additional random pointer 
which could point to any node in the list or null.

Return a `deep copy` of the list.

The Linked List is represented in the input/output as a list of n nodes. Each node 
is represented as a pair of [val, random_index] where:
1. val: an integer representing Node.val
2. random_index: the index of the node (range from 0 to n-1) where random pointer 
points to, or null if it does not point to any node.

Example:
Input: [[7,null],[13,0],[11,4],[10,2],[1,0]]
Output: [[7,null],[13,0],[11,4],[10,2],[1,0]]

LeetCode link: https://leetcode-cn.com/problems/copy-list-with-random-pointer/
"""


class Node:
    def __init__(self, x: int, next: 'Node' = None, random: 'Node' = None):
        self.val = int(x)
        self.next = next
        self.random = random

    def __repr__(self) -> str:
        return f"[{self.val}, {self.next}]"

def copy_random_list_hash_table(head: Node) -> Node:
    """ Hash Table
    We can use a hash table to save original nodes and copied nodes. 
    We iterate the list for first time save all nodes and copied nodes 
    into the hash table. The key will be the original node, while the 
    value will be the newly created node (copied node with next and 
    random as None).

    Then we can iterate the original list to update all next and random 
    pointers for those newly created nodes, as:
    map.get(original) -> returns the newly copied node.
    map.get(original.next) -> returns the newly copied node's next.
    map.get(original.random) -> returns the newly copied node's random.

    So we can assign those nodes to:
    1. node_map[current].next = node_map[current.next]
    2. node_map[current].random = node_map[current.random]

    Finally, we can return the result by map.get(head).

    Time Complexity - O(N) - For iteration twice.
    Space Complexity - O(N) - For the hash table.
    """
    # Edge case - for empty list.
    if not head: return None

    node_map = {}
    current = head

    # Iterate through the linked list, add all nodes into hash table 
    # with original node as key and newly created node (copied node) 
    # as value.
    while current:
        new_node = Node(current.val, None, None)
        node_map[current] = new_node
        current = current.next

    current = head

    # Update those newly created nodes' next and random.
    # The original node's next will be a key to get the newly copied 
    # node's next. It will be the same for random pointer.
    while current:
        if current.next:
            node_map[current].next = node_map[current.next]
        
        if current.random:
            node_map[current].random = node_map[current.random]

        current = current.next
    
    return node_map[head]


def copy_random_list(head: Node) -> Node:
    """ Copy after Original Nodes and Then Split

    The most difficult part of this problem is how to copy the random 
    pointer.

    We can solve the problem with three steps:
    1. Iterate through original nodes, create a copy node after each 
    original node, so the original node 1 is pointing to newly created 
    copy node 1' rather than orginal node 2.
    2. Set new nodes' random pointers.
    - If the original node 1's random pointer is pointing to the original 
    node 3, then the random pointer of new copy node 1' is pointing to 
    the original node 3's next. In general, the original i's random pointer 
    is pointing to original node j, then the copied node i's random pointer 
    will point to j's next.
    3. Split the list into the original list and the copied list and then 
    return the new list.

    Time Complexity - O(N) - Iterate the list.
    Space Complexity - O(1) - Constant space for pointers.
    """
    # Edge case - empty list
    if not head: return head

    # Create copied nodes after original nodes.
    # 1 -> 1' -> 2 -> 2' -> 3 -> 3'
    current = head
    while current:
        new_node = Node(current.val, None, None)
        new_node.next = current.next
        current.next = new_node
        current = new_node.next
    
    # Set random pointers for new copied nodes.
    current = head
    while current:
        if current.random:
            current.next.random = current.random.next
        current = current.next.next

    # Split two lists
    # 1  -> 2  -> 3
    # 1' -> 2' -> 3'
    current = head
    dummy = Node(-1, None, None)
    cur = dummy

    while current:
        cur.next = current.next
        cur = cur.next
        current.next = cur.next
        current = current.next
    
    return dummy.next


if __name__ == "__main__":
    head = Node(3)
    head.next = Node(2)
    head.random = None
    head.next.next = Node(1)
    head.next.random = head
    head.next.next.random = None

    new_head = copy_random_list_hash_table(head)
    while new_head:
        print(new_head)
        new_head = new_head.next
    
    new_head = copy_random_list(head)
    while new_head:
        print(new_head)
        new_head = new_head.next