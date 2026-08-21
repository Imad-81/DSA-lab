# DAA Lab — Advanced Data Structures & Algorithms

Comprehensive Python implementations, algorithmic explanations, step-by-step operation breakdowns, complexity analysis, and viva questions for the Design and Analysis of Algorithms (DAA) Laboratory repository (`daalab`).

---

## Table of Contents

- [Directory Structure & Quick Reference](#directory-structure--quick-reference)
- [Experiment 1: B-Tree Operations & Implementation](#experiment-1-b-tree-operations--implementation)
- [Experiment 2: Binomial Heap Implementation](#experiment-2-binomial-heap-implementation)
- [Experiment 3: Fibonacci Heap Implementation](#experiment-3-fibonacci-heap-implementation)
- [Experiment 4: Red-Black Tree Implementation](#experiment-4-red-black-tree-implementation)
- [Experiment 5: Greedy Algorithms](#experiment-5-greedy-algorithms)
- [Comprehensive Time & Space Complexity Matrix](#comprehensive-time--space-complexity-matrix)
- [Viva Questions & Answers](#viva-questions--answers)

---

## Directory Structure & Quick Reference

| File | Structure / Topic | Primary Operations Covered | Time Complexity (Primary) |
|---|---|---|---|
| [`exp1.py`](file:///Users/imadmac/school/code/Uni_Labs/daalab/exp1.py) | **B-Tree** | Linear Search, Node Insert, Node Delete, Splitting & Insertion | $O(\log_t n)$ search / insert |
| [`exp2.py`](file:///Users/imadmac/school/code/Uni_Labs/daalab/exp2.py) | **Binomial Heap** | `insert`, `get_min`, `extract_min`, `union`, `merge_trees` | $O(\log n)$ insert / extract-min |
| [`exp3.py`](file:///Users/imadmac/school/code/Uni_Labs/daalab/exp3.py) | **Fibonacci Heap** | `insert`, `find_min`, `extract_min`, `consolidate`, `decrease_key`, `cut` | $O(1)$ amortized insert & decrease-key |
| [`exp4.py`](file:///Users/imadmac/school/code/Uni_Labs/daalab/exp4.py) | **Red-Black Tree** | `insert`, `fix_insert`, `left_rotate`, `right_rotate`, `search`, `inorder` | $O(\log n)$ search / insert |
| [`exp5.py`](file:///Users/imadmac/school/code/Uni_Labs/daalab/exp5.py) | **Greedy Algorithms** | Fractional Knapsack, Activity Selection, Huffman Coding | $O(n \log n)$ sorting / heap building |

---

## Experiment 1: B-Tree Operations & Implementation

**Source File:** [`exp1.py`](file:///Users/imadmac/school/code/Uni_Labs/daalab/exp1.py)

### Overview
A **B-Tree** is a self-balancing search tree designed to work efficiently on secondary storage (disks). Unlike binary search trees, B-Tree nodes can store multiple keys and have more than two child pointers.

### Parts Breakdown

#### Part 1: B-Tree Node Search (`b_tree_node = [10, 20, 30, 40, 50]`)
- Performs a linear lookup of a key within a simulated single node.
- Complexity: $O(n)$ where $n$ is the number of keys in the node.

#### Part 2: B-Tree Node Insertion
- Finds the first position where `key < node[i]` and inserts the key using `list.insert(i, key)`, maintaining sorted order.
- If key is greater than all existing elements, it appends to the end.

#### Part 3: B-Tree Node Deletion
- Locates the key within the array and removes it using `list.pop(i)`, shifting trailing keys to keep the node compact and sorted.

#### Part 4: Full B-Tree Class Implementation (`BTree`, `BTreeNode`)
- **Node Structure (`BTreeNode`)**: `key` array, `child` array of node references, `leaf` boolean flag.
- **Minimum Degree ($t$)**: Every non-root node must contain at least $t-1$ keys and at most $2t-1$ keys.
- **Child Splitting (`split_child`)**: When a child node overflows ($2t-1$ keys), it is split around its median key (index $t-1$), promoting the median to the parent.
- **Recursive Non-Full Insertion (`insert_non_full`)**: Descends the tree, preemptively splitting full nodes along the path to ensure insertion always succeeds at the leaf level.

```
Example B-Tree Structure (t=3):
               [3]
             /     \
      [0, 1]         [4, 5]   [7, 8]
```

---

## Experiment 2: Binomial Heap Implementation

**Source File:** [`exp2.py`](file:///Users/imadmac/school/code/Uni_Labs/daalab/exp2.py)

### Overview
A **Binomial Heap** is a collection of **Binomial Trees** $B_0, B_1, B_2, \dots, B_k$ satisfying:
1. Every binomial tree in the heap obeys the **min-heap property**.
2. There is at most **one** binomial tree of any given degree.

### Key Operations & Algorithms

1. **Tree Link / Merge (`merge_trees(tree1, tree2)`)**:
   - Given two trees of degree $k$, the tree with the smaller root becomes the parent of the other tree, forming a tree of degree $k+1$ in $O(1)$ time.
2. **Heap Union (`union(other_head)`)**:
   - Merges root lists sorted by degree (`merge_heap`), then iterates through to combine trees of duplicate degree.
3. **Insertion (`insert(key)`)**:
   - Constructs a single-node binomial heap $B_0$ and unions it with the current heap in $O(\log n)$ time.
4. **Extract Minimum (`extract_min()`)**:
   - Finds the minimum root node, removes it from the root list, reverses its children to form a valid root list, and performs `union()` with the remaining heap.

```
Binomial Tree Degrees:
B0: (1 node)    B1: (2 nodes)     B2: (4 nodes)
   o               o                 o
                  /                 / \
                 o                 o   o
                                  /
                                 o
```

---

## Experiment 3: Fibonacci Heap Implementation

**Source File:** [`exp3.py`](file:///Users/imadmac/school/code/Uni_Labs/daalab/exp3.py)

### Overview
A **Fibonacci Heap** is a loose collection of heap-ordered trees using circular doubly linked lists. It defers structural consolidation until `extract_min()`, providing $O(1)$ amortized running time for `insert`, `find_min`, and `decrease_key`.

### Key Mechanics

1. **Circular Doubly Linked Lists**:
   - Node attributes `left` and `right` allow constant-time $O(1)$ splicing of nodes into and out of root/child lists.
2. **Lazy Insertion**:
   - New keys are simply attached to the root circular list; no tree restructuring occurs immediately.
3. **Consolidation (`consolidate()`)**:
   - Executed during `extract_min()`. Uses an array/hash table keyed by tree degree to link trees of equal degrees until all root trees have distinct degrees.
4. **Cut & Cascading Cut (`cut`, `cascading_cut`)**:
   - **`cut`**: Detaches a modified node from its parent (when its key decreases below parent's key) and moves it to the root list.
   - **`cascading_cut`**: If a parent has already lost a child (`mark == True`), it is also cut and moved to the root list, propagating recursively upwards. This maintains bounding properties necessary for logarithmic height.

---

## Experiment 4: Red-Black Tree Implementation

**Source File:** [`exp4.py`](file:///Users/imadmac/school/code/Uni_Labs/daalab/exp4.py)

### Overview
A **Red-Black Tree** is a self-balancing binary search tree where every node contains an extra color bit (`RED` or `BLACK`). It guarantees that no path from root to leaf is more than twice as long as any other path.

### 5 Invariant Rules
1. Every node is either **RED** or **BLACK**.
2. The root is always **BLACK**.
3. Every leaf (`NIL`) is **BLACK**.
4. If a node is **RED**, both its children must be **BLACK** (no two adjacent RED nodes).
5. For each node, all simple paths from the node to descendant leaves contain the same number of **BLACK** nodes (Black-Height).

### Insertion Fixup Cases (`fix_insert`)

When inserting a node (always colored `RED` initially), potential red-red violations are resolved based on the uncle's color:

- **Case 1 (Uncle is RED)**:
  - Recolor parent and uncle to `BLACK`, grandparent to `RED`. Move pointer $k$ to grandparent.
- **Case 2 (Uncle is BLACK, $k$ is inner child - Zig-Zag)**:
  - Apply `left_rotate` (or `right_rotate`) on parent to transform into Case 3.
- **Case 3 (Uncle is BLACK, $k$ is outer child - Zig-Zig)**:
  - Recolor parent to `BLACK`, grandparent to `RED`, then perform rotation (`right_rotate` / `left_rotate`) on grandparent.

---

## Experiment 5: Greedy Algorithms

**Source File:** [`exp5.py`](file:///Users/imadmac/school/code/Uni_Labs/daalab/exp5.py)

### Overview
Greedy algorithms construct solutions piece by piece, always choosing the next piece that offers the most immediate (locally optimal) benefit, aiming to find a global optimum.

---

### 5(a) — Part 1: Fractional Knapsack Problem

- **Strategy**: Calculate the **profit-to-weight ratio** ($P_i / W_i$) for each item and sort items in descending order of ratio.
- **Greedy Choice**: Take as much of the item with the highest value density as possible. If the remaining capacity cannot take the whole item, take the fractional portion.
- **Time Complexity**: $O(n \log n)$ due to sorting $n$ items.

```
Given: Capacity W = 50, Items: (w, p) = [(10, 60), (20, 100), (30, 120)]
Ratios: [6.0, 5.0, 4.0]
Selection: Item 1 (full: 10w, 60p) + Item 2 (full: 20w, 100p) + Item 3 (20/30 frac: 20w, 80p)
Total Profit = 240.0
```

---

### 5(a) — Part 2: Activity Selection Problem

- **Strategy**: Given start times $S$ and finish times $F$ for $n$ activities, select the maximum number of mutually compatible activities.
- **Greedy Choice**: Sort activities by **finish time** in ascending order. Always pick the activity with the earliest finish time that starts after or when the previous activity ends.
- **Time Complexity**: $O(n \log n)$ for sorting finish times ($O(n)$ if already sorted).

```
Activities (Finish, Start): [(2, 1), (4, 3), (6, 0), (7, 5), (9, 8), (9, 5)]
Selected: Activity 1 [1-2], Activity 2 [3-4], Activity 4 [5-7], Activity 5 [8-9]
Maximum Activities = 4
```

---

### 5(b) — Huffman Coding & Complexity Analysis

- **Strategy**: A lossless data compression algorithm that assigns variable-length prefix codes to characters based on their frequencies.
- **Greedy Choice**: Use a **Min-Heap (Priority Queue)**. Repeatedly extract the two nodes with the lowest frequencies, combine them into an internal parent node with frequency sum, and insert the parent back into the heap.
- **Prefix Property**: No code is a prefix of another code, ensuring unambiguous decoding.

#### Time & Space Complexity Analysis:
- **Building the Min-Heap**: $O(n)$
- **Extracting minimums & inserting ($n-1$ iterations)**: Each step takes $O(\log n)$, so tree construction takes $O(n \log n)$.
- **Generating Codes (Tree Traversal)**: $O(n)$
- **Overall Time Complexity**: $O(n \log n)$
- **Auxiliary Space Complexity**: $O(n)$ to store tree nodes and heap.

---

## Comprehensive Time & Space Complexity Matrix

| Structure / Algorithm | Search / Find Min | Insert (Worst Case) | Insert (Amortized) | Extract Min / Delete | Overall Time Complexity | Space Complexity |
|---|---|---|---|---|---|---|
| **B-Tree ($t$)** | $O(\log n)$ | $O(\log n)$ | $O(\log n)$ | $O(\log n)$ | $O(\log n)$ | $O(n)$ |
| **Binomial Heap** | $O(\log n)$ | $O(\log n)$ | $O(1)$ | $O(\log n)$ | $O(\log n)$ | $O(n)$ |
| **Fibonacci Heap** | $O(1)$ | $O(1)$ | $O(1)$ | $O(\log n)$ amortized | $O(1)$ amortized | $O(n)$ |
| **Red-Black Tree** | $O(\log n)$ | $O(\log n)$ | $O(\log n)$ | $O(\log n)$ | $O(\log n)$ | $O(n)$ |
| **Fractional Knapsack** | N/A | N/A | N/A | N/A | $O(n \log n)$ | $O(n)$ |
| **Activity Selection** | N/A | N/A | N/A | N/A | $O(n \log n)$ | $O(n)$ |
| **Huffman Coding** | N/A | $O(\log n)$ | $O(\log n)$ | $O(\log n)$ | $O(n \log n)$ | $O(n)$ |

---

## Viva Questions & Answers

### Q1: Why does Greedy work for Fractional Knapsack but fail for 0/1 Knapsack?
Fractional Knapsack allows breaking items; taking the item with the highest profit density ($P/W$) leaves the remaining capacity optimal. In 0/1 Knapsack, taking a high-density item might leave empty space that cannot be filled, so Dynamic Programming is required.

### Q2: Why must activities be sorted by finish time rather than start time or duration?
Sorting by earliest finish time leaves the maximum possible remaining time for subsequent activities. Sorting by start time or duration can block longer optimal activity schedules.

### Q3: What is the Prefix Rule in Huffman Coding and why is it crucial?
The prefix rule states that no character's codeword can be a prefix of another character's codeword. This enables unambiguous left-to-right decoding without separators/delimiters.

### Q4: What is the time complexity of Huffman Coding if characters are already sorted by frequency?
If frequencies are pre-sorted, we can maintain two standard queues (one for initial leaf nodes and one for combined internal nodes), allowing tree construction in linear $O(n)$ time.

### Q5: What makes B-Trees ideal for File Systems and Database Systems?
B-Trees have large branching factors (high degree $t$). This keeps the height of the tree small, minimizing the number of disk accesses required to find a record. Entire B-Tree nodes can be aligned with disk block sizes.

### Q6: Why are new nodes in a Red-Black Tree always inserted as RED?
Inserting a RED node preserves Rule 5 (Black-Height invariant) across all paths. Inserting a BLACK node would immediately violate black-height on that branch and require complex global updates.

### Q7: What is the purpose of the `mark` field in Fibonacci Heap nodes?
The `mark` boolean indicates whether a node has lost a child since it became a child of its current parent. It triggers a **cascading cut** when a second child is lost, preventing trees from becoming excessively deep and preserving $O(1)$ amortized efficiency.

---

*Prepared for DAA Laboratory — Unit Experiments 1–5*