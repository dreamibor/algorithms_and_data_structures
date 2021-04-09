# Binary Search
Binary Search could be used in a sorted list.

Template for Binary Search:
1. Initialization - `start = 0, end = len(array) - 1`.
2. Loop termination condition - `start + 1 < end`.
3. Compare the middle point with the target, such as `array[mid] ==, < or > target`.
4. Compare the last two elements left (`array[start]` and `array[end]`) with target.

The time complexity for binary search is O(logN).
