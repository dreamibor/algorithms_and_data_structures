"""
Two pointers - Remove Duplicates (easy)

Description:
Given a sorted linked list, delete all duplicates such that each element appear 
only once.

Example:
Input: 1->1->2->3->3
Output: 1->2->3

Notes:
1. The given linked list is sorted.

Time Complexity - O(N) - N is the total number of elements in the given linked list.
Space Complexity - O(1)

LeetCode Link: https://leetcode-cn.com/problems/remove-duplicates-from-sorted-list/
"""
from linked_list import ListNode, traverse, create_linked_list


def remove_duplicates_linked_list(head:ListNode) -> ListNode:
    # Edge case - the input linked list (head) is empty.
    if not head:
        return head

    current = head

    while current != None and current.next != None:
        if current.val == current.next.val:
            current.next = current.next.next
        else:
            current = current.next
    
    return head


"""
Description:
Write code to remove duplicates from an unsorted linked list.

Example:
Input: [1, 2, 3, 3, 2, 1]
Output: [1, 2, 3]

Notes:
1. The given linked list is unsorted.
2. Advance - Try to solve it without temporary buffer.

LeetCode Link: https://leetcode-cn.com/problems/remove-duplicate-node-lcci/
"""

def remove_duplicates_unsorted_linked_list(head: ListNode) -> ListNode:
    """ Using hash table (set here) to memorize seen values.
    Time Complexity - O(N) - N is the total number of elements in the given linked list.
    Space Complexity - O(N) - worst case, saving all elements into the hash table.
    """
    # Edge case - the input linked list (head) is empty.
    if not head:
        return head

    values = {head.val} # The first element is always seen as distinct.
    current = head

    # Since this is a singly linked list, so we can't access the previous node. However,
    # we can assume current as the previous node, then current.next will be the node itself, 
    # and the next node will be current.next.next.
    while current.next: # Equivalent to current.next != None
        if current.next.val in values:
            # If we've seen the value, skip this node.
            current.next = current.next.next
        else:
            # If it's unseen before, save it to the hash table and move to next node.
            values.add(current.next.val)
            current = current.next
    
    return head

def remove_duplicates_unsorted_linked_list_two_pointers(head: ListNode) -> ListNode:
    """ Using two pointers with two embedded loops, one loop to iterate through the list and 
    keep a reserved node, the second loop will start from the reserved node and iterate until 
    the end of the linked list, along the way, we'll remove all nodes with same values as the 
    reserved node.

    Time Complexity - O(N^2) - N is the total number of elements in the given linked list.
    Space Complexity - O(1) - no extra space used.
    """
    # Edge case - the input linked list (head) is empty.   
    if not head:
        return head

    reserved = head

    while reserved:
        current = reserved
        
        while current.next:
            if current.next.val == reserved.val:
                current.next = current.next.next
            else:
                current = current.next

        reserved = reserved.next

    return head

if __name__ == "__main__":
    # For remove duplicates in a sorted linked list
    head = create_linked_list([1,1,2,3,4])
    result = remove_duplicates_linked_list(head)
    print(f"New LinkedList: {traverse(result)}")

    # For remove duplicates in a unsorted linked list
    new_head = create_linked_list([1,2,3,3,2,1])
    new_result = remove_duplicates_unsorted_linked_list(new_head)
    print(f"New LinkedList: {traverse(new_result)}")

    # For remove duplicates in a unsorted linked list (two pointers, in-place)
    new_head_2 = create_linked_list([1,2,3,3,2,1])
    print(f"Old LinkedList: {traverse(new_head_2)}")
    new_result_2 = remove_duplicates_unsorted_linked_list_two_pointers(new_head_2)
    print(f"New LinkedList: {traverse(new_result_2)}")