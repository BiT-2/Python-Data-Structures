class Node(object):
    def __init__(self, left_child=None, right_child=None, data=None):
        self.left_child = left_child
        self.right_child = right_child
        self.data = data

    def get_left_child(self):
        return self.left_child

    def get_right_child(self):
        return self.right_child

    def set_left_child(self, new_left):
        self.left_child=new_left

    def set_right_child(self,new_right):
        self.right_child=new_right

    def get_data(self):
        return self.data


class BinarySearchTree(object):
    def __init__(self):
        self.root = None

    def insert(self,data):
        new_node = Node(data=data)
        if self.root is None:
            self.root = new_node
        else:
            self._insert(self.root,new_node)

    def _insert(self, cur_node, new_node):
        if int(new_node.get_data()) < int(cur_node.get_data()):
            if cur_node.get_left_child() is None:
                cur_node.set_left_child(new_node)
            else:
                self._insert(cur_node.get_left_child(), new_node)
        elif int(new_node.get_data()) > int(cur_node.get_data()):
            if cur_node.get_right_child() is None:
                cur_node.set_right_child(new_node)
            else:
                self._insert(cur_node.get_right_child(), new_node)
        else:
            print('Node already exists!')

    def print_BST(self):
        if self.root is None:
            print('Empty tree!')
        else:
            self._print_BST(self.root)

    def _print_BST(self, cur_node):
        if cur_node is None:
            return None
        else:
            self._print_BST(cur_node.get_left_child())

            self._print_BST(cur_node.get_right_child())
            print(cur_node.get_data())

    def height_BST(self):
        if self.root is None:
            print('0')
        else:
            cur_height = 1
            height = self._height_BST(self.root, cur_height)
        return height

    def _height_BST(self, cur_node, cur_height):
        if cur_node is None:
            return cur_height
        left_height = self._height_BST(cur_node.get_left_child(), cur_height + 1)
        right_height = self._height_BST(cur_node.get_right_child(), cur_height + 1)

        return max(left_height, right_height)


def function1():
    from random import randint
    BST = BinarySearchTree()
    for i in range(100):
        BST.insert(randint(0, 1000))
    BST.print_BST()
    print('Tree height is : ', BST.height_BST())

function1()
