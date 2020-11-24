"""
Two pointers - Remove Duplicates from Sorted List II (medium)

Description:
Given a sorted linked list, delete all nodes that have duplicate numbers, leaving only 
distinct numbers from the original list.
Return the linked list sorted as well.

Example:
Input: 1->2->3->3->4->4->5
Output: 1->2->5
Explanation: 3 and 4 appeared more than once.

Notes:
1. The first node could be a duplicate number and it could be deleted.

Time Complexity - O(N) - N is the total number of elements in the given array.
Space Complexity - O(1)

LeetCode link: https://leetcode-cn.com/problems/remove-duplicates-from-sorted-list-ii/
"""

from linked_list import ListNode, create_linked_list, traverse


def delete_duplicates(head: ListNode) -> ListNode:
    """ Two pointers
    To handle cases where the first node is also a duplicated node, we can 
    use dummy node to handle this. Firstly, we define two pointers `a` and 
    `b`, where `a` pointing to the dummy node, and `b` pointing to the head 
    node. 

    If the node `a` pointing to has a different value comparing to the node 
    `b` is pointing to, then both `a` and `b` move forward for one step. If 
    the values are the same, then only move `b`, and `b` keeps moving until 
    the values are different.

    Here we are comparing a.next.val == b.next.val. While the values that 
    the two pointers are pointing to are equal, we can use a while loop to
    keep `b` moving until we've filtered duplicated nodes.

    Here `a` is called `preserve` and `b` is called `current`.
    
    Time Complexity - O(N) - Iterate the linked list once.
    Space Complexity - O(1) - Constant space for pointers.
    """
    # Edge cases, empty list or single element list.
    if not (head and head.next): return head

    # Create dummy node pointing to head.
    dummy = ListNode(0)
    dummy.next = head

    preserve = dummy
    current = head

    while current and current.next:
        # If the nodes have different values, move forward one step.
        if preserve.next.val != current.next.val:
            preserve = preserve.next
            current = current.next
        else:
            # If the nodes have same values, then move current node until preseve and current 
            # pointing to different values. Exclude all those nodes have same values.
            while current and current.next and preserve.next.val == current.next.val:
                current = current.next
            preserve.next = current.next
            current = current.next

    return dummy.next


def delete_duplicates_three_pointers(head: ListNode) -> ListNode:
    """ Three pointers
    The solution is similar to the two pointers one. The difference is in this 
    method, we are using `b` pointing to head.next rather than head. So to compare 
    whether two nodes have same values, we need to use: a.next.val == b.val.

    When the two pointers are pointing to different values, both a and b move forward 
    one step, while when they pointing to same values, there are some differentce.
    1. a.next pointing to b now;
    2. Pointer b has to handle bound problems, where b could be None, so we can't use 
    b = b.next directly, instead we have to see if b is already Nonem, so we won't get 
    an None has no next property error.

    Here `a` is called `preserve` and `b` is called `current`.

    Time Complexity - O(N) - Iterate the linked list once.
    Space Complexity - O(1) - Constant space for pointers.

    """
    # Edge cases, empty list or single element list.
    if not (head and head.next): return head

    # Create dummy node pointing to head
    dummy = ListNode(-1)
    dummy.next = head

    preserve = dummy
    current = head.next

    # Current could be None, such as 1 -> 1.
    while current:
        # If the nodes have different values, move forward one step.
        if preserve.next.val != current.val:
            preserve = preserve.next
            current = current.next
        else:
            # If the nodes have same values, then move current node until preseve and current 
            # pointing to different values.
            while current and preserve.next.val == current.val:
                current = current.next
            # Different from two pointers solution, here a.next pointing to b.
            preserve.next = current
            # Current could pointing to None after the while loop before.
            current = current.next if current else None
        
    return dummy.next

if __name__ == "__main__":
    head = create_linked_list([1,2,3,3,4,4,5])
    result = delete_duplicates(head)
    print(traverse(result))

    head = create_linked_list([1,2,3,3,4,4,5])
    result = delete_duplicates_three_pointers(head)
    print(traverse(result))