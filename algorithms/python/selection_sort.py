def selection_sort(arr):
    """ Divide the array into two parts, sorted and unsorted.
    Each time select the minimum (or maximum) value and exchange it with the first unsorted element.
    Time  Complexity: O(N^2)
    Space Complexity: O(1)
    """
    if len(arr) <= 1:
        return arr
    
    for i in range(0, len(arr)):
        # Default minimum value and it's index
        minimum = arr[i]
        min_index = i

        # Find minimum value and it's index
        for j in range(i, len(arr)):
            if arr[j] < minimum:
                minimum = arr[j]
                min_index = j
        
        # Exchange fisrt unsorted element with the minimum value
        arr[i], arr[min_index] = arr[min_index], arr[i]

    return arr


if __name__ == "__main__":
    example = [6,5,4,3,2,1]
    print("Original Array:         {}".format(example))
    print("Selection Sorted Array: {}".format(selection_sort(example)))