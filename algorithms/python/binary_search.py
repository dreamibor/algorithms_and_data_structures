def simple_binary_search(arr, target):
    """
    """
    if len(arr) <= 1: return arr

    low = 0
    high = len(arr) - 1

    # Termination condition: low <= high
    while low <= high:
        mid = low + ((high - low) >> 1) # Replace (low + high) // 2 to avoid the overflow of integer.
        if arr[mid] == target:
            return mid
        elif arr[mid] < target:
            # Update low = mid + 1
            low = mid + 1
        else:
            # Update high = mid - 1
            high = mid - 1

    return -1

def recursive_binary_search_wrapper(arr, target):
    return recursive_binary_search(arr, 0, len(arr) - 1, target)

def recursive_binary_search(arr, low, high, target):
    """
    """
    if low > high: return -1

    mid = low + ((high - low) >> 1)
    if arr[mid] == target:
        return mid
    elif arr[mid] < target:
        return recursive_binary_search(arr, mid + 1, high, target)
    else:
        return recursive_binary_search(arr, low, mid - 1, target)


if __name__ == "__main__":
    arr = [1,2,3,4,5,6,7,8,9,10]
    print("Index of 6 In The Array: {}".format(simple_binary_search(arr, 4)))
    print("Index of 6 In The Array: {}".format(recursive_binary_search_wrapper(arr, 4)))