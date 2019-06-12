# -*- coding: utf-8 -*-
def insertion_sort(arr):
    """ Divide the array into two parts, sorted and unsorted.
    For each element in unsorted area, compare it with the elements in sorted area and find the right position to insert it.
    Time  Complexity: O(N^2)
    Space Complexity: O(1)
    """
    if len(arr) <= 1:
        return arr

    sorted_index = 0
    for i in range(1, len(arr)):
        for j in range(sorted_index):
            if arr[i] < arr[j]:
                tmp = arr[i]
                for index in range(i,j,-1):
                    arr[index] = arr[index-1]
                arr[j] = tmp
                break
        sorted_index += 1
    return arr

def insertion_sort_backward(arr):
    """
    Time  Complexity: O(N^2)
    Space Complexity: O(1)
    """
    if len(arr) <= 1:
        return arr

    for i in range(1, len(arr)):
        tmp = arr[i]
        curr = 0
        found = False
         # Iterate the sorted aread from right to left.
        for j in range(i-1, -1, -1):
            curr = j
            if arr[j] > tmp:
                arr[j+1] = arr[j]
            else:
                found = True
                break
        # 如果下标为0，有两种可能，一种是遍历完之后没有发现比当前数值大的，一种是arr[1]>tmp, 但是arr[0] < tmp。
        if not found:
            arr[0] = tmp
        else:
            arr[curr+1] = tmp
    return arr

def insertion_sort_backward_while_loop(arr):
    """
    Time  Complexity: O(N^2)
    Space Complexity: O(1)
    """
    if len(arr) <= 1:
        return arr
    
    for i in range(1, len(arr)):
        value = arr[i]
        position = i
        # Since position is decremented 1 every time, so we don't have to worry about the case arr[1] > value and arr[0] < value.
        while position > 0 and arr[position-1] > value:
            arr[position] = arr[position-1]
            position -= 1
        arr[position] = value
    
    return arr 


if __name__ == "__main__":
    example = [4,5,6,1,3,2]
    print("Original Array:         {}".format(example))
    print("Insertion Sorted Array: {}".format(insertion_sort_backward_while_loop(example)))