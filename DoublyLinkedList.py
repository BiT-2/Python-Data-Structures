class Node(object):
    def __init__(self, next=None,prev=None,data=None):
        self.next = next
        self.prev = prev
        self.data = data
    def get_next(self):
        return self.next
    def get_prev(self):
        return self.prev
    def get_data(self):
        return self.data
    def set_data(self,data):
        self.data = data
    def set_next(self, new_next):
        self.next = new_next
    def set_prev(self,new_prev):
        self.prev = new_prev

class DoublyLinkedList(object):
    def __init__(self, head=None):
        self.head = None

    def dll_print(self):
        if self.head is not None:
            temp_node = self.head
            while temp_node is not None:
                print('Data : ', temp_node.get_data(), ' -> ', end=' ')
                temp_node = temp_node.get_next()
        else:
            print('Empty List')
    def dll_size(self):
        temp_node = self.head
        count = 0
        while temp_node is not None:
            count += 1
            temp_node = temp_node.get_next()
        return count

    def insert_begin(self, data):
        new_node = Node(data=data)
        new_node.set_next(self.head)
        new_node.set_prev(None)
        if self.head is not None:
            self.head.set_prev(new_node)
        self.head = new_node

    def insert_end(self, data):
        new_node = Node(data=data)
        if self.head is None:
            self.head = new_node
        else:
            temp_node = self.head
            while temp_node.get_next() is not None:
                temp_node = temp_node.get_next()
            new_node.set_prev(temp_node)
            new_node.set_next(None)
            temp_node.set_next(new_node)

    def insert_after(self,after_data,data):
        #new_node = Node(data=data)
        if self.head is None:
            print('List is empty')
        else:
            temp_node = self.head
            while temp_node is not None:
                if temp_node.get_data() == after_data:
                    new_node = Node(data=data)
                    if temp_node.get_next() is not None:
                        temp_node2 = temp_node.get_next()
                        new_node.set_prev(temp_node)
                        new_node.set_next(temp_node.get_next())
                        temp_node2.set_prev(new_node)
                        temp_node.set_next(new_node)
                    else:
                        temp_node.set_next(new_node)
                        new_node.set_prev(temp_node)
                        new_node.set_next(None)
                temp_node = temp_node.get_next()

def call_DLL():
    dll = DoublyLinkedList()
    ip = int(input('Options: \n 1. Add Begin \n 2. Add End \n 3. Insert after \n 4. Print 5. Size \n 6. Exit \n'))
    while ip!=6:
        if ip == 1:
            data = int(input('Enter data : '))
            dll.insert_begin(data)
        if ip ==2:
            data = int(input('Enter data : '))
            dll.insert_end(data)
        if ip==3:
            after_data = int(input('Insert after : '))
            data = int(input('Enter data : '))
            dll.insert_after(after_data,data)
        if ip == 4:
            dll.dll_print()
        if ip == 5:
            print(dll.dll_size())
        ip = int(input('Options: \n 1. Add Begin \n 2. Add End \n 3. Insert after \n 4. Print 5. Size \n 6 . Exit \n'))

call_DLL()