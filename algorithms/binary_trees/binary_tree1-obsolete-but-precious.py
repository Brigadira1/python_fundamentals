from node import Node


class BinaryTree1:

    def __init__(self):
        self.root = None
        self.current = None

    # def insert(self, node):
    #     if self.root is None:
    #         self.root = node
    #     else:
    #         self._insert(self.root, node)
    #
    # def _insert(self, current, node):
    #     if node.data < current.data:
    #         if current.left is None:
    #             current.left = node
    #         else:
    #             self._insert(current.left, node)
    #
    #     elif node.data > current.data:
    #         if current.right is None:
    #             current.right = node
    #         else:
    #             current = current.right
    #             self._insert(current, node)

    # def insert(self, node):
    #
    #     if self.current is None:
    #         self.current = node
    #         # self.root = node
    #     elif node.data < self.current.data:
    #         if self.current.left is None:
    #             self.current.left = node
    #             # self.current = self.root
    #         else:
    #             self.current = self.current.left
    #             self.insert(node)
    #     elif node.data > self.current.data:
    #         if self.current.right is None:
    #             self.current.right = node
    #             # self.current = self.root
    #         else:
    #             self.current = self.current.right
    #             self.insert(node)
    #     else:
    #         print("There is a node with this data in the binary tree")

    def insert_node(self, node):

        if self.current is None:
            self.current = node
            self.root = node
        elif node.data < self.current.data:
            if self.current.left is None:
                self.current.left = node
                self.current = self.root
            else:
                self.current = self.current.left
                self.insert_node(node)
        elif node.data > self.current.data:
            if self.current.right is None:
                self.current.right = node
                self.current = self.root
            else:
                self.current = self.current.right
                self.insert_node(node)
        else:
            print("There is a node with this data in the binary tree")

    def inorder_print(self, node):

        if node is None:
            return
        else:
            self.inorder_print(node.left)
            print(node.data, end= " ")
            self.inorder_print(node.right)

# root = Node("g")
binary_tree = BinaryTree1()
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

binary_tree.insert_node(root)
binary_tree.insert_node(node_c)
binary_tree.insert_node(node_b)
binary_tree.insert_node(node_a)
binary_tree.insert_node(node_e)
binary_tree.insert_node(node_d)
binary_tree.insert_node(node_f)
binary_tree.insert_node(node_i)
binary_tree.insert_node(node_h)
binary_tree.insert_node(node_j)
binary_tree.insert_node(node_k)

binary_tree.inorder_print(root)

