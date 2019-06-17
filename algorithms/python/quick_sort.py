def partition(arr, l, r):
    """
    我们通过游标 i 把 A[l…r-1] 分成两部分。
    A[l…i-1] 的元素都是小于 pivot，我们暂且叫它“已处理区间”，A[i…r-1] 是“未处理区间”。
    我们每次都从未处理的区间 A[i…r-1] 中取一个元素 A[j]，与 pivot 对比，
    如果小于 pivot ，则将其加入到已处理区间的尾部，也就是 A[i] 的位置。
    最后交换 pivot 与“未处理区间”开始的位置，也就是循环结束时i的位置。
    """
    pivot = arr[r]
    i = l
    for j in range(l, r):
        if arr[j] < pivot:
            arr[j], arr[i] = arr[i], arr[j]
            i += 1
    
    arr[r], arr[i] = arr[i], arr[r]
    return i

def quick_sort_partition(arr, l, r):
    """ Recursive function for quick sort.
    """
    if l >= r: return None
    q = partition(arr, l, r)
    # Left side of the pivot, left to q - 1.
    quick_sort_partition(arr, l, q-1)
    # Right side of the pivot, q + 1 to right. 
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
    example = [6,5,4,1,3,2,8,7,9]
    print("Original Array:     {}".format(example))
    quick_sort(example)
    print("Quick Sorted Array: {}".format(example))