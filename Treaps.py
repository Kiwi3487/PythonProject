class Treaps:
    def __init__(self, key, priority):
        self.key = key #Variable key
        self.priority = priority  # The priority (Heap property)
        self.left = None  # Left child reference
        self.right = None  # Right child reference


def rotate_right(y):
    x = y.left  # Set x as the left child of y
    y.left = x.right  # Move x's right subtree to y's left subtree
    x.right = y  # Make y the right child of x
    return x # return new root

def rotate_left(x):
    y = x.right  # Set y as the right child of x
    x.right = y.left  # Move y's left subtree to x's right subtree
    y.left = x  # Make x the left child of y
    return y  # Return y as the new node

def insert(root, key, priority):# inserts node into treap
    if root is None:
        return TreapNode(key, priority)

    if key < root.key: #checks value and if key is smaller than root key then place on left and rotates if there is a violation
        root.left = insert(root.left, key, priority)

        if root.left.priority > root.priority:
            root = rotate_right(root)  # Right rotate
    else:
        root.right = insert(root.right, key, priority) # if top if statement is false then insert into right instead

        if root.right.priority > root.priority:
            root = rotate_left(root)  # left rotate

    return root

def BST(root):
    if root is not None:
        BST(root.left)  # Traverse left subtree
        print(f"({root.key}, {root.priority})", end=" ")  # Print current node
        BST(root.right)  # Traverse right subtree

# num input
n = int(input("How many keys you want to enter: "))

data = []  # the list that stores the data

#user inout
print(f"Please enter {n} keys and their random values:")
for _ in range(n):
    key, priority = map(int, input().strip("()").split(","))  # read and convert inputs
    data.append((key, priority))  # Append the values to the list

root = None
for key, priority in data:
    root = insert(root, key, priority)  # insert into treap

BST(root)  # Call inorder function to display Treap
