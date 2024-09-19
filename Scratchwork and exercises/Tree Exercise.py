'''
my_tree = ['a', ['b', ['d',[],[]], ['e',[],[]] ], ['c',
['f',[],[]], []] ]

print(my_tree)
print('left subtree = ', my_tree[1])
print('root = ', my_tree[0])
print('right subtree = ', my_tree[2])
'''

def binary_tree(r):
    #Simply constructs a list with a root node and two empty sublists for the children
    #The root node is stored in the first index of the list 
    #The left child in the second index, and the right child in the third index
    return [r, [], []]

def insert_left(root, new_branch):
    
    #Pops the left child of the root node and stores it in a variable
    t = root.pop(1)
    
    #If the left child is not empty, it is stored in a list with the new branch as the left child
    if len(t) > 1:
        #The left child is stored in a list with the new branch as the left child
        #We push it down the tree by inserting it as the left child of the new branch
        root.insert(1, [new_branch, t, []])
    else:
        #If the left child is empty, the new branch is inserted as the left child
        root.insert(1, [new_branch, [], []])
        
    return root

def insert_right(root, new_branch):
    
    t = root.pop(2)
    
    if len(t) > 1:
        root.insert(2, [new_branch, [], t])
    else:
        root.insert(2, [new_branch, [], []])
    
    return root

def get_root_val(root):
    return root[0]

def set_root_val(root, new_val):
    root[0] = new_val

def get_left_child(root):
    return root[1]

def get_right_child(root):
    return root[2] 

def build_tree():
    
    #to buid a tree with the root node 'a' and the following structure:
    #     a
    #    / \
    #   b   c
    #    \  / \
    #     d e  f
      
    r = binary_tree('a')
    insert_left(r, 'b')
    insert_right(r, 'c')
    insert_right(get_left_child(r), 'd')
    insert_left(get_right_child(r), 'e')
    insert_right(get_right_child(r), 'f')
    return r

'''
#testing
r = binary_tree(3)
insert_left(r, 4)
insert_left(r, 5)
insert_right(r, 6)
insert_right(r, 7)
l = get_left_child(r)
print(l)
set_root_val(l, 9)
print(r)
insert_left(l, 11)
print(r)

print(get_right_child(get_right_child(r)))
'''

