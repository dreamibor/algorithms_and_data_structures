"""
Linked List - Merge Two Sorted Lists (easy)

Description:
Merge two sorted linked lists and return it as a new sorted list. The new list 
should be made by splicing together the nodes of the first two lists.

Example:
Input: l1 = [1,2,4], l2 = [1,3,4]
Output: [1,1,2,3,4,4]

LeetCode link: https://leetcode-cn.com/problems/merge-two-sorted-lists/
"""
from linked_list import ListNode, create_linked_list, traverse


def merge_two_sorted_lists(l1: ListNode, l2: ListNode) -> ListNode:
    """ Iteration
    Time Complexity - O(N+M) - N, M are the total number of elements in the two 
    linked lists.
    Space Complexity - O(1) - For two pointers.
    """
    dummy = ListNode(-1)
    current = dummy

    while l1 and l2:
        if l1.val <= l2.val:
            current.next = l1
            l1 = l1.next
        else:
            current.next = l2
            l2 = l2.next
        
        current = current.next
    
    current.next = l1 if l1 else l2
    
    return dummy.next


def merge_two_sorted_lists_recursion(l1: ListNode, l2: ListNode) -> ListNode:
    """ Recursion
    Time Complexity - O(N+M) - N, M are the total number of elements in the two 
    linked lists.
    Space Complexity - O(N+M) - recursion stack.
    """
    # Stop condition: when l1 or l2 is empty.
    if l1 is None:
        return l2
    elif l2 is None:
        return l1
    
    if l1.val <= l2.val:
        # Merge l1's next node and l2 as l1's new next node.
        l1.next = merge_two_sorted_lists_recursion(l1.next, l2)
        return l1
    else:
        # Merge l2's next node and l1 as l2's new next node.
        l2.next = merge_two_sorted_lists_recursion(l1, l2.next)
        return l2


if __name__ == "__main__":
    l1 = create_linked_list([1,2,4,5])
    l2 = create_linked_list([1,3,4])
    new_head = merge_two_sorted_lists(l1, l2)
    print(traverse(new_head))

    l1 = create_linked_list([1,2,4,5])
    l2 = create_linked_list([1,3,4])
    merged = merge_two_sorted_lists_recursion(l1, l2)
    print(traverse(merged))