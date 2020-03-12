#This program accepts a list as an input and converts it to Min Heap and Max Heap


class Heap(object):
    def __init__(self, list1):
        self.heap_list = list1
        self.heap_size = len(list1) - 1

    def get_size(self):
        return self.heap_size

    def set_size(self, size):
        self.heap_size = size

    def convert_to_max_heap(self, index):
        largest_index = index
        left_child = 2*largest_index
        right_child = 2*largest_index + 1
        if left_child < self.heap_size and self.heap_list[left_child]  > self.heap_list[largest_index]:
            largest_index = left_child
        if right_child <= self.heap_size and self.heap_list[right_child] > self.heap_list[largest_index]:
            largest_index = right_child
        if largest_index != index:
            self.heap_list[largest_index], self.heap_list[index] = self.heap_list[index], self.heap_list[largest_index]
            self.convert_to_max_heap(largest_index)

    def print_heap(self):
        return self.heap_list

    def buildHeap_max(self):
        startIdx = self.heap_size // 2
        for i in range(startIdx, 0, -1):
            self.convert_to_max_heap(i)

    def buildHeap_min(self):
        startIdx = self.heap_size // 2
        for i in range(startIdx, 0, -1):
            self.convert_to_min_heap(i)


    def convert_to_min_heap(self, index):
        smallest_index = index
        left_child = 2*smallest_index
        right_child = 2*smallest_index + 1
        if left_child < self.heap_size and self.heap_list[left_child] < self.heap_list[smallest_index]:
            smallest_index = left_child
        if right_child <= self.heap_size and self.heap_list[right_child] < self.heap_list[smallest_index]:
            smallest_index = right_child
        if smallest_index != index:
            self.heap_list[smallest_index], self.heap_list[index] = self.heap_list[index], self.heap_list[smallest_index]
            self.convert_to_min_heap(smallest_index)
def call_max_heap():
    list1 = [0,1,4,6,2,78]
    h1 = Heap(list1)
    print('Size:', h1.get_size())
    print('Original Heap: ', h1.print_heap())
    print(h1.buildHeap_max())
    print('Final Heap: ', h1.print_heap())

def call_min_heap():
    list2 = [0,1,4,6,2,78,198,42,-9,98]
    h2 = Heap(list2)
    print('Size:', h2.get_size())
    print('Original Heap: ', h2.print_heap())
    print(h2.buildHeap_min())
    print('Final Heap: ', h2.print_heap())

call_max_heap()
call_min_heap()