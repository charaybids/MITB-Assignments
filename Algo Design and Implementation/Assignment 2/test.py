<<<<<<< HEAD
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
    root.data = arr.pop(0)
    array_to_bst(arr, root.left)
    array_to_bst(arr, root.right)

def binary_tree_to_bst(root):
    if root is None:
        return
    inorder = []
    store_inorder(root, inorder)
    inorder.sort()
    array_to_bst(inorder, root)
=======
class TreeNode:
    def __init__(self, value):
        self.value = int(value)
        self.left = None
        self.right = None

def insert_node(root, value):
    if root is None:
        return TreeNode(value)
    if int(value) < root.value:
        root.left = insert_node(root.left, value)
    elif int(value) > root.value:
        root.right = insert_node(root.right, value)
    return root

def pre_order_traversal(root, result):
    if root:
        result.append(root.value)
        pre_order_traversal(root.left, result)
        pre_order_traversal(root.right, result)

def build_bst(tree):
    root = None
    for entry in tree:
        if root is None:
            root = TreeNode(entry[0])
            if entry[1] != 'x':
                root.left = insert_node(root.left, entry[1])
            if entry[2] != 'x':
                root.right = insert_node(root.right, entry[2])
        else:
            root = insert_node(root, entry[0])
            if entry[1] != 'x':
                root = insert_node(root, entry[1])
            if entry[2] != 'x':
                root = insert_node(root, entry[2])
    return root

# Provided tree
tree = [['6988', 'x', 'x'], ['-1558', 'x', '-2208'], ['-11982', 'x', 'x'], ['5785', 'x', 'x'], 
        ['-20794', '6634', '17264'], ['11396', '8964', 'x'], ['-74', '-9300', 'x'], 
        ['8964', 'x', 'x'], ['-268', 'x', '6988'], ['6634', 'x', '-268'], ['-9300', '-20794', '8559'], 
        ['-84', '11396', 'x'], ['8559', '649', '-11982'], ['649', 'x', 'x'], 
        ['17264', '-14935', 'x'], ['-2208', 'x', '-84'], ['8234', 'x', '-74'], ['-14935', '-1558', '5785']]

# Build BST
root = build_bst(tree)

# Pre-order traversal
pre_order_result = []
pre_order_traversal(root, pre_order_result)

print(pre_order_result)
>>>>>>> a586687a1ec8375c2c84b598415d7e15cb9a14d1

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

<<<<<<< HEAD
# Example usage:
tree_array = [['6988', 'x', 'x'], ['-1558', 'x', '-2208'], ['-11982', 'x', 'x'], ['5785', 'x', 'x'], ['-20794', '6634', '17264'], ['11396', '8964', 'x'], ['-74', '-9300', 'x'], ['8964', 'x', 'x'], ['-268', 'x', '6988'], ['6634', 'x', '-268'], ['-9300', '-20794', '8559'], ['-84', '11396', 'x'], ['8559', '649', '-11982'], ['649', 'x', 'x'], ['17264', '-14935', 'x'], ['-2208', 'x', '-84'], ['8234', 'x', '-74'], ['-14935', '-1558', '5785']]
#tree_array = [['0', 'x', 'x'], ['-1', '1', '-2'], ['-2', '0', 'x'], ['1', 'x', 'x']]

root = build_tree(tree_array)

print("Inorder traversal of the original tree:")
inorder_traversal(root)
print("\n")

binary_tree_to_bst(root)

print("Preorder traversal of the converted BST:")
preorder_traversal(root)
print("\n")
=======

'''
# Provided tree
#tree = [['0', 'x', 'x'], ['-1', '1', '-2'], ['-2', '0', 'x'], ['1', 'x', 'x']]
tree = [['6988', 'x', 'x'], ['-1558', 'x', '-2208'], ['-11982', 'x', 'x'], ['5785', 'x', 'x'], ['-20794', '6634', '17264'], ['11396', '8964', 'x'], ['-74', '-9300', 'x'], ['8964', 'x', 'x'], ['-268', 'x', '6988'], ['6634', 'x', '-268'], ['-9300', '-20794', '8559'], ['-84', '11396', 'x'], ['8559', '649', '-11982'], ['649', 'x', 'x'], ['17264', '-14935', 'x'], ['-2208', 'x', '-84'], ['8234', 'x', '-74'], ['-14935', '-1558', '5785']]

# Build BST
root = build_bst_from_tree(tree)

# Pre-order traversal
pre_order_result = []
pre_order_traversal(root, pre_order_result)

print(pre_order_result)
'''
>>>>>>> a586687a1ec8375c2c84b598415d7e15cb9a14d1

