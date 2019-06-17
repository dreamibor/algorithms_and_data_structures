def partition(arr, l, r):
    pass

def quick_sort_partition(arr, l, r):
    if l >= r: return None
    q = partition(arr, l, r)
    quick_sort_partition(arr, l, q)
    quick_sort_partition(arr, q+1, r)
6
def quick_sort(arr):
    """ Quick sort.
    Recursive Formula: quick_sort(p...r) = quick_sort(p...q-1) + quick_sort(q+1...r)
    Termination Condition: l >= r
    Time Complexity: average: O(N*logN) worst:O(N)
    Space Complexity: O(1)
    """
    if len(arr) <= 1:
        return arr
    quick_sort_partition(arr, 0, len(arr) - 1)


if __name__ == "__main__":
    example = [6,5,4,3,1,2]
    print("Original Array:     {}".format(example))
    quick_sort(example)
    print("Quick Sorted Array: {}".format(example))