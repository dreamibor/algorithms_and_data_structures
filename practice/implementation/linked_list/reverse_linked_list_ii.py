"""
Linked List - Reverse Linked List II (medium)

Description:
Reverse a linked list from position m to n. Do it in one-pass.

Note: 1 ≤ m ≤ n ≤ length of list.

Example:
Input: 1->2->3->4->5->NULL, m = 2, n = 4
Output: 1->4->3->2->5->NULL

LeetCode link: https://leetcode-cn.com/problems/reverse-linked-list-ii/
"""
from linked_list import ListNode, create_linked_list, traverse


def reverse_between(head: ListNode, m: int, n: int) -> ListNode:
    """ Iteration based method

    Disadvantage: there are many details involved to process 
    the algorithm correctly.

    Time Complexity - O(N) - Iterate through the list once.
    Space Complexity - O(1) - Constant space for pointers.
    """
    # Edge case - empty list
    if not head: return head

    # Two pointers used to reverse the sub-linked list.
    prev = None
    cur = head

    # Iterate to the beginning of sub list to be reversed.
    while m > 1:
        # Move prev to current and current to current.next
        prev = cur
        cur = cur.next
        # Update both m and n
        m, n = m - 1, n - 1

    # Two pointers used to fix the final connections.
    # tail is the first node of the sub list and it will be the 
    # last node in the reversed list, con will be the node before 
    # the beginning node of the sub list, it could be None.
    tail, con = cur, prev

    # Iteratively reverse the nodes between m and n.
    while n:
        temp = cur.next
        cur.next = prev
        prev = cur
        cur = temp
        n -= 1
    
    # Adjust the final connections.
    if con:
        con.next = prev
    else:
        head = prev
    
    tail.next = cur

    return head

# Global variable for successor node.
successor = None

def reverse_n(head: ListNode, n: int) -> ListNode:
    """ Reverse N previous nodes in a linekd list from 1 to N.
    """
    global successor

    if n == 1:
        # Record N+1 node and mark it as successor.
        successor = head.next
        # Return the current node which will the new head.
        return head

    # Reverse N-1 previous nodes, starting from head.next
    last = reverse_n(head.next, n - 1)

    # Reverse the node after head to point to head
    print(head.val)
    head.next.next = head

    print(successor.val)
    # Connect the reversed new head node with successor.
    head.next = successor

    return last


def reverse_between_recursion(head: ListNode, m:int, n:int) -> ListNode:
    """ Reverse using recursion
    Assuming m - 1 is the first node and the folling will be similar to 
    reverse the previous N nodes.
    """
    # Stop condition
    if m == 1:
        return reverse_n(head, n)

    # Move foward until m - 1 is 1.
    head.next = reverse_between_recursion(head.next, m-1, n-1)

    return head


if __name__ == "__main__":
    head = create_linked_list([1,2,3,4,5])
    new_head = reverse_between(head, 2, 4)
    print(traverse(new_head))

    head = create_linked_list([7,9,2,10,1,8,6])
    new_head = reverse_between(head, 3, 6)
    print(traverse(new_head))

    head = create_linked_list([1,2,3,4,5])
    new_head = reverse_between_recursion(head, 2, 4)
    print(traverse(new_head))