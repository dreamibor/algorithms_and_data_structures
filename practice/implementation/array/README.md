# Array

Array is a type of **continuous** linear data structures.

Properties:
1. Access - O(1) - with known index.
2. Insertion - O(N) 
    - worst case O(N) insert at the beginning;
    - best case O(1) insert at the end;
    - in average O(N/2) -> O(N).
3. Deletion - O(N) - similar to insertion.

# How are lists implemented in CPython?
CPython’s lists are really **variable-length arrays**, not Lisp-style linked lists. The implementation uses a **contiguous array of references to other objects**, and keeps a pointer to this array and the array’s length in a list head structure.

This makes indexing a list a[i] an operation whose cost is independent of the size of the list or the value of the index.

When items are appended or inserted, the array of references is resized. Some cleverness is applied to improve the performance of appending items repeatedly; when the array must be grown, some extra space is allocated so the next few times don’t require an actual resize.

Problem List:
1. [x] Implement a Dynamic Expansion Array
3. [x] [Merge Sorted Array](https://leetcode-cn.com/problems/merge-sorted-array/)
4. [x] [Three Sum](https://leetcode.com/problems/3sum/)
5. [x] [Majority Element](https://leetcode.com/problems/majority-element/)
6. [x] [Missing Positive](https://leetcode.com/problems/first-missing-positive/)