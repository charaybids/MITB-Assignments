# 3/8 correct in online judge

import sys

class Node:
    def __init__(self, key):
        self.data = key
        self.left = None
        self.right = None

def build_tree(tree_array):
    if not tree_array:
        return None

    nodes = {val[0]: Node(val[0]) for val in tree_array}
    children = set()

    for val in tree_array:
        if val[1] != 'x':
            children.add(val[1])
        if val[2] != 'x':
            children.add(val[2])

    root_key = next(node for node in nodes if node not in children)
    root = nodes[root_key]

    for val in tree_array:
        node = nodes[val[0]]
        if val[1] != 'x':
            node.left = nodes[val[1]]
        if val[2] != 'x':
            node.right = nodes[val[2]]

<<<<<<< HEAD
=======
def build_tree(tree):
    nodes = {node[0]: TreeNode(node[0]) for node in tree}
    children = set()

    for node in tree:
        if node[1] != 'x':
            nodes[node[0]].left = nodes[node[1]]
            children.add(node[1])
        if node[2] != 'x':
            nodes[node[0]].right = nodes[node[2]]
            children.add(node[2])

    root_value = (set(nodes.keys()) - children).pop()
    return nodes[root_value]

def constructBst(root, nodes, index):
    if root is None:
        return index
    index = constructBst(root.left, nodes, index)
    root.value = nodes[index[0]]
    index[0] += 1
    index = constructBst(root.right, nodes, index)
    return index

# Function to convert a binary tree to a binary search tree
def binaryTreeToBst(root):
    nodes = in_order_traversal(root)
    nodes.sort()
    constructBst(root, nodes, [0])
    return root

# Function to display the tree in pre-order traversal
def pre_order_traversal(root):
    if root is None:
        return []
    return [root.value] + pre_order_traversal(root.left) + pre_order_traversal(root.right)

# Function to display the tree in pre-order traversal
def in_order_traversal(root):
    if root is None:
        return []
    return in_order_traversal(root.left) + [root.value] + in_order_traversal(root.right)

def to_CBST(a):
    
    root = build_tree(a)
    BST = binaryTreeToBst(root)
   
    return BST

num_line = int(sys.stdin.readline())
for _ in range(num_line):
    a = [s.split(':') for s in sys.stdin.readline().split()]
    print(in_order_traversal(to_CBST(a)))
    print("\n")


'''
import sys

class TreeNode:
    def __init__(self, value=0, left=None, right=None):
        self.value = value
        self.left = left
        self.right = right

def find_root(tree):
    all_nodes = set()
    child_nodes = set()
    
    for node in tree:
        all_nodes.add(node[0])
        if node[1] != 'x':
            child_nodes.add(node[1])
        if node[2] != 'x':
            child_nodes.add(node[2])
    
    root = list(all_nodes - child_nodes)[0]
>>>>>>> a586687a1ec8375c2c84b598415d7e15cb9a14d1
    return root

def store_inorder(node, inorder):
    if node is None:
        return
    store_inorder(node.left, inorder)
    inorder.append(node.data)
    store_inorder(node.right, inorder)

def array_to_bst(arr, root):
    if root is None:
        return
    
    array_to_bst(arr, root.left)
    root.data = arr.pop(0)
    array_to_bst(arr, root.right)

def binary_tree_to_bst(root):
    if root is None:
        return
    inorder = []
    store_inorder(root, inorder)
    inorder.sort()
    array_to_bst(inorder, root)

def inorder_traversal(root):
    if root is None:
        return
    inorder_traversal(root.left)
    print(root.data, end=' ')
    inorder_traversal(root.right)
    
def preorder_traversal(root):
    if root is None:
        return
    print(root.data, end=' ')
    preorder_traversal(root.left)
    preorder_traversal(root.right)

def to_CBST(a):
    root = build_tree(a)
    binary_tree_to_bst(root)
    preorder_traversal(root)
    print("\n")

num_line = int(sys.stdin.readline())
for _ in range(num_line):
    a = [s.split(':') for s in sys.stdin.readline().split()]
<<<<<<< HEAD
    to_CBST(a)


=======
    print(pre_order_traversal(to_CBST(a)))
'''
>>>>>>> a586687a1ec8375c2c84b598415d7e15cb9a14d1

#print("\n")
#tree = [['0', 'x', 'x'], ['-1', '1', '-2'], ['-2', '0', 'x'], ['1', 'x', 'x']]
#tree2 = [['6988', 'x', 'x'], ['-1558', 'x', '-2208'], ['-11982', 'x', 'x'], ['5785', 'x', 'x'], ['-20794', '6634', '17264'], ['11396', '8964', 'x'], ['-74', '-9300', 'x'], ['8964', 'x', 'x'], ['-268', 'x', '6988'], ['6634', 'x', '-268'], ['-9300', '-20794', '8559'], ['-84', '11396', 'x'], ['8559', '649', '-11982'], ['649', 'x', 'x'], ['17264', '-14935', 'x'], ['-2208', 'x', '-84'], ['8234', 'x', '-74'], ['-14935', '-1558', '5785']]
#output2 = preOrderSort(tree2)
#print(output2)
