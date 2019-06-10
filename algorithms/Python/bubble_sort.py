def bubble_sorting(array):
    for i in range(len(array) - 1, 0, -1):
        for j in range(i):
            if array[j] > array[j+1]:
                array[j], array[j+1] = array[j+1], array[j]
    return array

my_list = [1,5,2,3,7,6,4,1]
a = bubble_sorting(my_list)
print(a)
