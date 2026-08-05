# Node class
class BinomialNode:
    def __init__(self, key):
        self.key = key              # Value stored in the node
        self.degree = 0             # Number of children
        self.parent = None          # Parent pointer
        self.child = None           # Leftmost child
        self.sibling = None         # Next sibling


# Binomial Heap class
class BinomialHeap:

    def __init__(self):
        self.head = None            # Pointer to root list

    # Merge two binomial trees of the same degree
    def merge_trees(self, tree1, tree2):

        # Smaller key becomes the root
        if tree1.key > tree2.key:
            tree1, tree2 = tree2, tree1

        tree2.parent = tree1
        tree2.sibling = tree1.child
        tree1.child = tree2
        tree1.degree += 1

        return tree1

    # Merge two root lists
    def merge_heap(self, h1, h2):

        if h1 is None:
            return h2
        if h2 is None:
            return h1

        # Select first root
        if h1.degree <= h2.degree:
            head = h1
            h1 = h1.sibling
        else:
            head = h2
            h2 = h2.sibling

        tail = head

        # Merge according to degree
        while h1 and h2:
            if h1.degree <= h2.degree:
                tail.sibling = h1
                h1 = h1.sibling
            else:
                tail.sibling = h2
                h2 = h2.sibling

            tail = tail.sibling

        if h1:
            tail.sibling = h1
        else:
            tail.sibling = h2

        return head

    # Union operation
    def union(self, other_head):

        self.head = self.merge_heap(self.head, other_head)

        if self.head is None:
            return

        prev = None
        curr = self.head
        next_node = curr.sibling

        while next_node:

            if (curr.degree != next_node.degree or
               (next_node.sibling and
                next_node.sibling.degree == curr.degree)):

                prev = curr
                curr = next_node

            else:

                if curr.key <= next_node.key:
                    curr.sibling = next_node.sibling
                    curr = self.merge_trees(curr, next_node)

                else:
                    if prev is None:
                        self.head = next_node
                    else:
                        prev.sibling = next_node

                    curr = self.merge_trees(next_node, curr)

            next_node = curr.sibling

    # Insert a new key
    def insert(self, key):

        temp = BinomialHeap()
        temp.head = BinomialNode(key)

        self.union(temp.head)

    # Find minimum element
    def get_min(self):

        if self.head is None:
            return None

        minimum = float("inf")
        current = self.head

        while current:
            if current.key < minimum:
                minimum = current.key

            current = current.sibling

        return minimum

    # Reverse child list
    def reverse(self, node):

        prev = None

        while node:
            next_node = node.sibling
            node.sibling = prev
            node.parent = None
            prev = node
            node = next_node

        return prev

    # Extract minimum element
    def extract_min(self):

        if self.head is None:
            return None

        prev_min = None
        min_node = self.head

        prev = None
        curr = self.head

        minimum = curr.key

        while curr:

            if curr.key < minimum:
                minimum = curr.key
                prev_min = prev
                min_node = curr

            prev = curr
            curr = curr.sibling

        # Remove minimum node
        if prev_min:
            prev_min.sibling = min_node.sibling
        else:
            self.head = min_node.sibling

        # Reverse child list and merge again
        child = self.reverse(min_node.child)
        self.union(child)

        return minimum

    # Display all nodes
    def display_tree(self, node):

        while node:
            print(node.key, end=" ")

            if node.child:
                self.display_tree(node.child)

            node = node.sibling

    def display(self):

        if self.head is None:
            print("\nHeap is Empty\n")
            return

        print("\nElements in Binomial Heap:")

        self.display_tree(self.head)

        print("\n")


# -------------------------------
# Main Program (Menu Driven)
# -------------------------------

heap = BinomialHeap()

while True:

    print("\n====== BINOMIAL HEAP ======")
    print("1. Insert")
    print("2. Find Minimum")
    print("3. Extract Minimum")
    print("4. Display Heap")
    print("5. Exit")

    choice = int(input("Enter your choice: "))

    if choice == 1:

        value = int(input("Enter element to insert: "))
        heap.insert(value)

        print(value, "inserted successfully.")

    elif choice == 2:

        minimum = heap.get_min()

        if minimum is None:
            print("Heap is Empty")
        else:
            print("Minimum Element =", minimum)

    elif choice == 3:

        minimum = heap.extract_min()

        if minimum is None:
            print("Heap is Empty")
        else:
            print("Deleted Minimum Element =", minimum)

    elif choice == 4:

        heap.display()

    elif choice == 5:

        print("Program Ended.")
        break

    else:

        print("Invalid Choice!")