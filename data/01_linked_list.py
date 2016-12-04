from __future__ import print_function

class Node:
    def __init__(self, data=None, next=None):
        self.data = data
        self.next = next

    def __str__(self):
        return str(self.data)


class LinkedList:
    def __init__(self):
        self.head = None
        self.length = 0

    def insert(self, data):
        new_node = Node(data, self.head)
        self.head = new_node
        self.length += 1

    def tail_insert(self, data):
        temp_node = Node(data=data)
        tail_node = self.head
        if self.head == None:
            self.head = temp_node
            self.length += 1
        else:
            while tail_node.next != None:
                tail_node = tail_node.next
            tail_node.next = temp_node
            self.length += 1

    def delete(self,data):
        del_node = self.head
        pre_node = None
        while del_node != None:
            if del_node.data == data:
                # If the node is the head
                if pre_node == None:
                    self.head = del_node.next
                    self.length -= 1
                    break
                # If the node is not the head
                else:
                    pre_node.next = del_node.next
                    self.length -= 1
                    break
            else:
                pre_node = del_node
                del_node = del_node.next
        else:
            raise ValueError("Value Not Found in This List!")

    def isEmpty(self):
        return self.head == None

    def __str__(self):
        if self.head != None:
            current = self.head
            out = '[\n' +str(current.data) +'\n'
            while current.next != None:
                current = current.next
                out += str(current.data) + '\n'
            return out + ']'
        return 'LinkedList []'


if __name__ == '__main__':
    test_linked_list = LinkedList()
    # head insert elements
    # test_linked_list.insert(6)
    # test_linked_list.insert(7)
    # test_linked_list.insert('@@')
    # test_linked_list.insert(True)

    # tail insert elements
    test_linked_list.tail_insert(6)
    test_linked_list.tail_insert(int(7))
    test_linked_list.tail_insert('@@')
    test_linked_list.tail_insert('hello')
    test_linked_list.tail_insert(True)
    test_linked_list.tail_insert(float(7.0))

    print("The Linked List: {}".format(str(test_linked_list)))
    print("Linked List Length: {}".format(test_linked_list.length))

    delete_data = input('Input the value to be deleted:\n')
    test_linked_list.delete(delete_data)

    print("The Linked List: {}".format(str(test_linked_list)))
    print("{}".format(test_linked_list.isEmpty()))
    print("Linked List Length: {}".format(test_linked_list.length))
