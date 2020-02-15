class Node(object):
    def __init__(self, next=None, data=None):
        self.next = next
        self.data = data
    def get_data(self):
        return self.data
    def get_next(self):
        return self.next
    def set_next(self,new_next):
        self.next = new_next

class LinkedList(object):
    def __init__(self, head=None):
        self.head = head

    def insert_begin(self,data):
        new_node = Node(data=data)
        new_node.set_next(self.head)
        self.head = new_node

    def insert_end(self, data):
        new_node = Node(data=data)
        new_node.set_next(None)
        if self.head is None:
            self.head = new_node
        else:
            temp_node = self.head
            while temp_node.get_next() is not None:
                temp_node = temp_node.get_next()
            temp_node.set_next(new_node)

    def insert_after(self, data, after_data):
        if self.head is not None:
            new_node = Node(data=data)
            temp_node = self.head
            while temp_node.get_next() is not None:
                if int(temp_node.get_data()) == after_data:
                    new_node.set_next(temp_node.get_next())
                    temp_node.set_next(new_node)
                    break
                temp_node = temp_node.get_next()
            if temp_node.get_next() is None:
                print('No such node exists')
        else:
            print('Linked List is empty')

    def ll_size(self):
        tmp_node = self.head
        count = 0
        while tmp_node is not None:
            count = count + 1
            tmp_node = tmp_node.get_next()
        return count

    def print_ll(self):
        tmp_node = self.head
        while tmp_node is not None:
            print('Data : ', tmp_node.get_data(), ' -> ', end=' ')
            tmp_node = tmp_node.get_next()
        print('\n')
def create_LinkedList():
    ll = LinkedList()
    ip = int(input('Options : \n 1. Add Node Begin \n 2. Add Node End \n 3. Add after data: \n 4. Size \n 5. Print \n 6. Exit \n'))
    while ip != 6:
        if ip == 1:
            node_data = input('Enter data: ')
            ll.insert_begin(node_data)
        elif ip == 2:
            node_data = input('Enter data: ')
            ll.insert_end(node_data)
        elif ip == 3:
            node_data = int(input('Enter data: '))
            after_data = int(input('Enter after: '))
            ll.insert_after(node_data,after_data)
        elif ip == 4:
            print(ll.ll_size())
        elif ip == 5:
            ll.print_ll()
        ip = int(input('Options : \n 1. Add Node Begin \n 2. Add Node End \n 3. Add after data: \n 4. Size \n 5. Print \n 6. Exit \n'))

create_LinkedList()


