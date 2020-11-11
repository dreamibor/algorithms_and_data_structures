"""
LinkedList - Add Two Numbers (medium)

Description:
You are given two non-empty linked lists representing two non-negative integers. 
The digits are stored in reverse order, and each of their nodes contains a single 
digit. Add the two numbers and return the sum as a linked list.

You may assume the two numbers do not contain any leading zero, 
except the number 0 itself.

Example:
Input: l1 = [2,4,3], l2 = [5,6,4]
Output: [7,0,8]
Explanation: 342 + 465 = 807.

Notes:
1. The number's digits are saved in reverse order.
2. Need to consider special cases, such as two numbers have different number of 
digits, such as 123 + 45678; also there are some cases we need to carry a number 
once the previous sum of digits is >= 10.

Time Complexity - O(N) - N is the total number of elements in the LinkedList.
Space Complexity - O(1) - For two pointers.

LeetCode link: https://leetcode-cn.com/problems/add-two-numbers/
"""

class ListNode:
    # Define singly linked list.
    def __init__(self, value, next=None):
        self.value = value
        self.next = next

def traverse_linked_list(head: ListNode):
    result = []
    current = head
    while current:
        result.insert(0, current.value)
        current = current.next
    print(result)

def add_two_numbers(l1: ListNode, l2: ListNode) -> ListNode:
    carry = 0 # Carry one digit
    current = result = ListNode(0)
    
    while l1 or l2 or carry:
        # Calculate current sum
        cur_sum = (l1.value if l1 else 0) + (l2.value if l2 else 0) + carry
        carry = cur_sum // 10
        val = cur_sum % 10
        current.next = ListNode(val)
        current = current.next
        l1 = l1.next if l1 else None
        l2 = l2.next if l2 else None
    
    return result.next

if __name__ == "__main__":
    l1 = ListNode(2)
    l1.next = ListNode(4)
    l1.next.next = ListNode(3)
    traverse_linked_list(l1)
    l2 = ListNode(5)
    l2.next = ListNode(6)
    l2.next.next = ListNode(4)
    traverse_linked_list(l2)
    result = add_two_numbers(l1, l2)
    traverse_linked_list(result)

    l1 = ListNode(0)
    traverse_linked_list(l1)
    l2 = ListNode(0)
    traverse_linked_list(l2)
    result = add_two_numbers(l1, l2)
    traverse_linked_list(result)

    # Edge case, carry remain 1 after iterating through l1 and l2
    l1 = ListNode(9)
    l1.next = ListNode(9)
    l1.next.next = ListNode(9)
    l1.next.next.next = ListNode(9)
    l1.next.next.next.next = ListNode(9)
    l1.next.next.next.next.next = ListNode(9)
    l1.next.next.next.next.next.next = ListNode(9)
    traverse_linked_list(l1)
    l2 = ListNode(9)
    l2.next = ListNode(9)
    l2.next.next = ListNode(9)
    l2.next.next.next = ListNode(9)
    traverse_linked_list(l2)
    result = add_two_numbers(l1, l2)
    traverse_linked_list(result)