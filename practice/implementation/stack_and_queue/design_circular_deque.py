"""
Queue - Design Circular Deque (medium)

Description:
Design your implementation of the circular double-ended queue (deque).

Your implementation should support following operations:
- MyCircularDeque(k): Constructor, set the size of the deque to be k.
- insertFront(): Adds an item at the front of Deque. Return true if the operation is successful.
- insertLast(): Adds an item at the rear of Deque. Return true if the operation is successful.
- deleteFront(): Deletes an item from the front of Deque. Return true if the operation is successful.
- deleteLast(): Deletes an item from the rear of Deque. Return true if the operation is successful.
- getFront(): Gets the front item from the Deque. If the deque is empty, return -1.
- getRear(): Gets the last item from Deque. If the deque is empty, return -1.
- isEmpty(): Checks whether Deque is empty or not. 
- isFull(): Checks whether Deque is full or not.

Example:
MyCircularDeque circularDeque = new MycircularDeque(3); // set the size to be 3
circularDeque.insertLast(1);			// return true
circularDeque.insertLast(2);			// return true
circularDeque.insertFront(3);			// return true
circularDeque.insertFront(4);			// return false, the queue is full
circularDeque.getRear();  			// return 2
circularDeque.isFull();				// return true
circularDeque.deleteLast();			// return true
circularDeque.insertFront(4);			// return true
circularDeque.getFront();			// return 4

Leetcode Link: https://leetcode-cn.com/problems/design-circular-deque/
"""


class MyCircularDeque:
    def __init__(self, k: int):
        """ Initialize your data structure here. Set the size of the deque to be k. """
        self.max_len = k
        self.queue = []
        
    def insertFront(self, value: int) -> bool:
        """ Adds an item at the front of Deque. Return true if the operation is successful. """
        if len(self.queue) < self.max_len:
            self.queue.insert(0, value)
            return True
        return False

    def insertLast(self, value: int) -> bool:
        """ Adds an item at the rear of Deque. Return true if the operation is successful. """
        if len(self.queue) < self.max_len:
            self.queue.append(value)
            return True
        else:
            return False

    def deleteFront(self) -> bool:
        """ Deletes an item from the front of Deque. Return true if the operation is successful. """
        if len(self.queue):
            del self.queue[0]
            return True
        return False

    def deleteLast(self) -> bool:
        """ Deletes an item from the rear of Deque. Return true if the operation is successful. """
        if len(self.queue):
            del self.queue[-1]
            return True
        return False 

    def getFront(self) -> int:
        """ Get the front item from the deque. """
        if len(self.queue):
            return self.queue[0]
        return -1

    def getRear(self) -> int:
        """ Get the last item from the deque. """
        if len(self.queue):
            return self.queue[-1]
        return -1

    def isEmpty(self) -> bool:
        """ Checks whether the circular deque is empty or not. """
        return not self.queue 

    def isFull(self) -> bool:
        """ Checks whether the circular deque is full or not. """
        return len(self.queue) == self.max_len
    
    def __repr__(self) -> str:
        """ Display the deque in string. """
        result = []
        for element in self.queue:
            result.append(f"{element}")
        
        return ", ".join(result)


if __name__ == "__main__":
    circularDeque = MyCircularDeque(3);     # set the size to be 3
    circularDeque.insertLast(1);			# return true
    circularDeque.insertLast(2);			# return true
    circularDeque.insertFront(3);			# return true
    print(circularDeque)
    status = circularDeque.insertFront(4);	# return false, the queue is full
    print(status)
    rear = circularDeque.getRear();  	    # return 2
    print(rear)
    full = circularDeque.isFull();		    # return true
    print(full)
    circularDeque.deleteLast();			    # return true
    print(circularDeque)
    circularDeque.insertFront(4);			# return true
    print(circularDeque)
    front = circularDeque.getFront();		# return 4
    print(front)