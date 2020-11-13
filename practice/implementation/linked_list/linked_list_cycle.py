"""
Linked List - Linked List Cycle (easy)

Description:
Given the head of a Singly LinkedList, write a function to determine if the 
LinkedList has a cycle in it or not.

Example:
Input: head = [3,2,0,-4], pos = 1 (cycle postion)
Output: True
Explanation: There is a cycle in the linked list, linking from the last node 
to the second node.

Notes:
1. We can use hash table to record the nodes we've seen, and check whether a 
node is already in the hash table. This will take O(N) for space complexity, 
so try with constant space complexity solution.

Time Complexity - O(N) - N is the total number of elements in the LinkedList.
Space Complexity - O(1) - For two pointers.

LeetCode link: https://leetcode-cn.com/problems/linked-list-cycle/
"""

from linked_list import ListNode, create_linked_list, traverse


def linked_list_cycle(head: ListNode) -> ListNode:
    """ Fast and Slow Pointers
    """
    slow, fast = head, head

    while fast and fast.next:
        fast = fast.next.next
        slow = slow.next

        if fast == slow:
            return True
        
    return False

def linked_list_cycle_hash_table(head: ListNode) -> ListNode:
    """ Hash Table
    Time Complexity - O(N) - N is the total number of elements in the LinkedList.
    Space Complexity - O(N) - For hash table (set).
    """
    current = head
    node_set = set()

    while current:
        if current in node_set:
            return True
        
        node_set.add(current)
        current = current.next

    return False

if __name__ == "__main__":
    head = ListNode(1)
    head.next = ListNode(2)
    head.next.next = ListNode(3)
    head.next.next.next = head.next
    print(linked_list_cycle(head))
    print(linked_list_cycle_hash_table(head))
