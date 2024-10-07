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

def insert_into_bst(root, value):
    if root is None:
        return TreeNode(value)
    
    if value < root.value:
        if root.left is None:
            root.left = TreeNode(value, parent=root)
        else:
            insert_into_bst(root.left, value)
    else:
        if root.right is None:
            root.right = TreeNode(value, parent=root)
        else:
            insert_into_bst(root.right, value)
    
    return root

def in_order_traversal_collect(root, values):
    if root is None:
        return
    in_order_traversal_collect(root.left, values)
    values.append(root.value)
    in_order_traversal_collect(root.right, values)

def in_order_traversal_replace(root, values, index):
    if root is None:
        return index
    index = in_order_traversal_replace(root.left, values, index)
    root.value = values[index]
    index += 1
    index = in_order_traversal_replace(root.right, values, index)
    return index

# Function to display the tree in pre-order traversal
def pre_order_traversal(root):
    if root is None:
        return []
    return [root.value] + pre_order_traversal(root.left) + pre_order_traversal(root.right)

def print_tree(root):
    if not root:
        print("Tree is empty")
        return
    
    queue = deque([(root, 0)])
    current_level = 0
    level_nodes = []
    
    while queue:
        node, level = queue.popleft()
        
        if level > current_level:
            print(" ".join(level_nodes))
            level_nodes = []
            current_level = level
        
        if node:
            level_nodes.append(str(node.value))
            queue.append((node.left, level + 1))
            queue.append((node.right, level + 1))
        else:
            level_nodes.append("x")
    
    if level_nodes:
        print(" ".join(level_nodes))

#tree = [['0', 'x', 'x'], ['-1', '1', '-2'], ['-2', '0', 'x'], ['1', 'x', 'x']]
tree = [['6988', 'x', 'x'], ['-1558', 'x', '-2208'], ['-11982', 'x', 'x'], ['5785', 'x', 'x'], ['-20794', '6634', '17264'], ['11396', '8964', 'x'], ['-74', '-9300', 'x'], ['8964', 'x', 'x'], ['-268', 'x', '6988'], ['6634', 'x', '-268'], ['-9300', '-20794', '8559'], ['-84', '11396', 'x'], ['8559', '649', '-11982'], ['649', 'x', 'x'], ['17264', '-14935', 'x'], ['-2208', 'x', '-84'], ['8234', 'x', '-74'], ['-14935', '-1558', '5785']]

root_value = find_root(tree)
root = build_tree(tree, root_value)

# Step 1: Perform in-order traversal to collect node values
values = []
in_order_traversal_collect(root, values)

# Step 2: Sort the collected node values
values.sort()

# Step 3: Perform in-order traversal to replace node values with sorted values to maintain the structure
in_order_traversal_replace(root, values, 0)

# Display the BST
print(pre_order_traversal(root))


'''
num_line = int(sys.stdin.readline())
for _ in range(num_line):
    a = [s.split(':') for s in sys.stdin.readline().split()]
    print(to_CBST(a))
'''
