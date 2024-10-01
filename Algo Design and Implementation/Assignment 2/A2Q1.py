'''
import sys

def to_CBST(a):
    return '0 -1 -2 1'

num_line = int(sys.stdin.readline())
for _ in range(num_line):
    a = [s.split(':') for s in sys.stdin.readline().split()]
    print(to_CBST(a))


'''


class TreeNode:
    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None

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
        if node[2] != 'x':
            nodes[node[0]].right = nodes[node[2]]
    
    return nodes[root_value]

def in_order_traversal(root):
    if root is None:
        return []
    return [root.value] + in_order_traversal(root.left)  + in_order_traversal(root.right)

def pre_order_traversal(root):
    if root is None:
        return []
    return [root.value] + pre_order_traversal(root.left) + pre_order_traversal(root.right)

def build_bst_from_inorder(inorder):
    if not inorder:
        return None
    
    root_value = inorder[0]
    root = TreeNode(root_value)
    
    for value in inorder[1:]:
        insert_into_bst(root, value)
    
    return root
#error here
def insert_into_bst(root, value):
    if value < root.value:
        if root.left is None:
            root.left = TreeNode(value)
        else:
            insert_into_bst(root.left, value)
    else:
        if root.right is None:
            root.right = TreeNode(value)
        else:
            insert_into_bst(root.right, value)

# Given tree structure
tree = [['0', 'x', 'x'], ['-1', '1', '-2'], ['-2', '0', 'x'], ['1', 'x', 'x']]

# Step 2: Find the root value
root_value = find_root(tree)
print("Root value of the tree:", root_value)

# Step 3: Build the binary tree from the root value
root = build_tree(tree, root_value)

# Step 4: Traverse in-order and print the order
inorder_result = in_order_traversal(root)
print("In-order traversal of the original tree:", " ".join(inorder_result))

# Step 5: Use the in-order traversal output to build a BST
bst_root = build_bst_from_inorder(inorder_result)

# Step 6: Display the tree using pre-order traversal
preorder_result = pre_order_traversal(bst_root)
print("Pre-order traversal of the constructed BST:", " ".join(preorder_result))


#print("\n")
#tree2 = [['6988', 'x', 'x'], ['-1558', 'x', '-2208'], ['-11982', 'x', 'x'], ['5785', 'x', 'x'], ['-20794', '6634', '17264'], ['11396', '8964', 'x'], ['-74', '-9300', 'x'], ['8964', 'x', 'x'], ['-268', 'x', '6988'], ['6634', 'x', '-268'], ['-9300', '-20794', '8559'], ['-84', '11396', 'x'], ['8559', '649', '-11982'], ['649', 'x', 'x'], ['17264', '-14935', 'x'], ['-2208', 'x', '-84'], ['8234', 'x', '-74'], ['-14935', '-1558', '5785']]
#output2 = preOrderSort(tree2)
#print(output2)
