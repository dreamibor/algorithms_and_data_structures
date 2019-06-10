def quick_sort(alist):
    quick_sort_helper(alist, 0, len(alist) - 1)

def quick_sort_helper(alist, first, last):
    if first < last:
        splitpoint = partition(alist, first, last)
        quick_sort_helper(alist, first, splitpoint - 1)
        quick_sort_helper(alist, splitpoint + 1, last)

def partition(alist, first, last):
    pivot = alist[first]
    left_mark = first + 1
    right_mark = last

    done = False
    while not done:
        while left_mark <= right_mark and alist[left_mark] <= pivot:
            left_mark += 1
        while alist[right_mark] >= pivot and right_mark >= left_mark:
            right_mark -= 1
        if left_mark > right_mark:
            done = True
        else:
            alist[left_mark], alist[right_mark] = alist[right_mark], alist[left_mark]

    alist[first], alist[right_mark] = alist[right_mark], alist[first]
    return right_mark

alist = [54,26,93,17,77,31,44,55,20]
quick_sort(alist)
print(alist)
