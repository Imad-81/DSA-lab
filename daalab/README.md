# DAA Lab Experiments & Algorithms

This directory (`daalab`) contains Python implementations for Advanced Data Structures and Algorithms covered in Design and Analysis of Algorithms (DAA) Lab.

---

## Directory Overview

| Experiment File | Description | Core Operations |
|---|---|---|
| [`exp1.py`](file:///Users/imadmac/school/code/Uni_Labs/daalab/exp1.py) | **B-Tree Operations & Full Implementation** | Node Search, Node Insertion, Node Deletion, Tree Splitting & Insertion |
| [`exp2.py`](file:///Users/imadmac/school/code/Uni_Labs/daalab/exp2.py) | **Binomial Heap Implementation** | Insertion, Get Min, Extract Min, Union / Tree Merging, Display |
| [`exp3.py`](file:///Users/imadmac/school/code/Uni_Labs/daalab/exp3.py) | **Fibonacci Heap Implementation** | Insertion, Find Min, Extract Min (Consolidate), Decrease Key, Cascading Cut |

---

## Experiment Details

### Experiment 1: B-Tree Operations & Full Implementation (`exp1.py`)

#### Parts Included
1. **Part 1: B-Tree Node Search** — Linear key search within a sorted array representation of a B-Tree node ($O(n)$).
2. **Part 2: B-Tree Node Insertion** — Inserting a new key into a single sorted B-Tree node while preserving sorted order ($O(n)$).
3. **Part 3: B-Tree Node Deletion** — Searching and deleting a key from a sorted node list via `pop()` ($O(n)$).
4. **Part 4: Full B-Tree Implementation** — Complete dynamic B-Tree class (`BTree`, `BTreeNode`) supporting insertion, node splitting, and hierarchical level-order tree traversal ($O(\log n)$ search/insertion).

---

### Experiment 2: Binomial Heap (`exp2.py`)

#### Overview
A **Binomial Heap** is a collection of Binomial Trees satisfying the min-heap property, where each degree occurs at most once. It provides efficient heap union operations ($O(\log n)$).

#### Key Components
- **`BinomialNode`**: Stores `key`, `degree`, `parent`, `child` (leftmost child), and `sibling` (next sibling).
- **`BinomialHeap`**: Main heap class managing root lists and operations.

#### Core Operations & Time Complexities
- **Merge Trees (`merge_trees`)**: Links two binomial trees of degree $k$ to form a tree of degree $k+1$ in $O(1)$ time.
- **Union (`union`)**: Merges two binomial heap root lists and combines trees of equal degrees in $O(\log n)$ time.
- **Insert (`insert`)**: Creates a single-node heap and calls `union()` in $O(\log n)$ time (amortized $O(1)$).
- **Find Minimum (`get_min`)**: Traverses the root list in $O(\log n)$ time.
- **Extract Minimum (`extract_min`)**: Removes the root with the minimum key, reverses its child list, and performs a `union()` in $O(\log n)$ time.

---

### Experiment 3: Fibonacci Heap (`exp3.py`)

#### Overview
A **Fibonacci Heap** is a data structure for priority queue operations consisting of a collection of heap-ordered trees. It offers faster amortized running times than Binary or Binomial heaps, especially for `decrease_key`.

#### Key Components
- **`FibonacciNode`**: Stores `key`, `degree`, `mark` (boolean for cascading cut), `parent`, `child`, `left`, and `right` (circular doubly linked list pointers).
- **`FibonacciHeap`**: Heap structure maintaining `min_node` pointer and `total_nodes` count.

#### Core Operations & Time Complexities
- **Insert (`insert`)**: Adds a new node to the root circular list in $O(1)$ amortized time.
- **Find Minimum (`find_min`)**: Returns `min_node.key` in $O(1)$ time.
- **Extract Minimum (`extract_min`)**: Removes `min_node`, adds its children to the root list, and calls `consolidate()` to combine roots of equal degrees in $O(\log n)$ amortized time.
- **Consolidate (`consolidate`)**: Groups root nodes by degree using a degree table.
- **Decrease Key (`decrease_key`)**: Decreases a node's key value. Performs `cut()` and `cascading_cut()` if heap order is violated, bringing amortized time complexity to $O(1)$.

---

## Summary of Time & Space Complexities

| Data Structure | Search / Get Min | Insert | Extract Min | Decrease Key | Union / Merge | Space |
|---|---|---|---|---|---|---|
| **B-Tree** | $O(\log n)$ | $O(\log n)$ | $O(\log n)$ | N/A | N/A | $O(n)$ |
| **Binomial Heap** | $O(\log n)$ | $O(\log n)$ / $O(1)$ amortized | $O(\log n)$ | $O(\log n)$ | $O(\log n)$ | $O(n)$ |
| **Fibonacci Heap** | $O(1)$ | $O(1)$ amortized | $O(\log n)$ amortized | $O(1)$ amortized | $O(1)$ | $O(n)$ |

---

## Viva Questions & Answers

### Q1: What is a B-Tree and why is it used?
A **B-Tree** is a self-balancing search tree where nodes can contain multiple keys and more than two children. It is primarily used in **databases and file systems** to minimize disk I/O operations because each node fits into a single block/page.

### Q2: What is the main structural difference between Binomial Heap and Fibonacci Heap?
- **Binomial Heap**: A strictly structured collection of binomial trees where roots are kept sorted by degree, and degree conflicts are resolved immediately during union/insertion operations.
- **Fibonacci Heap**: A lazy data structure using circular doubly linked lists for roots and children. It defers tree consolidation until `extract_min()`, enabling $O(1)$ amortized insertion and `decrease_key`.

### Q3: Why is `decrease_key` faster in Fibonacci Heap compared to Binomial Heap?
In a Binomial Heap, decreasing a key requires bubble-up traversal along parent pointers, taking $O(\log n)$ time. In a Fibonacci Heap, if decreasing a key breaks the min-heap order, the node is simply **cut** from its parent and moved to the root list in $O(1)$ time. **Cascading cuts** ensure trees do not become overly unbalanced.

### Q4: How does tree consolidation work during `extract_min` in Fibonacci Heap?
After removing the minimum node, all its children are merged into the root list. Then, `consolidate()` uses a degree lookup table to continuously link any two root trees that share the exact same degree until every root in the heap has a unique degree.

---

*Prepared for DAA Lab Experiments 1 (B-Tree), 2 (Binomial Heap), and 3 (Fibonacci Heap)*