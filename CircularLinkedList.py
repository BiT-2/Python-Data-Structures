class Node(object):
    def __init__(self,next=None,data=None):
        self.next = next
        self.data = data

    def get_next(self):
        return self.next

    def set_next(self, new_next):
        self.next = new_next

    def get_data(self):
        return self.data

class CircularLinkedList(object):
    def __init__(self, head=None):
        self.head = head

    def print_cll(self):
        if self.head is not None:
            temp_node =self.head
            while True:
                print('Data : ', temp_node.get_data(), ' - > ', end = ' ')
                temp_node = temp_node.get_next()
                if temp_node == self.head:
                    break
        else:
            print('List is empty')

    def insert_begin(self,data):
        new_node = Node(data=data)
        if self.head is None:
            self.head = new_node
            new_node.set_next(self.head)
        else:
            temp_node = self.head
            while temp_node.get_next() != self.head:
                temp_node = temp_node.get_next()
            temp_node.set_next(new_node)
            new_node.set_next(self.head)
            self.head = new_node

    def insert_end(self,data):
        new_node = Node(data=data)
        if self.head is not None:
            temp_node = self.head
            while temp_node.get_next() != self.head:
                temp_node = temp_node.get_next()
            new_node.set_next(self.head)
            temp_node.set_next(new_node)
        else:
            self.head = new_node
            new_node.set_next(self.head)

    def insert_after(self,after_data,data):
        if self.head is not None:
            temp_node =self.head
            while temp_node.get_next() != self.head:
                if temp_node.get_data() == after_data:
                    new_node = Node(data=data)
                    new_node.set_next(temp_node.get_next())
                    temp_node.set_next(new_node)
                temp_node = temp_node.get_next()
            if temp_node.get_next() == self.head:
                if temp_node.get_data() == after_data:
                    new_node = Node(data=data)
                    temp_node.set_next(new_node)
                    new_node.set_next(self.head)

def call_CLL():
    ip = int(input('Option : \n 1. Add beginning \n 2.Add end \n 3. Insert after \n 4. Print \n 5. Exit \n'))
    cll = CircularLinkedList()
    while ip != 5:
        if ip==1:
            data = int(input('Enter data : '))
            cll.insert_begin(data)
        if ip==2:
            data = int(input('Enter data : '))
            cll.insert_end(data)
        if ip==3:
            after_data = int(input('Enter after : '))
            data = int(input('Enter data : '))
            cll.insert_after(after_data,data)
        if ip == 4:
            cll.print_cll()
        ip = int(input('Option : \n 1. Add beginning \n 2.Add end \n 3. Insert after \n 4. Print \n 5. Exit \n'))


call_CLL()