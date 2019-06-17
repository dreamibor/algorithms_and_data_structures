def bubble_sorting_forward(arr):
    """ Compare the two adjacent elements, if the left one is larger than the right, exchange them.
    For each bubble loop, there will be a number moved to the right postion. 
    We should reach all elements before the sorted element. 
    Run it for N loops to get a sorted array.
    Time  Complexity: O(N^2)
    Space Complexity: O(1), only the temp variable for exchanging elements.
    """
    for i in range(len(arr)):
        for j in range(len(arr) -i - 1):
            if arr[j] > arr[j+1]:
                arr[j], arr[j+1] = arr[j+1], arr[j]
    return arr

def bubble_sorting_forward_early_stop(arr):
    """ If the array is already sorted, then we can stop the following bubble loops. 
    """
    for i in range(len(arr)):
        exchanged = False
        for j in range(len(arr) - i - 1):
            if arr[j] > arr[j+1]:
                arr[j], arr[j+1] = arr[j+1], arr[j]
                exchanged = True
        if not exchanged:
            break
    return arr

def bubble_sorting_backward(array):
    """ The outside loop is to control the inner loop to run for N times, so we can also start from N to 0, decrease 1 each time.
    In this case, we can set the range for inner loop as the value of the current outside loop.
    """
    for i in range(len(array) - 1, 0, -1):
        for j in range(i):
            if array[j] > array[j+1]:
                array[j], array[j+1] = array[j+1], array[j]
    return array

if __name__ == "__main__":
    my_list = [3,5,4,1,2,6,1]
    # Sort from min to max
    print("Bubble Sort Forward:            {}".format(bubble_sorting_forward(my_list)))
    print("Bubble Sort Forward Early Stop: {}".format(bubble_sorting_forward_early_stop(my_list)))
    print("Bubble Sort Backward:           {}".format(bubble_sorting_backward(my_list)))