class Node(object):
    def __init__(self, left_child=None, right_child=None, data=None):
        self.left_child = left_child
        self.right_child = right_child
        self.data = int(data)

    def get_left_child(self):
        return self.left_child

    def get_right_child(self):
        return self.right_child

    def get_data(self):
        return self.data

    def set_left_child(self, new_left):
        self.left_child = new_left

    def set_right_child(self, new_right):
        self.right_child = new_right

class BST(object):
    def __init__(self, root = None):
        self.root = root

    def insert(self, data):
        new_node = Node(data=data)
        if self.root is None:
            self.root = new_node
        else:
            self._insert(self.root, new_node)

    def _insert(self, cur_node, new_node_add):
        if new_node_add.get_data() < cur_node.get_data():
            if cur_node.get_left_child() is None:
                cur_node.set_left_child(new_node_add)
            else:
                self._insert(cur_node.get_left_child(), new_node_add)
        elif new_node_add.get_data() > cur_node.get_data():
            if cur_node.get_right_child() is None:
                cur_node.set_right_child(new_node_add)
            else:
                self._insert(cur_node.get_right_child(), new_node_add)
        elif cur_node.get_data() == new_node_add.get_data():
            print('Node already exists')


    def print_BST(self):
        if self.root is None:
            print('Tree is empty')
        else:
            print('Inorder: ')
            self._print_BST_inorder(self.root)
            print('Preorder: ')
            self._print_BST_preorder(self.root)
            print('Postorder: ')
            self._print_BST_postorder(self.root)
            print('BFS')
            self.print_BFS()

    def _print_BST_inorder(self, cur_node):
        if cur_node is None:
            return None
        else:
            self._print_BST_inorder(cur_node.get_left_child())
            print(cur_node.get_data())
            self._print_BST_inorder(cur_node.get_right_child())

    def _print_BST_preorder(self, cur_node):
        if cur_node is None:
            return None
        else:
            print(cur_node.get_data())
            self._print_BST_preorder(cur_node.get_left_child())
            self._print_BST_preorder(cur_node.get_right_child())

    def _print_BST_postorder(self, cur_node):
        if cur_node is None:
            return None
        else:
            self._print_BST_postorder(cur_node.get_left_child())
            self._print_BST_postorder(cur_node.get_right_child())
            print(cur_node.get_data())

    def height(self):
        if self.root is None:
            print('Tree is empty')
        else:
            height = 0
            return  self._height(self.root, height)

    def _height(self, cur_node, height):
        if cur_node is None:
            return height
        else:
            left_height = self._height(cur_node.get_left_child(), height + 1)
            right_height = self._height(cur_node.get_right_child(), height + 1)
            return max(left_height, right_height)

    def search(self, data):
        if self.root is None:
            print('Tree is empty!')
        else:
            return self._search(self.root, data)

    def _search(self, cur_node, data):
        if cur_node.get_data() == data:
            return True
        else:
            if (data < cur_node.get_data()) and (cur_node.get_left_child() != None):
                return self._search(cur_node.get_left_child(), data)
            elif (data > cur_node.get_data()) and (cur_node.get_right_child() != None):
                return self._search(cur_node.get_right_child(), data)
            else:
                return False

    def print_BFS(self):
        if self.root is None:
            print('Tree is empty')
        else:
            height = self.height()
            for h in range(1, height+1):
                self._print_BFS(self.root, h)

    def _print_BFS(self, cur_node, level):
        if cur_node is None:
            return
        elif level == 1:
            print(cur_node.get_data())
        else:
            self._print_BFS(cur_node.get_left_child(), level - 1)
            self._print_BFS(cur_node.get_right_child(), level - 1)


def call():
    from random import randint
    BST1 = BST()
    BST1.insert(5)
    BST1.insert(3)
    BST1.insert(6)
    BST1.insert(2)
    BST1.insert(4)
    BST1.insert(8)

    #for i in range(10):
     #   BST1.insert(randint(0,100))

    BST1.print_BST()
    print('Height: ',BST1.height())
    print('Data exists? ',BST1.search(109))


call()
