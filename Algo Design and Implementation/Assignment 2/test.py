class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

def inorder_traversal_collect(root, values):
    if root:
        inorder_traversal_collect(root.left, values)
        values.append(root.val)
        inorder_traversal_collect(root.right, values)

def inorder_traversal_replace(root, values_iter):
    if root:
        inorder_traversal_replace(root.left, values_iter)
        root.val = next(values_iter)
        inorder_traversal_replace(root.right, values_iter)

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

def binary_tree_to_bst(root):
    if not root:
        return None
    
    values = []
    inorder_traversal_collect(root, values)
    
    values.sort()
    
    values_iter = iter(values)
    inorder_traversal_replace(root, values_iter)
    
    return root

def pre_order_traversal(root):
    if root is None:
        return []
    return [root.val] + pre_order_traversal(root.left) + pre_order_traversal(root.right)


#tree = [['0', 'x', 'x'], ['-1', '1', '-2'], ['-2', '0', 'x'], ['1', 'x', 'x']]
tree = [['6988', 'x', 'x'], ['-1558', 'x', '-2208'], ['-11982', 'x', 'x'], ['5785', 'x', 'x'], ['-20794', '6634', '17264'], ['11396', '8964', 'x'], ['-74', '-9300', 'x'], ['8964', 'x', 'x'], ['-268', 'x', '6988'], ['6634', 'x', '-268'], ['-9300', '-20794', '8559'], ['-84', '11396', 'x'], ['8559', '649', '-11982'], ['649', 'x', 'x'], ['17264', '-14935', 'x'], ['-2208', 'x', '-84'], ['8234', 'x', '-74'], ['-14935', '-1558', '5785']]


binary_tree_root = find_root(tree)
binary_tree = build_tree(tree, binary_tree_root)
print("binary tree pre-order: ", pre_order_traversal(binary_tree)) # 0 -1 1 -2
# Converting binary tree to BST
bst_root = binary_tree_to_bst(binary_tree)
print(pre_order_traversal(bst_root)) # 15



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

# Helper function to insert a value into the BST

    if root is None:
        return TreeNode(value)
    
    if value < root.value:
        root.left = insert_into_bst(root.left, value)
    else:
        root.right = insert_into_bst(root.right, value)
    
    return root

def collect_values_by_level(node, level, levels):
    if node is None:
        return
    if level not in levels:
        levels[level] = []
    levels[level].append(node.value)
    collect_values_by_level(node.left, level + 1, levels)
    collect_values_by_level(node.right, level + 1, levels)

# Function to construct BST from the original binary tree and sorted values
def construct_bst(tree, values, root_value):
    root = build_tree(tree, root_value)
    
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

# Function to display the tree in pre-order traversal
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
print("Binary Tree: ", pre_order_traversal(root))

# Step 1: Perform in-order traversal to collect node values
values = []
in_order_traversal_collect(root, values)
# Step 2: Sort the collected node values
values.sort()
#step 3 construct the bst
bst_root = construct_bst(tree, values, root_value)
print("BST: ", pre_order_traversal(bst_root))

# Display the BST in pre-order traversal
#print(pre_order_traversal(bst_root))




'''
