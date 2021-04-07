import collections


class BinarySearchTree:
    def __init__(self):
        self.root = None

    def insert(self, value):
        node = Node(value)
        if self.root is None:
            self.root = node
            return
        else:
            current = self.root
            while True:
                if value == current.value:
                    return None
                if value < current.value:
                    if current.left is None:
                        current.left = node
                        return
                    else:
                        current = current.left
                elif value > current.value:
                    if current.right is None:
                        current.right = node
                        return
                    else:
                        current = current.right

    def find(self, value):
        if value == self.root:
            return self.root
        if self.root is None:
            return None
        else:
            current = self.root
            found = False
            while current and not found:
                if value == current.value:
                    found = True
                    break
                if value < current.value:
                    current = current.left
                if value > current.value:
                    current = current.right
            if found:
                return True
            else:
                return False

    def BFS(self):
        node = self.root
        data = []
        queue = collections.deque()
        queue.append(self.root)
        while len(queue) is not 0:
            node = queue.popleft()
            data.append(node.value)
            if node.left:
                queue.append(node.left)
            if node.right:
                queue.append(node.right)
        return data

    def DFS_pre_order(self):
        data = []

        def traverse(node):
            data.append(node.value)
            if node.left:
                traverse(node.left)
            if node.right:
                traverse(node.right)

        traverse(self.root)
        return data


class Node:
    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None


tree = BinarySearchTree()
tree.root = Node(10)
tree.insert(10)
tree.insert(6)
tree.insert(15)
tree.insert(3)
tree.insert(8)
tree.insert(20)
print(tree.DFS_pre_order())
print(tree.BFS())
