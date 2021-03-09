class MaxHeap:

    def __init__(self, maxsize):
        self.maxsize = maxsize
        self.curr_size = -1
        self.heap = [0] * maxsize

    def get_parent(self, pos):
        return (pos-1) // 2 if pos>0 else 0

    def get_left_child(self, pos):
        return (pos * 2) + 1

    def get_right_child(self, pos):
        return (pos * 2) + 2

    def is_leaf(self, pos):
        return True if pos >= self.curr_size // 2 and pos <= self.curr_size else False

    def swap(self, pos1, pos2):
        self.heap[pos1], self.heap[pos2] = self.heap[pos2], self.heap[pos1]

    def max_heapify(self, pos):
        if not self.is_leaf(pos):

            if (self.heap[pos] < self.heap[self.get_right_child(pos)] or
                    self.heap[pos] < self.heap[self.get_left_child(pos)]):

                if self.heap[self.get_left_child(pos)] > self.heap[self.get_right_child(pos)]:
                    self.swap(pos, self.get_left_child(pos))
                    self.max_heapify(self.get_left_child(pos))

                else:
                    self.swap(pos, self.get_right_child(pos))
                    self.max_heapify(self.get_right_child(pos))

    def insert(self, element):

        if self.curr_size == self.maxsize:
            return

        self.curr_size += 1
        self.heap[self.curr_size] = element

        current = self.curr_size
        while self.heap[current] > self.heap[self.get_parent(current)]:
            # print(self.heap)
            self.swap(current, self.get_parent(current))
            current = self.get_parent(current)

    def print(self):
        # print(self.heap)
        for i in range(0, (self.curr_size // 2)):
            print(" PARENT : " + str(self.heap[i]) +
                  " LEFT CHILD : " + str(self.heap[2*i + 1]) +
                  " RIGHT CHILD : " + str(self.heap[2*i + 2]))

    def get_max(self):
        self.swap(0, self.curr_size)
        popped = self.heap[self.curr_size]
        self.heap[self.curr_size] = 0
        self.curr_size -= 1
        self.max_heapify(0)
        return popped

    def remove(self, element):
        if self.heap[0] == element:
            self.get_max()
        else:
            for i in range(1, self.curr_size):
                if self.heap[i] == element:
                    self.swap(i, self.curr_size)
                    self.heap[self.curr_size] = 0
                    self.curr_size -= 1
                    self.max_heapify(i)


if __name__ == '__main__':
    import random

    heap = MaxHeap(7)

    a = [9, 3, 6, 5, 7, 2]  # random.randint(1, 10) for i in range(7)]
    print(a)
    [heap.insert(i) for i in a]
    heap.print()
    # print(heap.get_max())
    # heap.remove(7)
    # heap.print()