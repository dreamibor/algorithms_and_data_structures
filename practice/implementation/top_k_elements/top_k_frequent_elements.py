"""
Heap - Top K Frequent Elements (medium)

Given an integer array nums and an integer k, return the k most frequent 
elements. You may return the answer in any order.

Example:

Input: nums = [1,1,1,2,2,3], k = 2
Output: [1,2]

Follow up: Your algorithm's time complexity must be better than O(n log n), 
where n is the array's size.

LeetCode: https://leetcode-cn.com/problems/top-k-frequent-elements/
"""
import heapq
from collections import defaultdict


def top_k_frequent(nums: list, k: int) -> list:
    """


    """
    heap = []
    frequency_map = defaultdict(int)
    
    for num in nums:
        frequency_map[num] += 1
    
    for num, frequency in frequency_map.items():
        heapq.heappush(heap, (frequency, num))

        if len(heap) > k:
            heapq.heappop(heap)
    
    res = []
    while heap:
        res.append(heapq.heappop(heap)[1])

    return res

if __name__ == "__main__":
    nums, k = [1,1,1,2,2,3], 2
    print(top_k_frequent(nums, k))

    nums, k = [1, 3, 5, 12, 11, 12, 11], 2
    print(top_k_frequent(nums, k))