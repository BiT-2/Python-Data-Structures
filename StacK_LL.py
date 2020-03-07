class Node(object):
    def __init__(self, next=None, data=None):
        self.next = next
        self.data = data
    def get_next(self):
        return self.next
    def set_next(self, new_next):
        self.next = new_next
    def get_data(self):
        return self.data

class Stack(object):
    def __init__(self, top = None):
        self.top = top
    def push_element(self, data):
        new_node = Node(data=data)
        if self.top is None:
            self.top = new_node
            new_node.set_next(None)
        else:
            new_node.set_next(self.top)
            self.top = new_node
    def peek_element(self):
        if self.top is not None:
            return self.top.get_data()
        else:
            return 'Empty Stack'
    def pop_element(self):
        if self.top is None:
            print('Empty stack')
        else:
            temp = self.top
            self.top = temp.get_next()
            temp.set_next(None)
    def stack_size(self):
        count = 0
        if self.top is None:
            return 0
        else:
            temp = self.top
            while temp is not None:
                count = count + 1
                temp = temp.get_next()
        return count
    def print_stack(self):
        if self.top is not None:
            temp = self.top
            while temp is not None:
                print(temp.get_data())
                temp = temp.get_next()
        else:
            print('Empty stack')

def callStack():
    s1 = Stack()
    ip = int(input('1. Push \n2. Peek\n3.Pop \n4. Size \n5.Print\n6.Exit'))
    while ip != 6:
        if ip == 1:
            data = int(input('Enter value: '))
            s1.push_element(data=data)
        if ip == 2:
            print(s1.peek_element())
        if ip == 3:
            s1.pop_element()
        if ip == 4:
            print(s1.stack_size())
        if ip == 5:
            s1.print_stack()
        ip = int(input('1. Push \n2. Peek\n3.Pop \n4. Size \n5.Print\n6.Exit'))

callStack()