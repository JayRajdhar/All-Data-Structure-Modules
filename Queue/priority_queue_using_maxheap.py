from Heap import maxheap_using_list


p_queue = maxheap_using_list.MaxHeap(10)

p_queue.insert(10)
p_queue.insert(4)
p_queue.insert(6)
p_queue.get_max()
p_queue.insert(1)
print(p_queue.heap)