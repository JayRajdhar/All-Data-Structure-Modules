
class Node:

    def __init__(self, value1, value2):
        self.value1 = value1
        self.value2 = value2
        self.next = None


class LinkedList:

    def __init__(self):
        self.head = None

    def insert_at_start(self, *args):
        i_node = Node(*args)
        i_node.next = self.head
        self.head = i_node

    def insert_at_end(self, *args):
        i_node = Node(*args)

        if self.head is None:
            self.head = i_node

        temp = self.head
        while temp.next:
            temp = temp.next

        temp.next = i_node

    def insert_after(self, node, *args):
        i_node = Node(*args)
        temp = node.next
        i_node.next = temp
        node.next = i_node

    def del_node_index(self, index):
        if self.head is None:
            return
        temp = self.head
        if index == 0:
            self.head = self.head.next
            temp = None
            return

        for i in range(index-1):
            temp = temp.next
            if temp is None:
                break
        if temp is None:
            return
        if temp.next is None:
            return
        nex = temp.next.next
        temp.next = None
        temp.next = nex


    def print_list(self):
        temp = self.head
        while temp is not None:
            print(temp.value1, temp.value2, end="-->")
            temp = temp.next


if __name__ == '__main__':

    linked_list = LinkedList()
    node1 = Node(1, 'one')
    node2 = Node(2, 'two')
    node3 = Node(3, 'three')

    linked_list.head = node1
    linked_list.head.next = node2
    node2.next = node3
    linked_list.insert_at_start(0, 'zero')

    linked_list.insert_at_end(4, 'four')

    linked_list.insert_after(node2, 2.2, 'two.two')
    # linked_list.del_node_index(4)
    linked_list.print_list()


