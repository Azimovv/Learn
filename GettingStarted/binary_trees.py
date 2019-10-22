class Node:
    """Binary tree node"""

    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None


class BinaryTree:
    """This class represents a binary tree data structure"""
    def __init__(self, root):
        """
        :param root:Binary tree node
        """
        self.root = root


def breadth_first(leafy):
    """
    Breadth first search of binary tree, print out each node
    :param leafy: BinaryTree
    """
    current_level = [leafy]
    next_level = []
    while current_level:
        for node in current_level:
            print(node.value)
            if node.left:
                next_level.append(node.left)
            if node.right:
                next_level.append(node.right)
        current_level = next_level
        next_level = []


tree = Node("a")
tree.left = Node("b")
tree.right = Node("c")
tree.left.left = Node("d")
tree.right.right = Node("e")

breadth_first(tree)
