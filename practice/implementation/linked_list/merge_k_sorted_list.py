"""
Linked List: Merge K Sorted Lists (hard)

Description:
You are given an array of k linked-lists lists, each linked-list is 
sorted in ascending order. 
Merge all the linked-lists into one sorted linked-list and return it.

Example:
Input: lists = [[1,4,5],[1,3,4],[2,6]]
Output: [1,1,2,3,4,4,5,6]
Explanation: The linked-lists are:
[
  1->4->5,
  1->3->4,
  2->6
]
merging them into one sorted list:
1->1->2->3->4->4->5->6

Solutions:
1. Brute force - Add all nodes in all lists into one list and then sort.
2. Brute force - Merge list one by one.
3. Divide and conquer - Merge half and half's half, ...
4. Priority queue - Get minimum element each time.

Notes:
For the priority queue based method, we need to 

LeetCode Link: https://leetcode-cn.com/problems/merge-k-sorted-lists/
"""
from linked_list import ListNode, create_linked_list, traverse
import heapq
# import sys
# sys.setrecursionlimit(2000)


def merge_two_sorted_lists(l1: ListNode, l2: ListNode) -> ListNode:
    """ Merge two sorted lists.
    """
    if not l1: return l2
    if not l2: return l1

    if l1.val <= l2.val: 
        l1.next = merge_two_sorted_lists(l1.next, l2)
        return l1
    else:
        l2.next = merge_two_sorted_lists(l1, l2.next)
        return l2

def merge(input_lists: list, left: int, right: int) -> ListNode:
    """ Divide and Conquer - divide the input lists into half and 
    process them and then merge them together.
    """
    if left == right: return input_lists[left]

    mid = left + (right - left) // 2

    l1 = merge(input_lists, left, mid)
    l2 = merge(input_lists, mid+1, right)

    return merge_two_sorted_lists(l1, l2)


def merge_k_lists_divide_and_conquer(input_lists: list) -> ListNode:
    """ Solution - Divide and Conquer
    We can merge lists in pairs, suppose we have k lists at the beginning, 
    then we can merge list pairs for the first round, so we will have k/2 
    merged lists, repeat the process, until we have the final one sorted list.

    Time Complexity - O(kn*logk) - the first round merging k/2 pair of lists, 
    the time complexity is O(2n) for each pair, the second round merging k/4 
    pair of lists, and the time complexty for each pair is O(4n), ... in total 
    the time complexity is O(kn*logk).
    Space Complexity - O(logk) - for recursion stack.
    """
    if not input_lists: return 

    n = len(input_lists)
    return merge(input_lists, 0, n-1)


def merge_k_sorted_lists_heapq(input_lists: list) -> ListNode:
    """ Solution - Min Heap
    We first insert the first element (also smallest as the lists are sorted) of each 
    linked list in a min heap. After this, we can take out the smallest element from 
    the heap and add it to the merged list. After removing the smallest element from the 
    heap, we can insert the next element of the same list into the heap. Repeat previous
    steps to populate the merged list in sorted order.

    Time Complexity - O(kn*logk) - the number of elements in the priority queue will be 
    less than k, so the time complexity for insertion and deletion will be O(logk), there 
    are at most k*n elements (every node is inserted and deleted once), so the total time 
    complexity will be O(kn*logk)
    Space Complexity - O(k) - for the priority queue (min-heap).
    """
    dummy = ListNode(-1)
    current = dummy
    min_heap = []

    # Put the root of each list in the min heap
    for root in input_lists:
        if root:
            heapq.heappush(min_heap, root)

    # Pop the smallest element from the min heap and add it to the result sorted list.
    while min_heap:
        node = heapq.heappop(min_heap)
        current.next = node
        current = current.next

        # If the element poped still have next node, then add it into the heap.
        if node.next:
            heapq.heappush(min_heap, node.next)

    return dummy.next


if __name__ == "__main__":
    l1 = create_linked_list([2,6,8])
    l2 = create_linked_list([3,6,7])
    l3 = create_linked_list([1,3,4])
    new_list = merge_k_lists_divide_and_conquer([l1, l2, l3])
    print(traverse(new_list))

    l1 = create_linked_list([1,4,5])
    l2 = create_linked_list([1,3,4])
    l3 = create_linked_list([2,6])
    result = merge_k_sorted_lists_heapq([l1, l2, l3])
    print(traverse(result))

