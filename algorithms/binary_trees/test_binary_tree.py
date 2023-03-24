import collections

from node import Node

class BinaryTree:

    def __init__(self):
        self.root = None
        self.current = None

    def insert_node(self, node):

        if not self.root:
            self.root = node
            self.current = root
                        
        if node.data < self.current.data:

            if not self.current.left:
                self.current.left = node
                self.current = self.root

            else:
                self.current = self.current.left
                self.insert_node(node)
                
        elif node.data > self.current.data:

            if not self.current.right:
                self.current.right = node
                self.current = self.root

            else:
                self.current = self.current.right
                self.insert_node(node)

    def inorder_print(self, node):

        if not node:
            return

        self.inorder_print(node.left)
        print(node.data, end=" ")
        self.inorder_print(node.right)

    def level_search(self):
        if not self.root:
            return

        visited = []
        queue = collections.deque()
        current = self.root
        queue.append(current)

        while queue:
            current = queue.popleft()
            data = current.data
            if current.left:
                queue.append(current.left)

            if current.right:
                queue.append(current.right)

            visited.append(data)

        return visited





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

print("Inorder print of the tree:")
binary_tree.inorder_print(root)
print()
print()
print("Level print of the tree:")
level_list = binary_tree.level_search()

for item in level_list:
    print(f"{item}", end=" ")



