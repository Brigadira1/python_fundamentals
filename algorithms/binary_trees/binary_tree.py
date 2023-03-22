from node import Node


class BinaryTree:


    def __init__(self):
        self.root = None
        self.current_node = None
        self.adjacency_list = dict()

    def insert_node(self, node):

        if self.root is None:
            self.root = node
            self.current_node = node

        if node.data < self.current_node.data:
            if self.current_node.left is None:
                self.current_node.left = node
                self.current_node = self.root

            else:
                self.current_node = self.current_node.left
                self.insert_node(node)

        elif node.data > self.current_node.data:
            if self.current_node.right is None:
                self.current_node.right = node
                self.current_node = self.root
            else:
                self.current_node = self.current_node.right
                self.insert_node(node)

        else:
            print("Invalid value - it already exists. Two node with the same values are not allowed in binary trees!")

    def inorder_printing(self, node):

        if node is None:
            return
        self.inorder_printing(node.left)
        print(node.data, end=" ")
        self.inorder_printing(node.right)

    def preoder_printing(self, node):

        if node is None:
            return

        print(node.data, end=" ")
        self.preoder_printing(node.left)
        self.preoder_printing(node.right)

    def postoder_printing(self, node):

        if node is None:
            return

        self.postoder_printing(node.right)
        print(node.data, end=" ")
        self.postoder_printing(node.left)

    def depth_first_search(self,node):
        if node is None:
            return

        self.depth_first_search(node.left)
        print(node.data, end=" ")
        self.depth_first_search(node.right)

    def create_adjacency_list(self, node):
        if node is None:
            return

        self.adjacency_list[node.data] = []

        self.create_adjacency_list(node.left)

        if node.left is not None:
            self.adjacency_list[node.data].append(node.left.data)

        if node.right is not None:
            self.adjacency_list[node.data].append(node.right.data)

        self.create_adjacency_list(node.right)

        return self.adjacency_list

    def tree_height(self, node):

        if node is None:
            return -1

        left_height = self.tree_height(node.left)
        right_height = self.tree_height(node.right)

        return max(left_height, right_height) + 1

    def max(self, a, b):

        if a >= b:
            return a
        else:
             return b




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

binary_tree.inorder_printing(root)
print()
binary_tree.preoder_printing(root)
print()
binary_tree.postoder_printing(root)
print()
binary_tree.depth_first_search(root)
print()
adjacency_list = binary_tree.create_adjacency_list(root)
print(adjacency_list)

print(binary_tree.tree_height(root))

