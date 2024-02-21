from node import Node


class BinaryTree:

    def __init__(self):
        self.root = None
        self.current = None

    def insert(self, node):

        if self.root is None:
            self.root = node
            self.current = self.root

        elif node.data < self.current.data:
            if self.current.left is None:
                self.current.left = node
                self.current = self.root
            else:
                self.current = self.current.left
                self.insert(node)

        elif node.data > self.current.data:
            if self.current.right is None:
                self.current.right = node
                self.current = self.root
            else:
                self.current = self.current.right
                self.insert(node)

        else:
            print("Node with this value already exists!")

    def inorder_print(self, node):
        if node is None:
            return
        self.inorder_print(node.left)
        print(node.data, end=" ")
        self.inorder_print(node.right)


binary_tree = BinaryTree()

root = Node("g")
node_c = Node("c")
node_b = Node("b")
node_a = Node("a")
node_e = Node("e")
node_d = Node("d")
node_f = Node("f")
node_i = Node("i")
node_h = Node("h")
node_j = Node("j")
node_k = Node("k")

binary_tree.insert(root)
binary_tree.insert(node_c)
binary_tree.insert(node_b)
binary_tree.insert(node_a)
binary_tree.insert(node_e)
binary_tree.insert(node_d)
binary_tree.insert(node_f)
binary_tree.insert(node_i)
binary_tree.insert(node_h)
binary_tree.insert(node_j)
binary_tree.insert(node_k)

binary_tree.inorder_print(root)
