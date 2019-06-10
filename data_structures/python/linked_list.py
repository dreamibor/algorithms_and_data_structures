class Node():
    """docstring for Node"""
    def __init__(self, cargo, next=None):
        self.cargo = cargo
        self.next = next

    def __str__(self):
        return str(self.cargo)

class LinkedList():
    def __init__(self, head=None):
        self.head = None

    def is_empty(self):
        return self.head == None

    def insert(self, data):
        temp = Node(data)
        temp.next = self.head
        self.head = temp

    def delete(self, data):
        prev = None
        curr = self.head
        while curr != None:
            if curr.cargo == data:
                if prev == None:
                    curr == curr.next
                    break
                else:
                    prev.next = curr.next
                    break
            else:
                prev = curr
                curr = curr.next
        else:
            raise ValueError("Value Not Found")

    def __str__(self):
        curr = self.head
        out = "[ "
        while curr != None:
            out += "{} ".format(curr.cargo)
            curr = curr.next
        out += "]"
        return out


my_list = LinkedList()
my_list.insert(5)
my_list.insert(6)
my_list.insert(7)
print(my_list)
my_list.delete(6)
print(my_list)

