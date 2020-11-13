"""
Linked List - Reverse LinkedList Cycle (easy)

Description:
Reverse a singly linked list (in-place).

Example:
Input: 1->2->3->4->5->NULL
Output: 5->4->3->2->1->NULL

LeetCode link: https://leetcode-cn.com/problems/reverse-linked-list/

"""
from linked_list import ListNode, traverse, create_linked_list


def reverse_linked_list(head:ListNode) -> ListNode:
    """ Reverse with iteration
    
    """
    prev, current = None, head

    while current:
        temp = current.next
        current.next = prev
        prev = current
        current = temp
    
    return prev

def reverse_linked_list_recursion(head: ListNode) -> ListNode:
    """
    """
    if head == None or head.next == None:
        return head
    
    temp = reverse_linked_list_recursion(head.next)

    head.next.next = head

    head.next = None

    return temp



if __name__ == "__main__":
    head = create_linked_list([1, 2, 3, 4, 5])
    print(traverse(head))
    reversed_head = reverse_linked_list(head)
    print(traverse(reversed_head))
    reverted_head = reverse_linked_list_recursion(reversed_head)
    print(traverse(reverted_head))