
class Stack:

    def __init__(self, size):
        self.capacity = size
        self.stack = [None]*size
        self.top = -1

    def is_empty(self):
        return True if self.top == -1 else False

    def is_full(self):
        return True if self.top == self.capacity-1 else False

    def push(self, value):
        if self.is_full():
            print('Sorry Stack Full', self.stack)
        else:
            self.top += 1
            self.stack[self.top] = value
            print(value, ' Pushed at:', self.top)
            print(self.stack)

    def pop(self):
        if self.is_empty():
            print('Sorry Stack Already Empty')
        else:
            pop = self.stack[self.top]
            self.stack[self.top] = None
            self.top -= 1
            print(pop, ' Popped')
            print(self.stack)

    def peek(self):
        return print(self.stack[self.top])

    def current_size(self):
        return print(self.top + 1)




s = Stack(5)
s.push(1)
s.push(2)
s.push(3)
s.current_size()
s.push(4)
s.pop()
s.push(5)
s.peek()
s.push(7)
s.is_empty()
s.current_size()
s.is_full()