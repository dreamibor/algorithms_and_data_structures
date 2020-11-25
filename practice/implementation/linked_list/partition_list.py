"""
Linked List - Partition List (medium)

Description:
Given a linked list and a value x, partition it such that all nodes less than x come before 
nodes greater than or equal to x.

Example:
Input: head = 1->4->3->2->5->2, x = 3
Output: 1->2->2->4->3->5

Note:
You should preserve the original relative order of the nodes in each of the two partitions.

LeetCode link: https://leetcode-cn.com/problems/partition-list/
"""

from linked_list import ListNode, create_linked_list, traverse


def partition_list(head: ListNode, x: int) -> ListNode:
    """ Break Down and Concatenate
    We can break down the list into two parts:
    1. Nodes have value smaller than x;
    2. Nodes have value larger than or equal to x.


    Time Complexity - O(N) - Iterate through the list once.
    Space Complexty - O(1) - For pointers.
    """
    # Use two dummy nodes to store two break-down lists.
    s = smaller = ListNode(-1)
    l = larger = ListNode(-1)

    while head:
        if head.val < x:
            s.next = head
            s = s.next
        else:
            l.next = head
            l = l.next
        head = head.next

    # Last node of larger is the end. 
    l.next = None
    # Concatenate two lists, as smaller will be followed by larger.
    s.next = larger.next

    return smaller.next
    

if __name__ == "__main__":
    head = create_linked_list([1,4,3,2,5,2])
    result = partition_list(head, 3)
    print(traverse(result))
