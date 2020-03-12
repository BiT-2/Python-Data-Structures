#This program accepts input as individual integer elements and creates a min heap.
# It also rearranges elements to retain min heap property and we can perform pop operation too!
# Max Heap for individual elements can be done by inverting the signs in this code

class BinaryHeap(object):
    def __init__(self):
        self.heap_list = [0]
        self.current_heap_size = len(self.heap_list) - 1

    def current_size(self):
        return self.current_heap_size

    def set_heap_size(self, size):
        self.current_heap_size = size

    def insert_heap(self, data):
        self.heap_list.append(data)
        self.set_heap_size(len(self.heap_list) - 1)
        self.balance_up(len(self.heap_list) - 1)

    def balance_up(self, index):
        while index // 2 > 0:
            if self.heap_list[index // 2] > self.heap_list[index]:
                temp = self.heap_list[index//2]
                self.heap_list[index//2] = self.heap_list[index]
                self.heap_list[index] = temp
            index = index//2

    def minimum_child(self, index):
        if 2*index + 1 > self.current_heap_size:
            return 2*index
        else:
            if self.heap_list[2*index] < self.heap_list[2*index+1]:
                return 2*index
            else:
                return 2*index + 1

    def balance_down(self, index):
        while 2*index <= self.current_heap_size:
            min_child_index = self.minimum_child(index)
            if self.heap_list[index] > self.heap_list[min_child_index]:
                temp = self.heap_list[index]
                self.heap_list[index] = self.heap_list[min_child_index]
                self.heap_list[min_child_index] = temp
            index = min_child_index

    def return_min(self):
        return self.heap_list[1]

    def pop_heap(self):
        min_val = self.heap_list[1]
        self.heap_list[1] = self.heap_list[len(self.heap_list)- 1]
        self.set_heap_size(len(self.heap_list) - 2)
        self.heap_list.pop()
        self.balance_down(1)
        return min_val

    def construct_heap(self, list1):
        i = len(list1) // 2
        self.set_heap_size(len(list1))
        self.heap_list.append(list1)
        while i > 0:
            self.balance_down(i)
            i = i - 1
    def print_heap(self):
        return self.heap_list[1:]
heap1 = BinaryHeap()
heap1.insert_heap(78)
heap1.insert_heap(6)
heap1.insert_heap(2)
heap1.insert_heap(4)
heap1.insert_heap(1)
print(heap1.print_heap())
#print(heap1.pop_heap())
#print(heap1.pop_heap())
#print(heap1.pop_heap())