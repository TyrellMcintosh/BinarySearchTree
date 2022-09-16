import random
import time
from bst import BinarySearchTree

class Program:
    """Provides the data and which operations to execute"""
    root = None
    bst = BinarySearchTree()
    SIZE = 10
    list_ = [0] * SIZE  #Initialize the list to a given length

    print('Elements to be inserted into the tree')
    count = 0
    while count != SIZE:
        list_[count] = random.randint(1,100)
        print(list_[count])
        count += 1

    start = time.time()
    for x in list_:
        root = bst.insert(root, x)
    finish = time.time()

    performance = "{:.2f}".format(finish - start)
    print("Binary Search Tree Insertion Time: ", performance)

    print('Inorder Traversal:')
    bst.in_order(root)

    print('Preorder Traversal:')
    bst.pre_order(root)

    print('Postorder Traversal:')
    bst.post_order(root)

    min = bst.find_smallest(root)
    max = bst.find_largest(root)
    # f string
    print(f"Smallest: {min} and Largest: {max}")
