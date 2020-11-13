""" 实现一个支持动态扩容的数组

https://blog.csdn.net/weixin_43633501/article/details/90108817

Properties：
    capacity - capacity of the array
    size - actual length of the array
Functions:
    add() - add element to the array
    remove() - remove element in the array
"""


class DynamicArray:
    def __init__(self, capacity=10):
        self._capacity = capacity
        self._size = 0
        self._data = [None] * self._capacity

    def add(self, index, element):
        if index < 0 or index > self._capacity:
            raise Exception("Index out of scope!")

        if index == self._capacity:
            self._resize()

        # TODO: What if there is already an element at this index?
        self._data[index] = element
        self._size += 1

    def delete(self, index):
        if index < 0 or index >= self._capacity:
            raise Exception("Index out of scope!")

        self._data[index] = None

    def _resize(self):
        new_data = [None] * (self._capacity * 2)
        for i in range(self._capacity):
            new_data[i] = self._data[i]
        self._data = new_data
        self._capacity *= 2

    def __repr__(self):
        temp = [f"{data}" for data in self._data]
        return " ".join(temp)


if __name__ == "__main__":
    my_array = DynamicArray(capacity=5)
    my_array.add(0, 0)
    my_array.add(3, 30)
    my_array.add(5, 50)
    print(my_array)

    my_array.delete(5)
    print(my_array)