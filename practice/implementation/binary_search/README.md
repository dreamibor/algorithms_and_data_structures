# Binary Search
Binary search could be used in a **sorted** list to look for a specific number.

The time complexity for binary search is O(logN).

There are some conditions for using binary search:
1. The array shall be **sorted** (decreasing or increasing).
2. The array shall be **bounded** (there are up and down bounds).
3. The array shall be **accessible by index**.

Template for binary search:
1. Initialization - `start = 0, end = len(array) - 1`.
2. Loop termination condition - `start + 1 < end`.
3. Compare the middle point with the target, such as `array[mid] ==, < or > target`.
4. Compare the last two elements left (`array[start]` and `array[end]`) with target.

Source code:
``` Python
def binary_search(array):
    left, right = 0, len(array) - 1

    while left <= right:
        mid = (left + right) / 2

        if array[mid] == target:
            # Found the target
            break # or return result
        elif array[mid] < target:
            left = mid + 1
        else:
            right = mid - 1
```