'''
#passed input 1
from collections import deque

class TreeNode:
    def __init__(self, value=0, left=None, right=None, parent=None):
        self.value = value
        self.left = left
        self.right = right
        self.parent = parent
    def has_left_child(self):
        return self.left_child
    def has_right_child(self):
        return self.right_child
    def is_left_child(self):
        return self.parent and self.parent.left_child == self
    def is_right_child(self):
        return self.parent and self.parent.right_child == self
    def is_root(self):
        return not self.parent
    def is_leaf(self):
        return not (self.right_child or self.left_child)
    def has_any_children(self):
        return self.right_child or self.left_child
    def has_both_children(self):
        return self.right_child and self.left_child
    def replace_node_data(self, key, value, lc, rc):
        self.key = key
        self.payload = value
        self.left_child = lc
        self.right_child = rc
        if self.has_left_child():
            self.left_child.parent = self
        if self.has_right_child():
            self.right_child.parent = self

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
    return root

def build_tree(tree, root_value):
    nodes = {node[0]: TreeNode(node[0]) for node in tree}
    
    for node in tree:
        if node[1] != 'x':
            nodes[node[0]].left = nodes[node[1]]
            nodes[node[1]].parent = nodes[node[0]]
        if node[2] != 'x':
            nodes[node[0]].right = nodes[node[2]]
            nodes[node[2]].parent = nodes[node[0]]
    
    return nodes[root_value]

def construct_bst(root, values):
   
    # Step 1: Collect values by level
    levels = {}
    collect_values_by_level(root, 0, levels)
    
    # Step 2: Sort values at each level
    for level in levels:
        levels[level].sort()
    
    # Step 3: Replace values in the tree by level
    in_order_traversal_replace_level(root, values, 0, levels)
    
    return root

def in_order_traversal_collect(root, values):
    if root is None:
        return
    in_order_traversal_collect(root.left, values)
    values.append(root.value)
    in_order_traversal_collect(root.right, values)

def in_order_traversal_replace_level(node, values, level, levels):
    if node is None:
        return
    in_order_traversal_replace_level(node.left, values, level + 1, levels)
    node.value = levels[level].pop(0)
    in_order_traversal_replace_level(node.right, values, level + 1, levels)

def pre_order_traversal(root):
    if root is None:
        return []
    return [root.value] + pre_order_traversal(root.left) + pre_order_traversal(root.right)

def in_order_traversal(root):
    if root is None:
        return []
    return in_order_traversal(root.left) + [root.value] + in_order_traversal(root.right)

#tree = [['0', 'x', 'x'], ['-1', '1', '-2'], ['-2', '0', 'x'], ['1', 'x', 'x']]
tree = [['6988', 'x', 'x'], ['-1558', 'x', '-2208'], ['-11982', 'x', 'x'], ['5785', 'x', 'x'], ['-20794', '6634', '17264'], ['11396', '8964', 'x'], ['-74', '-9300', 'x'], ['8964', 'x', 'x'], ['-268', 'x', '6988'], ['6634', 'x', '-268'], ['-9300', '-20794', '8559'], ['-84', '11396', 'x'], ['8559', '649', '-11982'], ['649', 'x', 'x'], ['17264', '-14935', 'x'], ['-2208', 'x', '-84'], ['8234', 'x', '-74'], ['-14935', '-1558', '5785']]

root_value = find_root(tree)
root = build_tree(tree, root_value)

values = []
in_order_traversal_collect(root, values)
values.sort()
#step 3 construct the bst


print("BST: ", pre_order_traversal(bst_root))

# Display the BST in pre-order traversal
#print(pre_order_traversal(bst_root))
'''




