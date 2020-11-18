"""
Linked List - Palindrome Linked List (medium)

Decription:
Given the head of a Singly LinkedList, write a method to check if the LinkedList is a 
palindrome or not.

Example:
Input: 2 -> 4 -> 6 -> 4 -> 2 -> null
Output: true

Notes:
1. We shall use constant space and the linked list shall be in the original form after 
the algorithm is finished.
1. The algorithm shall have O(N) time complexity.

LeetCode Link: https://leetcode-cn.com/problems/palindrome-linked-list/
"""
from linked_list import ListNode, create_linked_list


def check_palindrome(head: ListNode) -> bool:
    """ Solution: Find Middle Node and Reverse Second Half
    We can find the middle node first using fast and slow pointers, then we can 
    reverse the second half of the linked list, we then compare the reversed 
    second half with the first half one by one.

    Time Complexity - O(N) - Linearly iterate through the list.
    Space Complexity - O(1) - for pointers.
    """
    if not head or not head.next:
        return True
    
    # Find the middle of the linked list.
    fast, slow = head, head
    number = 0

    while fast and fast.next:
        number = number * 10 + slow.val
        slow = slow.next
        fast = fast.next.next

    # Reverse the second half.
    second_half_head = reverse_linked_list(slow)
    # Set two temp pointers for iteration.
    cur = head
    second_cur = second_half_head

    # Compare the reversed second half with the first half.
    while cur and second_cur:
        if cur.val != second_cur.val:
            return False
        
        cur = cur.next
        second_cur = second_cur.next
    
    # Reverse the second half back.
    reverse_linked_list(second_half_head)

    return True


def reverse_linked_list(head: ListNode) -> ListNode:
    """ Reverse a linked list using recursion.
    """
    if not head or not head.next:
        return head
    
    temp = reverse_linked_list(head.next)
    head.next.next = head
    head.next = None

    return temp

#################################################################

class Solution:
    def __init__(self):
        # To avoid using global variables, we can use a class to encapsulate 
        # the variables.
        pass

    def check_palindrome_recursion(self, head: ListNode) -> bool:
        """ Iterate the linekd list reversely using recursion and use 
        an external (global) variale to iterate normally, then compare 
        the numbers to determine whether it's a palindrome.

        Time complexity - O(N) - iterate through the linked list.
        Space complexity - O(N) - for the recursion stack.
        """
        self.temp = head

        def check(head: ListNode) -> bool:
            if head is None: return True

            # All previous nodes match and current node's value match.
            res = check(head.next) and (self.temp.val == head.val)
            self.temp = self.temp.next
            return res

        return check(head)

#################################################################

def check_palindrome_array(head: ListNode) -> bool:
    """ Convert to array and then compare.

    Time complexity - O(N) - Iterate through the result once and compare once.
    Space complexity - O(N) - N for storing the values in array.
    """
    result = []

    if not head: return True

    while head:
        result.append(head.val)
        head = head.next
    
    return result == result[::-1]

#################################################################

def check_palindrome_positive(head: ListNode) -> bool:
    """ ONLY WOKRS FOR POSITIVE NUMBERS
    Accumulate first half number and then compare, will fail 
    for test cases such as [-129, -129].
    """
    # Edge cases, empty list.
    if not head: return True

    fast, slow = head, head
    number = 0

    while fast and fast.next:
        number = number * 10 + slow.val
        fast = fast.next.next
        slow = slow.next
    
    # Whether the linked list has even or odd number of nodes.
    if fast:
        slow = slow.next
    
    while slow:
        number, res = divmod(number,10)
        if slow.val != res:
            return False
        slow = slow.next
    
    return True


if __name__ == "__main__":
    head = create_linked_list([1,2,3,2,1])
    print(f"Palindrome: {check_palindrome(head)}")

    head = create_linked_list([1,2,2,1])
    print(f"Palindrome: {check_palindrome(head)}")

    head = create_linked_list([1,2])
    print(f"Palindrome: {check_palindrome(head)}")

    head = create_linked_list([1,2,3,2,1])
    print(f"Palindrome: {check_palindrome_array(head)}")
    
    head = create_linked_list([1,2])
    print(f"Palindrome: {check_palindrome_array(head)}")

    solution = Solution()
    head = create_linked_list([1,2,3])
    print(f"Palindrome: {solution.check_palindrome_recursion(head)}")
    