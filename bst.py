from node import Node

class BinarySearchTree():
    """Contains several methods to perform operations on the BST"""
    def __init__(self):
        print("init")

    def insert(self,root,val):
        """Insertion depending on current values in tree"""
        if root is None:
            root = Node()
            root.value = val
        elif val < root.value:
            root.left = self.insert(root.left,val)
            root.left.parent = root
        else:
            root.right = self.insert(root.right,val)
            root.right.parent = root
        return root

    def in_order(self,root):
        """Inorder traversal from left, to root, to right"""
        if root is not None:
            self.in_order(root.left)
            print(root.value)
            self.in_order(root.right)

    def pre_order(self,root):
        """Preorder traversal from root, to left, to right"""
        if root is not None:
            print(root.value)
            self.pre_order(root.left)
            self.pre_order(root.right)

    def post_order(self,root):
        """Postorder traversal from left, to right, to root"""
        if root is not None:
            self.post_order(root.left)
            self.post_order(root.right)
            print(root.value)

    def find_smallest(self,root):
        """Returns the smallest value in the tree"""
        if root.left is None:
            return root.value
        return self.find_smallest(root.left)

    def find_largest(self,root):
        """Returns the smallest value in the tree"""
        if root.right is None:
            return root.value
        return self.find_largest(root.right)
