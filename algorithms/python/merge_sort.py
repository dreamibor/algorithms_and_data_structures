def merge(arr, l, mid, r):
    """ Merge function to merge left and right array into one sorted array.
    """
    # Initialise start postions for while loop
    i = l; j = mid + 1
    temp = []

    # Compare the elements in two arrays and merge the smallest into sorted array
    while i <= mid and j <= r:
        if arr[i] < arr[j]:
            temp.append(arr[i])
            i += 1
        else:
            temp.append(arr[j])
            j += 1
    
    # Merge the remaining array
    while i <= mid:
        temp.append(arr[i])
        i += 1
    
    while j <= r:
        temp.append(arr[j])
        j += 1
    
    # Copy the sorted array into the original array
    for i in range(len(temp)):
        arr[i+l] = temp[i]

def merge_sort_partition(arr, l, r):
    """ Recusion code to merge left and right part.
    """
    if l >= r:
        return None

    mid = (l + r) // 2
    merge_sort_partition(arr, l, mid)
    merge_sort_partition(arr, mid+1, r)
    merge(arr, l, mid, r)

def merge_sort(arr):
    """ Wrap recusion code
    """
    if len(arr) <= 1:
        return arr
    
    merge_sort_partition(arr, 0, len(arr) - 1)


if __name__ == "__main__":
    example = [4,5,6,1,3,2,7,32,7,213,434,55,677,334,23,50,20]
    print("Original Array:     {}".format(example))
    merge_sort(example)
    print("Merge Sorted Array: {}".format(example))