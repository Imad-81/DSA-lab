# ------------------------------
# Red-Black Tree Implementation
# ------------------------------

# Node class
class Node:
    def __init__(self, data):
        self.data = data
        self.color = "RED"          # New node is always RED
        self.left = None
        self.right = None
        self.parent = None


# Red-Black Tree class
class RedBlackTree:

    def __init__(self):
        # Create a special NIL node (Black)
        self.NIL = Node(0)
        self.NIL.color = "BLACK"
        self.root = self.NIL

    # ------------------------------
    # Left Rotation
    # ------------------------------
    def left_rotate(self, x):

        y = x.right                  # Right child becomes parent
        x.right = y.left

        if y.left != self.NIL:
            y.left.parent = x

        y.parent = x.parent

        if x.parent is None:
            self.root = y
        elif x == x.parent.left:
            x.parent.left = y
        else:
            x.parent.right = y

        y.left = x
        x.parent = y

    # ------------------------------
    # Right Rotation
    # ------------------------------
    def right_rotate(self, y):

        x = y.left                   # Left child becomes parent
        y.left = x.right

        if x.right != self.NIL:
            x.right.parent = y

        x.parent = y.parent

        if y.parent is None:
            self.root = x
        elif y == y.parent.right:
            y.parent.right = x
        else:
            y.parent.left = x

        x.right = y
        y.parent = x

    # ------------------------------
    # Insert Operation
    # ------------------------------
    def insert(self, key):

        # Create new node
        node = Node(key)
        node.left = self.NIL
        node.right = self.NIL

        parent = None
        current = self.root

        # Find correct position for insertion
        while current != self.NIL:
            parent = current

            if node.data < current.data:
                current = current.left
            else:
                current = current.right

        node.parent = parent

        # Insert node
        if parent is None:
            self.root = node

        elif node.data < parent.data:
            parent.left = node

        else:
            parent.right = node

        # New node is RED
        node.color = "RED"

        # Fix Red-Black Tree properties
        self.fix_insert(node)

    # ------------------------------
    # Fix Tree after Insertion
    # ------------------------------
    def fix_insert(self, k):

        while k != self.root and k.parent.color == "RED":

            # Parent is left child
            if k.parent == k.parent.parent.left:

                uncle = k.parent.parent.right

                # Case 1: Uncle is RED
                if uncle.color == "RED":

                    k.parent.color = "BLACK"
                    uncle.color = "BLACK"
                    k.parent.parent.color = "RED"

                    k = k.parent.parent

                else:

                    # Case 2: Left Rotation
                    if k == k.parent.right:
                        k = k.parent
                        self.left_rotate(k)

                    # Case 3: Right Rotation
                    k.parent.color = "BLACK"
                    k.parent.parent.color = "RED"

                    self.right_rotate(k.parent.parent)

            # Parent is right child
            else:

                uncle = k.parent.parent.left

                # Case 1: Uncle is RED
                if uncle.color == "RED":

                    k.parent.color = "BLACK"
                    uncle.color = "BLACK"
                    k.parent.parent.color = "RED"

                    k = k.parent.parent

                else:

                    # Case 2: Right Rotation
                    if k == k.parent.left:
                        k = k.parent
                        self.right_rotate(k)

                    # Case 3: Left Rotation
                    k.parent.color = "BLACK"
                    k.parent.parent.color = "RED"

                    self.left_rotate(k.parent.parent)

        # Root is always BLACK
        self.root.color = "BLACK"

    # ------------------------------
    # Search Operation
    # ------------------------------
    def search(self, node, key):

        # Element found or tree ended
        if node == self.NIL or node.data == key:
            return node

        # Search in left subtree
        if key < node.data:
            return self.search(node.left, key)

        # Search in right subtree
        return self.search(node.right, key)

    # ------------------------------
    # Inorder Traversal
    # ------------------------------
    def inorder(self, node):

        if node != self.NIL:

            self.inorder(node.left)

            print(node.data, "-", node.color)

            self.inorder(node.right)


# ------------------------------
# Main Program
# ------------------------------

tree = RedBlackTree()

# Read number of nodes
n = int(input("Enter number of nodes: "))

# Insert nodes
print("Enter node values:")

for i in range(n):
    value = int(input())
    tree.insert(value)

# Display tree
print("\nInorder Traversal:")
tree.inorder(tree.root)

# Search element
key = int(input("\nEnter element to search: "))

result = tree.search(tree.root, key)

if result != tree.NIL:
    print("Element Found:", result.data)
else:
    print("Element Not Found")