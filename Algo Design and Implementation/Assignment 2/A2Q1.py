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

def insert_into_bst(root, value):
    if root is None:
        return TreeNode(value)
    if value < root.value:
        root.left = insert_into_bst(root.left, value)
    else:
        root.right = insert_into_bst(root.right, value)
    return root

def preOrderSort(tree):
    
    def find_root(tree):
        all_nodes = set()
        child_nodes = set()
        
        for node in tree:
            value, left, right = node
            all_nodes.add(value)
            if left != 'x':
                child_nodes.add(left)
            if right != 'x':
                child_nodes.add(right)
        
        root = list(all_nodes - child_nodes)[0]
        return root

    def build_bst_from_tree(tree):
        
        root_value = find_root(tree)
        root = TreeNode(int(root_value))
        inserted_values = {int(root_value)}
        
        for value, left, right in tree:
            if int(value) not in inserted_values:
                root = insert_into_bst(root, int(value))
                inserted_values.add(int(value))
            if left != 'x' and int(left) not in inserted_values:
                root = insert_into_bst(root, int(left))
                inserted_values.add(int(left))
            if right != 'x' and int(right) not in inserted_values:
                root = insert_into_bst(root, int(right))
                inserted_values.add(int(right))
    
        return root

    def traverse_pre_order(node):
        if node is None:
            return []
        
        return [str(node.value)] + traverse_pre_order(node.left) + traverse_pre_order(node.right)

    bst_root = build_bst_from_tree(tree)
    return ' '.join(traverse_pre_order(bst_root))


tree = [['-1', '1', '-2'], ['-2', '0', 'x'], ['1', 'x', 'x'],['0', 'x', 'x']]
tree2 = [['6988', 'x', 'x'], ['-1558', 'x', '-2208'], ['-11982', 'x', 'x'], ['5785', 'x', 'x'], ['-20794', '6634', '17264'], ['11396', '8964', 'x'], ['-74', '-9300', 'x'], ['8964', 'x', 'x'], ['-268', 'x', '6988'], ['6634', 'x', '-268'], ['-9300', '-20794', '8559'], ['-84', '11396', 'x'], ['8559', '649', '-11982'], ['649', 'x', 'x'], ['17264', '-14935', 'x'], ['-2208', 'x', '-84'], ['8234', 'x', '-74'], ['-14935', '-1558', '5785']]

output1 = preOrderSort(tree)
print(output1)

print("\n")

#output2 = preOrderSort(tree2)
#print(output2)


'''
def find_root(tree):
    all_nodes = set()
    child_nodes = set()
    
    for node in tree:
        value, left, right = node
        all_nodes.add(value)
        if left != 'x':
            child_nodes.add(left)
        if right != 'x':
            child_nodes.add(right)
    
    root = list(all_nodes - child_nodes)[0]
    return root

def print_tree(tree):
    nodes = {}
    for node in tree:
        value, left, right = node
        nodes[value] = (left, right)
    
    result = []
    
    def traverse(node):
        if node == 'x':
            return
        left, right = nodes.get(node, ('x', 'x'))
        result.append(node)
        traverse(left)
        traverse(right)
    
    root = find_root(tree)
    traverse(root)
    
    return ', '.join(result)

tree = [['0', 'x', 'x'], ['-1', '1', '-2'], ['-2', '0', 'x'], ['1', 'x', 'x']]
tree2 = [['6988', 'x', 'x'], ['-1558', 'x', '-2208'], ['-11982', 'x', 'x'], ['5785', 'x', 'x'], ['-20794', '6634', '17264'], ['11396', '8964', 'x'], ['-74', '-9300', 'x'], ['8964', 'x', 'x'], ['-268', 'x', '6988'], ['6634', 'x', '-268'], ['-9300', '-20794', '8559'], ['-84', '11396', 'x'], ['8559', '649', '-11982'], ['649', 'x', 'x'], ['17264', '-14935', 'x'], ['-2208', 'x', '-84'], ['8234', 'x', '-74'], ['-14935', '-1558', '5785']]
output = print_tree(tree)
print(output)
'''