class TreeNode:
    def __init__(self, key):
        self.left = None
        self.right = None
        self.val = key

def construct_tree(subtrees):
    nodes = {}
    children = set()

    # Create nodes and store children
    for subtree in subtrees:
        value, left, right = subtree
        if value not in nodes:
            nodes[value] = TreeNode(value)
        if left != 'x':
            if left not in nodes:
                nodes[left] = TreeNode(left)
            nodes[value].left = nodes[left]
            children.add(left)
        if right != 'x':
            if right not in nodes:
                nodes[right] = TreeNode(right)
            nodes[value].right = nodes[right]
            children.add(right)

    # Identify the root (node that is not anyone's child)
    root = None
    for value in nodes:
        if value not in children:
            root = nodes[value]
            break

    return root

def inorder(root):
    if root:
        inorder(root.left)
        print(root.val, end=' ')
        inorder(root.right)

def preorder(root):
    if root:
        print(root.val, end=' ')
        preorder(root.left)
        preorder(root.right)

def convertToBST(root):
    # Helper function to perform inorder traversal and collect nodes
    def inorder_collect(node, nodes):
        if node:
            inorder_collect(node.left, nodes)
            nodes.append(node.val)
            inorder_collect(node.right, nodes)

    # Helper function to convert sorted nodes list to BST
    def sorted_list_to_bst(nodes, start, end):
        if start > end:
            return None
        mid = (start + end) // 2
        node = TreeNode(nodes[mid])
        node.left = sorted_list_to_bst(nodes, start, mid - 1)
        node.right = sorted_list_to_bst(nodes, mid + 1, end)
        return node

    # Collect nodes in inorder
    nodes = []
    inorder_collect(root, nodes)
    nodes.sort()

    # Remove the original root value from the sorted list
    nodes.remove(root.val)

    # Convert sorted nodes list to BST and attach to the original root
    bst_root = sorted_list_to_bst(nodes, 0, len(nodes) - 1)
    root.left = bst_root.left
    root.right = bst_root.right

    return root

# Given subtrees
tree = [['0', 'x', 'x'], ['-1', '1', '-2'], ['-2', '0', 'x'], ['1', 'x', 'x']]

# Construct the tree
root = construct_tree(tree)

# Perform inorder traversal
print("Inorder traversal of the Binary Tree:")
inorder(root)
print()

# Convert to BST
bst_root = convertToBST(root)

# Perform inorder traversal of the BST
print("Inorder traversal of the Binary Search Tree:")
inorder(bst_root)
print()

# Perform preorder traversal of the BST
print("Preorder traversal of the Binary Search Tree:")
preorder(bst_root)
print()