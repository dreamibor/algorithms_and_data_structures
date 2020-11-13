"""
Two pointers - Remove Duplicates (easy)

Description:
Given an array of sorted numbers, remove all duplicates from it. You should not 
use any extra space; after removing the duplicates in-place return the length of 
the subarray that has no duplicate in it.

Example:
Input: [2, 3, 3, 3, 6, 9, 9]
Output: 4
Explanation: The first four elements after removing the duplicates will be [2, 3, 6, 9].

Notes:
1. We should not use extra space, like space complexity O(N) is not allowed.
2. The array is sorted.

Time Complexity - O(N) - N is the total number of elements in the given array.
Space Complexity - O(1)

LeetCode link: https://leetcode-cn.com/problems/remove-duplicates-from-sorted-array/
"""


from typing import List


def remove_duplicates(arr: list) -> int:
    next_distinct_index = 1

    for i in range(1, len(arr)):
        if arr[next_distinct_index - 1] != arr[i]:
            arr[next_distinct_index] = arr[i]
            next_distinct_index += 1

    return next_distinct_index


"""
Description:
Given an unsorted array of numbers and a target ‘key’, remove all instances of 
‘key’ in-place and return the new length of the array.

Example:
Input: [3, 2, 3, 6, 3, 10, 9, 3], Key=3
Output: 4
Explanation: The first four elements after removing every 'Key' will be [2, 6, 10, 9].

Notes:
1. Unsorted array.
2. Remove elements in-place.

Time Complexity - O(N) - N is the total number of elements in the given array.
Space Complexity - O(1)
"""


def remove_target_element(arr:list, key:int) -> int:
    next_element_index = 0

    for num in arr:
        if num != key:
            arr[next_element_index] = num
            next_element_index += 1
    
    return next_element_index


"""
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

class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None

def traverse_linked_list(head: ListNode):
    result = []
    node = head
    while node != None:
        result.append(node.val)
        node = node.next
    return result

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
    # For remove duplicates
    print(f"Duplicates removed array length: {remove_duplicates([2, 3, 3, 3, 6, 9, 9])}")
    print(f"Duplicates removed array length: {remove_duplicates([2, 2, 2, 11])}")
    # For remove target values in-place
    print(f"Array new length: {remove_target_element([3, 2, 3, 6, 3, 10, 9, 3], 3)}")
    print(f"Array new length: {remove_target_element([2, 11, 2, 2, 1], 2)}")
    # For remove duplicates in a sorted linked list
    head = ListNode(1)
    head.next = ListNode(1)
    head.next.next = ListNode(2)
    head.next.next.next = ListNode(3)
    head.next.next.next.next = ListNode(3)
    result = remove_duplicates_linked_list(head)
    print(f"New LinkedList: {traverse_linked_list(result)}")
    # For remove duplicates in a unsorted linked list
    new_head = ListNode(1)
    new_head.next = ListNode(2)
    new_head.next.next = ListNode(3)
    new_head.next.next.next = ListNode(3)
    new_head.next.next.next.next = ListNode(2)
    new_head.next.next.next.next.next = ListNode(1)
    new_result = remove_duplicates_unsorted_linked_list(new_head)
    print(f"New LinkedList: {traverse_linked_list(new_result)}")
    # For remove duplicates in a unsorted linked list (two pointers, in-place)
    new_head_2 = ListNode(1)
    new_head_2.next = ListNode(2)
    new_head_2.next.next = ListNode(3)
    new_head_2.next.next.next = ListNode(3)
    new_head_2.next.next.next.next = ListNode(2)
    new_head_2.next.next.next.next.next = ListNode(1)
    print(f"Old LinkedList: {traverse_linked_list(new_head_2)}")
    new_result_2 = remove_duplicates_unsorted_linked_list_two_pointers(new_head_2)
    print(f"New LinkedList: {traverse_linked_list(new_result_2)}")