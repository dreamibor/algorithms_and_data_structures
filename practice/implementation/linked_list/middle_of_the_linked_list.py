"""
Fast and slow pointers - Middle of the LinkedList (easy)

Description:
Given the head of a Singly LinkedList, write a method to return the middle 
node of the LinkedList. If the total number of nodes in the LinkedList is 
even, return the second middle node.

Example:
Input: 1 -> 2 -> 3 -> 4 -> 5 -> null
Output: 3

Time Complexity - O(N) - N is the total number of elements in the linked list.
Space Complexity - O(1) - For two pointers.

LeetCode link: https://leetcode-cn.com/problems/middle-of-the-linked-list/
"""
from linked_list import ListNode, create_linked_list


def find_middle_of_linked_list(head: ListNode) -> ListNode:
    """ Solution - Fast & Slow Pointers
    We can use two pointers to iterate through the linked list, slow walks one 
    step each time while fast walks two steps, so while fast has reached the end 
    of the linked list, slow must be in the middle of the linked list.
    """
    fast, slow = head, head

    while fast and fast.next:
        fast = fast.next.next
        slow = slow.next

    return slow

def find_middle_traverse_twice(head: ListNode) -> ListNode:
    """ Solution - Twice Traversal
    We can iterate through the linked list twice, the first time we will record the 
    length of the linked list N, and at the second traversal, we will iterate until 
    N/2 and return the node.
    Time Comlexity - O(N) - N is the number of nodes in the linked list.
    Space Complexity - O(1) - Constant space for variable and pointer.
    """
    list_len = 0
    current, second = head, head
    
    while current:
        list_len += 1
        current = current.next
    
    i = 0
    while i < list_len // 2:
        i += 1
        second = second.next

    return second

if __name__ == "__main__":
    head = create_linked_list([1,2,3,4,5])

    print("Middle Node: " + str(find_middle_of_linked_list(head).val))
    print("Middle Node: " + str(find_middle_traverse_twice(head).val))

    head.next.next.next.next.next = ListNode(6)
    print("Middle Node: " + str(find_middle_of_linked_list(head).val))
    print("Middle Node: " + str(find_middle_traverse_twice(head).val))

    head.next.next.next.next.next.next = ListNode(7)
    print("Middle Node: " + str(find_middle_of_linked_list(head).val))
    print("Middle Node: " + str(find_middle_traverse_twice(head).val))

    head.next.next.next.next.next.next.next = ListNode(8)
    print("Middle Node: " + str(find_middle_of_linked_list(head).val))
    print("Middle Node: " + str(find_middle_traverse_twice(head).val))