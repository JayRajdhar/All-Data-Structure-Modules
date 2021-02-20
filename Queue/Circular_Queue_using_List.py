from typing import List


class CirQueue:

    def __init__(self, size):
        self.capacity = size
        self.queue = [None]*size
        self.FRONT = -1
        self.REAR = -1

    def deco(func):
        def inner(self, *args):
            func(self, *args)
            self.show()
            return func
        return inner

    def is_full(self):
        return True if self.REAR == self.FRONT - 1 or (self.FRONT == 0 and self.REAR == self.capacity - 1) else False

    def is_empty(self):
        return True if self.REAR == -1 and self.FRONT == -1 else False

    @deco
    def enqueue(self, value):
        if self.is_full():
            return print('Sorry Queue Full')
        else:
            if self.FRONT == -1:  #imp point
                self.FRONT = 0
            self.REAR = (self.REAR + 1) % self.capacity
            self.queue[self.REAR] = value
            print(value, ' Queued at ', self.REAR)

    @deco
    def dequeue(self):
        if self.is_empty():
            return print('Sorry Queue Empty')
        elif self.FRONT == self.REAR:
            dq = self.queue[self.FRONT]
            self.queue[self.FRONT] = None
            self.REAR = -1
            self.FRONT = -1
            return print(dq, ' Item DQ')
        else:
            dq = self.queue[self.FRONT]
            self.queue[self.FRONT] = None
            self.FRONT = (self.FRONT + 1) % self.capacity
            return print(dq, ' Item DQ')

    def show(self):
        print(self.queue, 'Front:', self.FRONT, ' REAR:', self.REAR)


q = CirQueue(5)

# print(q.is_full())
q.dequeue()
q.enqueue(1)
q.enqueue(2)
q.dequeue()
q.dequeue()
q.dequeue()
q.enqueue(3)
q.enqueue(4)
q.enqueue(5)
q.enqueue(6)
q.enqueue(7)
q.enqueue(9)
q.dequeue()
q.enqueue(9)
q.enqueue(0)
