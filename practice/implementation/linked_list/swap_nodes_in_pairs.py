"""
Linked List - Swap Nodes in Pairs (medium)

Description:
Given a linked list, swap every two adjacent nodes and return its head.
You may not modify the values in the list's nodes. Only nodes itself may be changed.

Example:
Input: head = [1,2,3,4]
Output: [2,1,4,3]

Solutions:
1. Iteration
2. Recursion

LeetCode Link: https://leetcode-cn.com/problems/swap-nodes-in-pairs/
"""
from typing import List, OrderedDict
from linked_list import ListNode, traverse, create_linked_list


def swap_nodes_in_pairs(head: ListNode) -> ListNode:
    # Create a dummy node pointing to head.
    dummy = ListNode(0)
    dummy.next = head
    current = dummy

    # Iterate through the list, starting from the dummy node
    # each time exchange the order of the two nodes after current.
    # Stop when there is only 0 or 1 node left.
    while current.next and current.next.next:
        # To avoid confusion, we can rename the two nodes to be 
        # exchanged as node1 and node2.
        node1 = current.next
        node2 = current.next.next

        # Exchange node1 and node2:
        # current.next pointing to node2
        current.next = node2
        # node1.next pointing to node2.next
        node1.next = node2.next
        # node2.next pointing to node 1
        node2.next = node1

        # Move current to node1, we will exchange the two nodes
        # after node1 in the next iteration.
        current = node1
    
    return dummy.next

def swap_nodes_in_pairs_recursion(head: ListNode) -> ListNode:
    # Stop condition, when there is only one node or there 
    # isn't a node in the list, then we can't swap, so return.
    if not head or not head.next:
        return head

    # Swap two nodes, head is the first node while new head is 
    # the second node.
    # First we use new_head to represent the second node
    new_head = head.next
    # Then we swap the nodes after the second head and it will 
    # be the next of head as head is moving to the position of 
    # the original second node.
    head.next = swap_nodes_in_pairs_recursion(new_head.next)
    # Pointing new_head's next to head as new_head has become 
    # the new first node.
    new_head.next = head

    # Return the swapped node new_head.
    return new_head
    

if __name__ == "__main__":
    odd_list = create_linked_list([1,2,3,4,5])
    print(traverse(odd_list))
    new_odd_list = swap_nodes_in_pairs(odd_list)
    print(traverse(new_odd_list))

    even_list = create_linked_list([1,2,3,4])
    print(traverse(even_list))
    new_even_list = swap_nodes_in_pairs(even_list)
    print(traverse(new_even_list))

    result = swap_nodes_in_pairs_recursion(new_even_list)
    print(traverse(result))