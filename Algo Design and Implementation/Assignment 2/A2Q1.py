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
    return root

def build_tree(tree, root_value):
    nodes = {node[0]: TreeNode(node[0]) for node in tree}
    
    for node in tree:
        if node[1] != 'x':
            nodes[node[0]].left = nodes[node[1]]
        if node[2] != 'x':
            nodes[node[0]].right = nodes[node[2]]
    
    return nodes[root_value]

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

def to_CBST(a):
    root_value = find_root(a)
    root = build_tree(a, root_value)
    
    values = []
    in_order_traversal_collect(root, values)
    values.sort()
    in_order_traversal_replace(root, values, 0)
    
    return root

num_line = int(sys.stdin.readline())
for _ in range(num_line):
    a = [s.split(':') for s in sys.stdin.readline().split()]
    print(pre_order_traversal(to_CBST(a)))


#print("\n")
#tree = [['0', 'x', 'x'], ['-1', '1', '-2'], ['-2', '0', 'x'], ['1', 'x', 'x']]
#tree2 = [['6988', 'x', 'x'], ['-1558', 'x', '-2208'], ['-11982', 'x', 'x'], ['5785', 'x', 'x'], ['-20794', '6634', '17264'], ['11396', '8964', 'x'], ['-74', '-9300', 'x'], ['8964', 'x', 'x'], ['-268', 'x', '6988'], ['6634', 'x', '-268'], ['-9300', '-20794', '8559'], ['-84', '11396', 'x'], ['8559', '649', '-11982'], ['649', 'x', 'x'], ['17264', '-14935', 'x'], ['-2208', 'x', '-84'], ['8234', 'x', '-74'], ['-14935', '-1558', '5785']]
#output2 = preOrderSort(tree2)
#print(output2)
