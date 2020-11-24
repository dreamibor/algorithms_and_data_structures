"""
Linked List - Reverse Nodes in k-Group (hard)

Description:
Given a linked list, reverse the nodes of a linked list k at a time and return its 
modified list. k is a positive integer and is less than or equal to the length of 
the linked list. If the number of nodes is not a multiple of k then left-out nodes, 
in the end, should remain as it is.

Example:
Input: head = [1,2,3,4,5], k = 2
Output: [2,1,4,3,5]

Notes:
1. Could you solve the problem in O(1) extra memory space?
2. You may not alter the values in the list's nodes, only nodes itself may be changed.

LeetCode link: https://leetcode-cn.com/problems/reverse-nodes-in-k-group/
"""
from linked_list import ListNode, traverse, create_linked_list


def reverse_between(head: ListNode, tail: ListNode) -> ListNode:
    """ Reverse nodes between [head, tail) with iteration.
    """
    prev, cur = None, head

    while cur != tail:
        temp = cur.next
        cur.next = prev
        prev = cur
        cur = temp
    
    return prev

def reverse_k_group_recursion(head: ListNode, k: int) -> ListNode:
    """ Recursion based method.
    For more details:
    https://leetcode-cn.com/problems/reverse-nodes-in-k-group/solution/
    di-gui-si-wei-ru-he-tiao-chu-xi-jie-by-labuladong/

    Time Complexity - O(N) - Iterate through the list once.
    Space Complexity - O(N) - For recursion stack.
    """
    if not head: return None

    a, b = head, head

    # Recursion stop condition
    # Whether the number of remaining nodes is larger 
    # than k, if not return the remaining nodes.
    for i in range(k):
        if not b:
            return head
        b = b.next
    
    # Reverse nodes [a,b).
    new_head = reverse_between(a, b)
    # Reverse remaining linked list.
    a.next = reverse_k_group_recursion(b, k)
    
    return new_head


def reverse(head: ListNode, tail: ListNode):
    """ Reverse a sub linked list and return new head and tail.
    """
    prev = tail.next
    cur = head

    while prev != tail:
        temp = cur.next
        cur.next = prev
        prev = cur
        cur = temp

    # tail becomes new head and head becomes new tail.
    # For example, the reversed tail and head will be:
    # tail (new head): 2 -> 1 -> 3 -> 4 -> 5 -> None
    # head (new tail): 1 -> 3 -> 4 -> 5 -> None
    return tail, head


def reverse_k_group_iteration(head: ListNode, k: int) -> ListNode:
    """ Iteration based method.
    We can take k nodes as a group, we can use a pointer current to point
    to the head node of each group, and each time, we move this head node 
    k steps until the end of the linked list. For each group, we can check 
    it's length is larger or equal to k, if yes, we reverse this group.

    Time Complexity - O(N) - Iterate through the list once.
    Space Complexity - O(1) - Constant pointers.
    """
    # Create a dummy node and pointing it to head.
    dummy = ListNode(-1)
    dummy.next = head

    # prev pointer to save the node before head.
    prev = dummy

    while head:
        # Iterate k elements, starting from prev.
        tail = prev

        # Check if the remaining part is smaller than k.
        for i in range(k):
            tail = tail.next
            # Return directly if the number remaining nodes is less than k.
            if not tail:
                return dummy.next

        # Temp node to save the next group.
        temp = tail.next

        # Reverse the current group.
        head, tail = reverse(head, tail)

        # Pointing prev to the new head
        prev.next = head
        # Pointing tail to the saved next group (temp).
        tail.next = temp

        # Move prev and head to next group.
        prev = tail
        head = tail.next

    return dummy.next


if __name__ == "__main__":
    head = create_linked_list([1,2,3,4,5])
    new_head = reverse_k_group_recursion(head, 2)
    print(traverse(new_head))

    head = create_linked_list([1,2,3,4,5])
    new_head = reverse_k_group_iteration(head, 2)
    print(traverse(new_head))