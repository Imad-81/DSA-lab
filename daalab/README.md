# DAA Lab — Experiments 1 & 2

## Table of Contents

- [Experiment 1: B-Tree Search (Key Lookup)](#experiment-1-b-tree-search-key-lookup)
- [Experiment 2: B-Tree Insertion (Key Insertion in Sorted Order)](#experiment-2-b-tree-insertion-key-insertion-in-sorted-order)
- [Viva Questions & Answers](#viva-questions--answers)

---

## Experiment 1: B-Tree Search (Key Lookup)

### Code

```python
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
```

### What It Does

1. A static list `[10, 20, 30, 40, 50]` simulates a B-Tree node.
2. The user enters a number.
3. A linear search iterates through the list.
4. If the number matches any element, `found` is set to `True` and the loop breaks.
5. A message is printed indicating whether the key was found.

### Key Concepts

- **Linear / Sequential Search** — Checking each element one by one until a match is found. Complexity: **O(n)**.
- **Searching in a B-Tree node** — In a real B-Tree, each node holds **`n` keys** sorted in **ascending order**. Searching within a single node can be done via **linear scan** (or binary search for efficiency).
- **Flag variable** — `found` tracks success state. Once the key is located, `break` exits early to save iterations.
- **Edge cases** — Key not present (flag stays `False`), first-element match (early exit), last-element match (full traversal).

---

## Experiment 2: B-Tree Insertion (Key Insertion in Sorted Order)

### Code

```python
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
```

### What It Does

1. Starts with the same sorted list `[10, 20, 30, 40, 50]`.
2. The user enters a number to insert.
3. It scans the list to find the **correct sorted position** — the first element **greater than** the key.
4. `list.insert(i, key)` places the key at index `i`, shifting everything right.
5. If no such element is found (key is larger than all existing values), it **appends** to the end.
6. Prints the updated node.

### Key Concepts

- **Insertion Sort (one element)** — Finding the right spot in an already **sorted list** and inserting there. Complexity: **O(n)** (shift included in `insert`).
- **Maintaining sorted order** — B-Tree nodes must always remain sorted. This algorithm preserves that invariant.
- **`list.insert(index, value)`** — Python built-in; shifts all elements from `index` onward one position right. Under the hood, it requires moving O(n) elements.
- **`list.append(value)`** — Amortized O(1) operation for adding at the end.
- **Edge cases** — Insert smallest (placed at front, index 0), insert largest (appended), insert a duplicate (inserted before the equal value; B-Trees typically handle duplicates by storing in separate leaf or using comparison policy — here it just inserts before the first greater-or-equal).

---

## Viva Questions & Answers

### Q1: What is a B-Tree?

A **B-Tree** is a **self-balancing tree data structure** that maintains sorted data and allows **search, insertion, and deletion** in **O(log n)** time. Every node can contain **multiple keys** and have **more than two children**. It is widely used in databases and filesystems.

### Q2: What are the properties of a B-Tree of order `m`?

- Every node has **at most `m` children**.
- Every node (except root) has **at least `⌈m/2⌉` children**.
- The root has at least **2 children** if it is not a leaf.
- All leaves appear at the **same level**.
- A non-leaf node with `k` children contains **`k-1` keys**.
- All keys within a node are **sorted in ascending order**.

### Q3: How does searching work in a B-Tree?

Starting from the root, for each node we scan its keys linearly (or binary search). If the key matches, we are done. If the key lies between two adjacent keys `K[i]` and `K[i+1]`, we follow the child pointer at index `i+1` down into that subtree. This continues until we either find the key or reach a leaf without finding it.

### Q4: How does insertion work in a B-Tree?

We first **search** for the correct leaf node where the key should be placed. If the leaf has room (fewer than `m-1` keys), we **insert the key in sorted order**. If the leaf is **full**, we **split** it into two nodes, promote the median key to the parent, and recursively handle overflow up the tree.

### Q5: Why do these experiments use a Python list instead of a real tree structure?

These experiments **simulate a single B-Tree node** — the smallest unit of a B-Tree. A real implementation would require pointers/children, splitting, and balancing logic. Our goal here is to understand how **searching within a node** and **inserting in sorted order** works before implementing the full tree.

### Q6: What is the time complexity of the search in Experiment 1?

**O(n)** where `n` is the number of keys in the node (linear search). In a real B-Tree, each node's keys are sorted, so we could use binary search for O(log n) per node, but the overall tree search is O(log n) across all levels.

### Q7: What is the time complexity of the insertion in Experiment 2?

**O(n)** — finding the position costs O(n) and `list.insert()` also shifts O(n) elements. In a real B-Tree, insertion within a node also involves shifting keys, but the overall tree insertion is O(log n).

### Q8: What happens if you insert a key that already exists?

In our code, the condition `if key < b_tree_node[i]` inserts the duplicate **before** the first greater element. If the key equals an existing element, the condition `key < b_tree_node[i]` becomes `False`, so it skips over it. If it's greater than all, it appends. So duplicates are placed after equal values. In real B-Trees, duplicate handling depends on the implementation — they may be stored separately, use a count, or be disallowed.

### Q9: What is the difference between a B-Tree and a Binary Search Tree (BST)?

| Feature        | BST                          | B-Tree                               |
|----------------|------------------------------|--------------------------------------|
| Children/node  | 2                            | Up to `m`                            |
| Keys/node      | 1                            | Up to `m-1`                          |
| Height         | O(log n) to O(n) (if skewed) | Always O(log n) (self-balancing)     |
| Use case       | In-memory data               | Disk-based storage (databases, FS)   |
| Cache-friendly | Yes (small nodes)            | Yes (node size = disk block/page)    |

### Q10: What real-world systems use B-Trees?

- **Database indexes** (MySQL, PostgreSQL, SQLite)
- **Filesystems** (NTFS, HFS+, ext4)
- **Key-value stores** (MongoDB, many NoSQL systems)
- **Filesystem directories** (inode indexing)
- **Search engines** (inverted index storage)

### Q11: Could these experiments be improved?

Yes — we could use **binary search** (`bisect` module) instead of linear scan to make finding the position O(log n). We could also demonstrate **node splitting** by setting a maximum capacity and splitting when full, which is the core B-Tree balancing operation.

---

*Prepared for DAA Lab Viva — Experiments 1 (Search) & 2 (Insertion)*
