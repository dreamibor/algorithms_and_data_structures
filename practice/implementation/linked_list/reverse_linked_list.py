"""
Linked List - Reverse LinkedList Cycle (easy)

Description:
Reverse a singly linked list (in-place).

Example:
Input: 1->2->3->4->5->NULL
Output: 5->4->3->2->1->NULL

Notes:
1. Could we solve it with iteration?
2. Could we solve it with recursion?

LeetCode link: https://leetcode-cn.com/problems/reverse-linked-list/
"""
from linked_list import ListNode, traverse, create_linked_list


def reverse_linked_list(head:ListNode) -> ListNode:
    """ Reverse with iteration and two pointers.
    We can use two pointers to iterate through the linked list and reverse,
    a pointer called prev pointing to None at the beginning, a pointer called 
    current pointing to head. 

    Using a temp node to save nodes after the current node.

    Pointing the current node's next to prev to reverse the node, and move prev 
    and current one step further.
    
    Time Complexity - O(N) - Iterate through the list once.
    Space Complexity - O(1) - For two pointers.
    """
    prev, current = None, head

    while current:
        temp = current.next
        current.next = prev
        prev = current
        current = temp
    
    return prev

def reverse_linked_list_recursion(head: ListNode) -> ListNode:
    """ Reverse with recursion
    We can assume the following nodes (after head) have been reversed and we 
    only need to reverse the current node and current.next.

    It'll be hard for human beings to understand the full process of recursion, 
    as our brains are not designed to push many items in stack, so we need to 
    focus on one stage (see reverse_linked_list_single_case.jpg for reference), 
    rather than try to understand the full process.

    For a single stage: 
    Given an input node head, reverse the linked list starting with head, and 
    return the reversed new head.

    Time Complexity - O(N) - Iterate the list once.
    Space Complexity - O(N) - For recursion stack.
    """
    # Recursion stop condition.
    if head == None or head.next == None:
        return head
    
    # Reverse the following nodes. 
    # temp will be the last node or the head node for the reversed list.
    temp = reverse_linked_list_recursion(head.next)

    # Reverse - the next node after head shall point to head now.
    head.next.next = head

    # Pointing head to None to avoid dead loop.
    head.next = None

    # Always return the new head node.
    return temp


if __name__ == "__main__":
    head = create_linked_list([1, 2, 3, 4, 5])
    print(traverse(head))

    reversed_head = reverse_linked_list(head)
    print(traverse(reversed_head))

    reverted_head = reverse_linked_list_recursion(reversed_head)
    print(traverse(reverted_head))