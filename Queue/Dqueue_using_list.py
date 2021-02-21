
class Deque:

    def __init__(self):
        self.deque = []

    def is_empty(self):
        return self.deque == []

    def add_rear(self, value):
        self.deque.append(value)

    def add_front(self, value):
        self.deque.insert(0, value)

    def remove_rear(self):
        self.deque.pop()

    def remove_front(self):
        self.deque.pop(0)


if __name__ == '__main__':
    deque = Deque()

    deque.add_front(1)
    deque.add_front(2)
    deque.add_rear(5)
    print(deque.deque)
    deque.remove_front()
    deque.add_rear(7)
    deque.add_rear(8)
    deque.remove_rear()
    print(deque.deque)
