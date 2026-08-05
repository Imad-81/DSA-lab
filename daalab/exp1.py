# Experiment 1: B-Tree Operations (Search, Insertion, Deletion & Full B-Tree Implementation)

# ==========================================
# Part 1: B-Tree Node Search (Key Lookup)
# ==========================================
print("--- Part 1: B-Tree Node Search ---")
b_tree_node = [10, 20, 30, 40, 50]
key = int(input("Enter a number to search: "))

found = False
for k in b_tree_node: 
    if k == key: 
        found = True
        break

if found: 
    print("Entered element (key) found in the B-Tree node!")
else: 
    print("Entered element (key) is not found in the B-Tree node!")


# ==========================================
# Part 2: B-Tree Node Insertion (Sorted Order)
# ==========================================
print("\n--- Part 2: B-Tree Node Insertion ---")
b_tree_node = [10, 20, 30, 40, 50]
key = int(input("Enter number to insert: "))

inserted = False
for i in range(len(b_tree_node)):
    if key < b_tree_node[i]:
        b_tree_node.insert(i, key)
        inserted = True
        break

if not inserted: 
    b_tree_node.append(key)

print("Updated B-Tree node: ", b_tree_node)


# ==========================================
# Part 3: B-Tree Node Deletion
# ==========================================
print("\n--- Part 3: B-Tree Node Deletion ---")
b_tree_node = [10, 20, 30, 40, 50]
key = int(input("Enter the key to delete: "))
deleted = False
for i in range(len(b_tree_node)):
    if key == b_tree_node[i]:
        b_tree_node.pop(i)
        deleted = True
        break
if not deleted:
    print("Output: \n Entered element (key) not found in the B-Tree node!")
else:
    print("Output: \n Updated B-Tree node: ", b_tree_node)


# ==========================================
# Part 4: Full B-Tree Implementation
# ==========================================
print("\n--- Part 4: Full B-Tree Implementation ---")

class BTreeNode:
    def __init__(self, leaf=False):
        self.key = []
        self.child = []
        self.leaf = leaf

class BTree:
    def __init__(self, t):
        self.root = BTreeNode(True)
        self.t = t

    def insert(self, k):
        root = self.root
        if len(root.key) == (2 * self.t) - 1:
            temp = BTreeNode()
            self.root = temp
            temp.child.insert(0, root)
            self.split_child(temp, 0)
            self.insert_non_full(temp, k)
        else:
            self.insert_non_full(root, k)

    def insert_non_full(self, x, k):
        i = len(x.key) - 1
        if x.leaf:
            x.key.append(0)
            while i >= 0 and k < x.key[i]:
                x.key[i + 1] = x.key[i]
                i -= 1
            x.key[i + 1] = k
        else:
            while i >= 0 and k < x.key[i]:
                i -= 1
            i += 1
            if len(x.child[i].key) == (2 * self.t) - 1:
                self.split_child(x, i)
                if k > x.key[i]:
                    i += 1
            self.insert_non_full(x.child[i], k)

    def split_child(self, x, i):
        t = self.t
        y = x.child[i]
        z = BTreeNode(y.leaf)
        x.child.insert(i + 1, z)
        x.key.insert(i, y.key[t - 1])
        z.key = y.key[t:(2 * t) - 1]
        y.key = y.key[0:t - 1]
        if not y.leaf:
            z.child = y.child[t:2 * t]
            y.child = y.child[0:t]

    def print_tree(self, x, l=0):
        print("Level", l, " ", len(x.key), end=":")
        for i in x.key:
            print(i, end=" ")
        print()
        l += 1
        if len(x.child) > 0:
            for i in x.child:
                self.print_tree(i, l)

def main():
    b_tree = BTree(3)
    for i in range(10):
        b_tree.insert(i)
    b_tree.print_tree(b_tree.root)

if __name__ == "__main__":
    main()