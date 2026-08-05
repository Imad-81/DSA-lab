import math

class FibonacciNode:
    def __init__(self, key):
        self.key = key
        self.degree = 0
        self.mark = False
        self.parent = None
        self.child = None
        self.left = self
        self.right = self


class FibonacciHeap:
    def __init__(self):
        self.min_node = None
        self.total_nodes = 0

    # Insert operation
    def insert(self, key):
        node = FibonacciNode(key)

        if self.min_node is None:
            self.min_node = node
        else:
            node.left = self.min_node
            node.right = self.min_node.right
            self.min_node.right.left = node
            self.min_node.right = node

            if node.key < self.min_node.key:
                self.min_node = node

        self.total_nodes += 1
        return node

    # Find minimum
    def find_min(self):
        if self.min_node:
            return self.min_node.key
        return None

    # Remove minimum node
    def extract_min(self):
        z = self.min_node

        if z is not None:
            if z.child is not None:
                child = z.child
                while True:
                    next_child = child.right
                    child.parent = None

                    child.left = self.min_node
                    child.right = self.min_node.right
                    self.min_node.right.left = child
                    self.min_node.right = child

                    if next_child == z.child:
                        break
                    child = next_child

            # Remove minimum node
            z.left.right = z.right
            z.right.left = z.left

            if z == z.right:
                self.min_node = None
            else:
                self.min_node = z.right
                self.consolidate()

            self.total_nodes -= 1

        return z.key if z else None

    # Consolidation after extracting minimum
    def consolidate(self):
        degree_table = {}

        current = self.min_node
        nodes = []

        while True:
            nodes.append(current)
            current = current.right
            if current == self.min_node:
                break

        for node in nodes:
            x = node
            d = x.degree

            while d in degree_table:
                y = degree_table[d]

                if x.key > y.key:
                    x, y = y, x

                self.link(y, x)
                del degree_table[d]
                d += 1

            degree_table[d] = x

        self.min_node = None

        for node in degree_table.values():
            if self.min_node is None:
                self.min_node = node
            else:
                node.left = self.min_node
                node.right = self.min_node.right
                self.min_node.right.left = node
                self.min_node.right = node

                if node.key < self.min_node.key:
                    self.min_node = node

    # Link two trees
    def link(self, y, x):
        y.left.right = y.right
        y.right.left = y.left

        y.parent = x

        if x.child is None:
            x.child = y
            y.left = y
            y.right = y
        else:
            y.left = x.child
            y.right = x.child.right
            x.child.right.left = y
            x.child.right = y

        x.degree += 1
        y.mark = False

    # Decrease key operation
    def decrease_key(self, node, new_key):

        if new_key > node.key:
            print("New key is greater than current key")
            return

        node.key = new_key
        parent = node.parent

        if parent and node.key < parent.key:
            self.cut(node, parent)
            self.cascading_cut(parent)

        if node.key < self.min_node.key:
            self.min_node = node

    # Cut operation
    def cut(self, node, parent):

        if node.right == node:
            parent.child = None
        else:
            node.right.left = node.left
            node.left.right = node.right

            if parent.child == node:
                parent.child = node.right

        parent.degree -= 1

        node.parent = None
        node.left = self.min_node
        node.right = self.min_node.right
        self.min_node.right.left = node
        self.min_node.right = node

        node.mark = False

    # Cascading cut
    def cascading_cut(self, node):

        parent = node.parent

        if parent:
            if node.mark == False:
                node.mark = True
            else:
                self.cut(node, parent)
                self.cascading_cut(parent)

    # Display heap
    def display(self):

        if self.min_node is None:
            print("Heap is empty")
            return

        print("Fibonacci Heap:")

        temp = self.min_node

        while True:
            print(temp.key, end=" ")
            temp = temp.right

            if temp == self.min_node:
                break

        print()


# Main Program
heap = FibonacciHeap()

nodes = []

while True:

    print("\nFibonacci Heap Operations")
    print("1. Insert")
    print("2. Find Minimum")
    print("3. Extract Minimum")
    print("4. Decrease Key")
    print("5. Display")
    print("6. Exit")

    choice = int(input("Enter your choice: "))

    if choice == 1:
        key = int(input("Enter value: "))
        node = heap.insert(key)
        nodes.append(node)
        print("Inserted successfully")

    elif choice == 2:
        print("Minimum value:", heap.find_min())

    elif choice == 3:
        print("Extracted Minimum:", heap.extract_min())

    elif choice == 4:
        old = int(input("Enter existing value: "))
        new = int(input("Enter new value: "))

        for node in nodes:
            if node.key == old:
                heap.decrease_key(node, new)
                print("Key decreased")
                break

    elif choice == 5:
        heap.display()

    elif choice == 6:
        break

    else:
        print("Invalid choice")