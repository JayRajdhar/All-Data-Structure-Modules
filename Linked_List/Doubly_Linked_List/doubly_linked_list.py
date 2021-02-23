class Node:

    def __init__(self, val):
        self.val = val
        self.next = None
        self.prev = None


class DLinkedList:

    def __init__(self):
        self.head = None

    def insert_at_start(self, val):
        new_node = Node(val)
        if self.head is None:
            self.head = new_node
            return
        temp = self.head
        self.head = new_node
        new_node.next = temp
        temp.prev = new_node

    def insert_at_end(self, val):
        new_node = Node(val)

        if self.head is None:
            self.head = new_node
            return

        temp = self.head
        while temp.next:
            temp = temp.next
        temp.next = new_node
        new_node.prev = temp

    def del_index(self, index):
        if self.head is None:
            return

        temp = self.head
        if index == 0:
            self.head = self.head.next
            self.head.prev = None
            temp = None
            return

        for i in range(index - 1):
            temp = temp.next
            if temp is None:
                break

        if temp is None or temp.next is None:
            return

        nex = temp.next.next
        nex.prev = temp
        temp.next = None
        temp.next = nex


if __name__ == '__main__':
    ll = DLinkedList()

    node1 = Node(1)
    node2 = Node(2)
    node3 = Node(3)

    ll.head = node1
    node1.prev = None
    node1.next = node2
    node2.next = node3
    node2.prev = node1
    node3.next = None
    node3.prev = node2

    ll.insert_at_end(4)
    ll.insert_at_start(0)
    ll.del_index(3)

    temp = ll.head

    while temp is not None:
        print(temp.val, end="-->")
        if temp.next is None:
            break
        temp = temp.next

    print('\n*********')

    while temp is not None:
        print(temp.val, end="<--")
        temp = temp.prev
