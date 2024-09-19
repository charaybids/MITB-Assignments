class BinaryTree:
    def __init__(self, root):
        self.key = root
        self.left_child = None
        self.right_child = None
    
    def insert_left(self, new_node):
        if self.left_child is None:
            self.left_child = BinaryTree(new_node)
        else:
            t = BinaryTree(new_node)
            t.left_child = self.left_child
            self.left_child = t
    
    def insert_right(self, new_node):
        if self.right_child is None:
            self.right_child = BinaryTree(new_node)
        else:
            t = BinaryTree(new_node)
            t.right_child = self.right_child
            self.right_child = t
    
    def get_right_child(self):
        return self.right_child
    
    def get_left_child(self):
        return self.left_child
    
    def set_root_val(self,obj):
        self.key = obj
        
    def get_root_val(self):
        return self.key

    def build_tree(self):
        r = BinaryTree(self.get_root_val())
        r.insert_left('b')
        r.insert_right('c')
        r.get_left_child().insert_right('d')
        r.get_right_child().insert_left('e')
        r.get_right_child().insert_right('f')
        r.get_left_child().get_right_child().insert_right('g')
        return r
    
    def print_tree_in_order(self):
    #this is a in-order traversal
    #the following order is left, root, right
        if self.left_child:
            self.left_child.print_tree_in_order()
        print(self.key)
        if self.right_child:
            self.right_child.print_tree_in_order()
    
    def print_tree_pre_order(self):
    #this is a pre-order traversal
    #the following order is root, left, right
        print(self.key)
        if self.left_child:
            self.left_child.print_tree_pre_order()
        if self.right_child:
            self.right_child.print_tree_pre_order()
    
    def print_tree_post_order(self):
        # This is a post-order traversal
        # The following order is left, right, root
        if self.left_child:
            self.left_child.print_tree_post_order()
        if self.right_child:
            self.right_child.print_tree_post_order()
        print(self.key)

    def print_tree_level_order(self):
        # This is a level-order traversal
        # The following order is level by level from top to bottom
        queue = [self]
        while queue:
            current = queue.pop(0)
            print(current.key)
            if current.left_child:
                queue.append(current.left_child)
            if current.right_child:
                queue.append(current.right_child)

# Build and print the tree
# Explanation:
# 1. In-order Traversal (print_tree_in_order):
#    - Visit the left subtree.
#    - Visit the root node.
#    - Visit the right subtree.
# 2. Pre-order Traversal (print_tree_pre_order):
#    - Visit the root node.
#    - Visit the left subtree.
#    - Visit the right subtree.
# 3. Post-order Traversal (print_tree_post_order):
#    - Visit the left subtree.
#    - Visit the right subtree.
#    - Visit the root node.
# 4. Level-order Traversal (print_tree_level_order):
#    - Visit nodes level by level from top to bottom and left to right within each level.
#    - This is implemented using a queue to keep track of nodes at each level.

tree = BinaryTree('a').build_tree()
print("In-order Traversal:")
tree.print_tree_in_order()
print("\nPre-order Traversal:")
tree.print_tree_pre_order()
print("\nPost-order Traversal:")
tree.print_tree_post_order()
print("\nLevel-order Traversal:")
tree.print_tree_level_order()

# Other uncommon methods
# Certainly! Here are some examples of problems where uncommon traversal methods might be used, along with their typical time complexities:

# 1. Reverse In-order Traversal:
#    - Problem: Finding the k-th largest element in a binary search tree (BST).
#    - Big O Complexity: O(n) for time and O(h) for space, where n is the number of nodes and h is the height of the tree.

# 2. Reverse Pre-order Traversal:
#    - Problem: Serializing a binary tree in a specific order for storage or transmission.
#    - Big O Complexity: O(n) for time and O(h) for space.

# 3. Reverse Post-order Traversal:
#    - Problem: Deleting all nodes in a binary tree (useful in garbage collection).
#    - Big O Complexity: O(n) for time and O(h) for space.

# 4. Spiral Order Traversal (Zigzag Level Order):
#    - Problem: Printing a binary tree in a zigzag manner, which can be useful for visual representation or specific algorithms.
#    - Big O Complexity: O(n) for time and O(n) for space.

# 5. Boundary Traversal:
#    - Problem: Printing the boundary nodes of a binary tree, which can be useful in certain graphical applications or for specific tree-based algorithms.
#    - Big O Complexity: O(n) for time and O(h) for space.

# 6. Diagonal Traversal:
#    - Problem: Summing up all nodes that lie on the same diagonal in a binary tree, which can be useful in certain mathematical or graphical applications.
#    - Big O Complexity: O(n) for time and O(h) for space.

# 7. Vertical Order Traversal:
#    - Problem: Printing nodes of a binary tree in vertical order, which can be useful for certain types of data visualization or for solving specific tree-based problems.
#    - Big O Complexity: O(n log n) for time (due to sorting) and O(n) for space.


'''
# Test
# So the whole thing here is to firstly create a root node, then insert left and right children to it
# When accessing the left child node we access essentially a new tree, so we use the by get_root_val()


r = BinaryTree('a')
print("Root Val = ", r.get_root_val())
print("Left Child = ", r.get_left_child())
r.insert_left('b')
print("Left Child = ", r.get_left_child())

print(r.get_left_child().get_root_val())
r.insert_right('c')
print(r.get_right_child())
print(r.get_right_child().get_root_val())

r.get_right_child().set_root_val('hello')
print(r.get_right_child().get_root_val())
'''