

class CirQueue:

    def __init__(self, size):
        self.capacity = size
        self.queue = [None]*size
        self.FRONT = -1
        self.REAR = -1

    class Deco:

        @classmethod
        def decorator(cls, func):
            def inner(self, *args):
                func(self, *args)
                self.show()
                return func
            return inner

    # a = Deco()

    def is_full(self):
        return True if self.REAR == self.FRONT - 1 or (self.FRONT == 0 and self.REAR == self.capacity - 1) else False

    def is_empty(self):
        return True if self.REAR == -1 and self.FRONT == -1 else False

    # @a.decorator
    @Deco.decorator
    def enqueue(self, value):
        if self.is_full():
            return print('Sorry Queue Full')
        else:
            if self.FRONT == -1:  #imp point
                self.FRONT = 0
            self.REAR = (self.REAR + 1) % self.capacity
            self.queue[self.REAR] = value
            print(value, ' Queued at index', self.REAR)

    # @a.decorator
    @Deco.decorator
    def dequeue(self):
        if self.is_empty():
            return print('Sorry Queue Empty')
        elif self.FRONT == self.REAR:
            dq = self.queue[self.FRONT]
            self.queue[self.FRONT] = None
            self.REAR = -1
            self.FRONT = -1
            return print(dq, ' DQ')
        else:
            dq = self.queue[self.FRONT]
            self.queue[self.FRONT] = None
            self.FRONT = (self.FRONT + 1) % self.capacity
            return print(dq, ' DQ')

    def show(self):
        print('{:20}'.format(''), self.queue, 'Front:', self.FRONT, ' REAR:', self.REAR)


if __name__ == '__main__':
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
