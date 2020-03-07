class Node(object):
    def __init__(self, data, next = None):
        self.next = None
        self.data = data
    def get_next(self):
        return self.next
    def set_next(self, new_next):
        self.next = new_next
    def get_data(self):
        return self.data

class Queue(object):
    def __init__(self, head = None, tail = None):
        self.head = head
        self.tail = tail
    def enqueue(self, data):
        new_node = Node(data=data)
        if self.head is None and self.tail is None:
            self.head = new_node
            self.tail = new_node
        else:
            self.tail.set_next(new_node)
            self.tail = new_node

    def dequeue(self):
        if self.head is None and self.tail is None:
            return 'Empty queue'
        else:
            temp = self.head
            self.head = temp.get_next()
            temp.set_next(None)

    def queue_size(self):
        count = 0
        if self.head is not None:
            temp = self.head
            while temp is not None:
                count = count + 1
                temp = temp.get_next()
            return count
        else:
            return 'Empty Queue'
    def print_queue(self):
        if self.head is not None:
            temp = self.head
            while temp is not None:
                print(temp.get_data())
                temp = temp.get_next()
        else:
            print('Empty queue')

def callQueue():
    q1 = Queue()
    ip = int(input('1. Enqueue \n2. Dequeue\n3.Size \n4.Print \n5. Exit'))
    while ip != 5:
        if ip == 1:
            data = int(input('Enter value: '))
            q1.enqueue(data=data)
        if ip == 2:
            q1.dequeue()
        if ip == 3:
            print(q1.queue_size())
        if ip == 4:
            q1.print_queue()
        ip = int(input('1. Enqueue \t2. Dequeue\t3.Size \t4.Print \t5. Exit'))

callQueue()