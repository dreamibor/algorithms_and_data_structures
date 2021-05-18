"""
Heap - Kth Largest Element in an Array (medium)

Given an integer array nums and an integer k, return the kth largest element 
in the array.

Note that it is the kth largest element in the sorted order, not the kth 
distinct element.

Example:
Input: nums = [3,2,1,5,6,4], k = 2
Output: 5

LeetCode: https://leetcode-cn.com/problems/kth-largest-element-in-an-array/
"""
import heapq


def kth_largest_heap(nums: list, k: int) -> int:
    """ Heap

    We can have a heap of size k whose heap top will be the kth largest (or 
    the minimum in the heap), after iterating through the array, we can just 
    return the heap top as the result.

    Time Complexity - O(NlogK) - N for iterating through the array, logk for 
    readjusting the heap sorted.
    Space Complexity - O(K) - For the heap.
    """
    heap = []

    for num in nums:
        # Push the new element into the heap.
        heapq.heappush(heap, num)

        # Pop the heap top if there are more than K elements.
        if len(heap) > k:
            heapq.heappop(heap)

    return heap[0]

    


if __name__ == "__main__":
    nums, k = [3,2,1,5,6,4], 2
    print(kth_largest_heap(nums, k))