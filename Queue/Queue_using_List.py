
class Queue:

    def __init__(self, size):
        self.capacity = size
        self.queue = [None]*size
        self.REAR = self.FRONT = -1

    def is_empty(self):
        return True if (self.FRONT and self.REAR) == -1 else False

    def is_full(self):
        return True if (self.REAR == self.capacity-1) else False

    def enqueue(self, value):
        if self.is_full():
            print('Sorry Q full')
        else:
            if self.FRONT == -1:  #imp point
                self.FRONT = 0
            self.REAR += 1
            self.queue[self.REAR] = value
            print(value, 'queued at:', self.REAR)
            # print(self.queue)

    def dequeue(self):
        if self.is_empty():
            print('Sorry Q empty')
        else:
            pop = self.queue[self.FRONT]
            self.queue[self.FRONT] = None
            self.FRONT += 1
            if self.FRONT > (self.capacity-1):    # imp point
                self.REAR = self.FRONT = -1
            print(pop, 'is dequeued')
            # print(self.queue)

    def peek(self):
        if self.is_empty():
            print('Sorry Q empty')
        else:
            print(self.queue[self.FRONT])


q = Queue(5)
print(q.is_empty())
print(q.is_full())

q.enqueue(1)
q.enqueue(2)
q.enqueue(3)
q.dequeue()
q.enqueue(4)
q.peek()
q.enqueue(5)
print('full:', q.is_full())
q.dequeue()
q.dequeue()
q.dequeue()
print('empty:', q.is_empty())
q.dequeue()
print('empty:', q.is_empty())
q.enqueue(1)


x = '20'
y ='30'

print("30">'29')