class Node:
    def __init__(self, info):
        self.info = info
        self.left = None
        self.right = None
        self.level = None

    def __str__(self):
        return str(self.info)


class SearchTree:
    def __init__(self):
        self.root = None

    def create(self, val):
        if self.root is None:
            self.root = Node(val)
        else:
            current = self.root
            while True:
                if val < current.info:
                    if current.left:
                        current = current.left
                    else:
                        current.left = Node(val)
                        break
                elif val > current.info:
                    if current.right:
                        current = current.right
                    else:
                        current.right = Node(val)
                        break
                else:
                    break

    def bft(self):
        self.root.level = 0
        queue = [self.root]
        out = []
        current_level = self.root.level

        while queue:
            current_node = queue.pop(0)

            if current_node.level > current_level:
                current_level += 1
                out.append("\n")

            out.append(str(current_node.info) + " ")

            if current_node.left:
                current_node.left.level = current_level + 1
                queue.append(current_node.left)

            if current_node.right:
                current_node.right.level = current_level + 1
                queue.append(current_node.right)

        print("".join(out))

    def inorder(self, node):
        if node is not None:
            self.inorder(node.left)
            print(node.info, end=" ")
            self.inorder(node.right)

    def preorder(self, node):
        if node is not None:
            print(node.info, end=" ")
            self.preorder(node.left)
            self.preorder(node.right)

    def postorder(self, node):
        if node is not None:
            self.postorder(node.left)
            self.postorder(node.right)
            print(node.info, end=" ")


tree = SearchTree()
arr = [8, 3, 1, 6, 4, 7, 10, 14, 13]
for i in arr:
    tree.create(i)

print('Breadth-First Traversal')
tree.bft()

print('\nInorder Traversal')
tree.inorder(tree.root)

print('\nPreorder Traversal')
tree.preorder(tree.root)

print('\nPostorder Traversal')
tree.postorder(tree.root)