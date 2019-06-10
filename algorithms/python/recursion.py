def fibonacci(n):
    if n < 2:
        return n
    else:
        return fibonacci(n-1) + fibonacci(n-2)

def fib(n):
    a, b = 0, 1
    for i in range(0, n):
        a, b = b, a + b
    return a

print(fibonacci(5))
print(fib(50))

def binary_search(array, value):
    left = 0
    right = len(array) - 1
    while left <= right:
        mid = (left + right) / 2
        if array[mid] == value:
            return True
        elif value < array[mid]:
            right = mid - 1
        else:
            left = mid + 1
    return False
print(binary_search([1,2,3,4,56,78], 5))

def bubble_sort(array):
    for passnum in range(len(array)-1, 0, -1):
        for i in range(passnum):
            if array[i] > array[i+1]:
                array[i], array[i+1] = array[i+1], array[i]

    return array

print(bubble_sort([5,4,2,1,3]))
