# DSA Lab — All Experiments

## Table of Contents

- [Experiment 1: Built-in Data Structures (E-Commerce Analysis)](#experiment-1-built-in-data-structures-e-commerce-analysis)
- [Experiment 2: Linked List (Student GPA Management)](#experiment-2-linked-list-student-gpa-management)
- [Experiment 3: Stack & Postfix Evaluation](#experiment-3-stack--postfix-evaluation)
- [Experiment 4a: Product Sorting System](#experiment-4a-product-sorting-system)
- [Experiment 4b: Priority Queue Ticketing System](#experiment-4b-priority-queue-ticketing-system)
- [Experiment 5: Merge Sort (E-Commerce Sorting)](#experiment-5-merge-sort-e-commerce-sorting)
- [Experiment 6a: Linear & Binary Search](#experiment-6a-linear--binary-search)
- [Experiment 6b: AVL Tree Implementation](#experiment-6b-avl-tree-implementation)
- [Experiment 7: Hash Table with Chaining & Rehashing](#experiment-7-hash-table-with-chaining--rehashing)
- [Experiment 8: Simple Hash Table Implementation](#experiment-8-simple-hash-table-implementation)
- [Experiment 9: Dijkstra's Shortest Path Algorithm](#experiment-9-dijkstras-shortest-path-algorithm)
- [Experiment 10: Sudoku Solver using Backtracking](#experiment-10-sudoku-solver-using-backtracking)
- [Common Viva Questions](#common-viva-questions)

---

## Experiment 1: Built-in Data Structures (E-Commerce Analysis)

### Code

```python
products = [
    (101, "Mobile", "Electronics", 20000),
    (102, "Laptop", "Electronics", 55000),
    (103, "Shoes", "Fashion", 3000),
    (104, "Watch", "Fashion", 2500),
    (105, "Headphones", "Electronics", 1500)
]
purchases = [
    ("User1", 101, 1), ("User2", 103, 2),
    ("User1", 102, 1), ("User3", 101, 1), ("User2", 105, 3)
]
searches = ["Mobile", "Shoes", "Mobile", "Laptop", "Mobile", "Watch"]

names = [p[1] for p in products]
costliest = max(products, key=lambda x: x[3])
cat_counts = {c: [p[2] for p in products].count(c) for c in {p[2] for p in products}}

user_items = {}
for u, _, q in purchases:
    user_items[u] = user_items.get(u, 0) + q
top_user = max(user_items, key=user_items.get)
prod_sales = {p[0]: sum(q for u, pid, q in purchases if pid == p[0]) for p in products}

revenues = {p[1]: prod_sales[p[0]] * p[3] for p in products}
total_revenue = sum(revenues.values())

search_counts = {s: searches.count(s) for s in set(searches)}
most_searched = max(search_counts, key=search_counts.get)
```

### Concepts Covered

| Concept | Usage |
|---|---|
| **List** | `products`, `purchases`, `searches` — ordered, mutable collection |
| **Tuple** | Each product is a tuple `(id, name, category, price)` — immutable, fixed structure |
| **Dictionary** | `user_items`, `revenues`, `cat_counts` — key-value mapping for lookups |
| **`max()` with `key`** | Finding costliest product and top user |
| **List comprehension** | `[p[1] for p in products]` — concise data extraction |
| **`dict.get()`** | Safely increment counters: `user_items.get(u, 0) + q` |
| **`set` for unique values** | `{p[2] for p in products}` gets unique categories |

### Viva Q&A

**Q: Why use a tuple for products instead of a list?**
Tuples are immutable — product structure shouldn't change. They also use less memory and can be used as dictionary keys.

**Q: How does `max(products, key=lambda x: x[3])` work?**
`max()` iterates over the list. For each element, it calls the lambda function which extracts index 3 (price). It returns the element with the maximum price value.

**Q: What is the time complexity of the operations here?**
- List iteration: O(n)
- `max()` over n elements: O(n)
- Dict lookup/insertion: O(1) average
- List `count()`: O(n)

---

## Experiment 2: Linked List (Student GPA Management)

### Code

```python
class Node:
    def __init__(self, name, roll_number, marks):
        self.name = name
        self.roll_number = roll_number
        self.marks = marks
        self.next = None

class LinkedList:
    def __init__(self):
        self.head = None

    def add_student(self, name, roll_number, marks):
        new_student = Node(name, roll_number, marks)
        new_student.next = self.head
        self.head = new_student

    def display_students(self):
        current = self.head
        while current:
            print(f"Name: {current.name}, Roll Number: {current.roll_number}, Marks: {current.marks}")
            current = current.next

    def calculate_gpa(self):
        total_marks = 0
        total_students = 0
        current = self.head
        while current:
            total_marks += current.marks
            total_students += 1
            current = current.next
        average = total_marks / total_students
        if average >= 90: return "A"
        elif average >= 80: return "B"
        elif average >= 70: return "C"
        elif average >= 60: return "D"
        else: return "F"
```

### Concepts Covered

| Concept | Explanation |
|---|---|
| **Singly Linked List** | Each `Node` has data + a `next` pointer; traversal is one-directional |
| **Head pointer** | Entry point of list; `None` means empty list |
| **Insert at head** | O(1) — new node points to current head, head updates to new node |
| **Traversal** | O(n) — follow `next` until `None` |
| **GPA grading** | Threshold-based letter grade from average marks |

### Viva Q&A

**Q: What is a linked list vs an array?**
Linked lists are dynamic, have O(1) insertion/deletion at head, but O(n) random access. Arrays have O(1) index access but O(n) insertion/deletion.

**Q: Why does `add_student` insert at the head?**
It's O(1) — no traversal needed. Inserting at tail would require O(n) traversal or maintaining a tail pointer.

**Q: What if the list is empty?**
`head` is `None`. The while loop condition `while current:` won't execute, so `total_students` stays 0. The code returns 0 due to the check `if total_students == 0: return 0`.

**Q: Can you reverse a linked list?**
Yes — iteratively: `prev, curr = None, head`; for each node: store `next`, point `curr.next` to `prev`, move `prev` and `curr` forward.

---

## Experiment 3: Stack & Postfix Evaluation

### Code

```python
class Stack:
    def __init__(self):
        self.items = []

    def push(self, item):
        self.items.append(item)

    def pop(self):
        if not self.is_empty():
            return self.items.pop()
        return None

    def is_empty(self):
        return len(self.items) == 0

    @staticmethod
    def evaluate_expression(expression):
        stack = Stack()
        operators = {'+', '-', '*', '/'}
        for char in expression:
            if char.isdigit():
                stack.push(int(char))
            elif char in operators:
                op2 = stack.pop()
                op1 = stack.pop()
                if char == '+': stack.push(op1 + op2)
                elif char == '-': stack.push(op1 - op2)
                elif char == '*': stack.push(op1 * op2)
                elif char == '/': stack.push(op1 / op2)
        return stack.pop()
```

### Concepts Covered

| Concept | Explanation |
|---|---|
| **Stack (LIFO)** | Last-In-First-Out — `push` adds to top, `pop` removes from top |
| **Postfix notation** | Operators come after operands (e.g., `23*5+` = `(2*3)+5 = 11`) |
| **Evaluation** | Operands pushed; operator pops 2, computes, pushes result |
| **No parentheses needed** | Postfix encodes operator precedence implicitly |

### Viva Q&A

**Q: Why use a stack for postfix evaluation?**
Postfix evaluation inherently requires LIFO behavior — operands must be recalled in reverse order of when they were seen.

**Q: How does `23*5+` evaluate to 11?**
1. Push 2, push 3 → stack: [2, 3]
2. `*` → pop 3, pop 2 → 2\*3=6 → push 6 → [6]
3. Push 5 → [6, 5]
4. `+` → pop 5, pop 6 → 6+5=11 → push 11
5. Result: 11

**Q: What is the difference between stack and queue?**
Stack: LIFO (Last-In-First-Out). Queue: FIFO (First-In-First-Out).

**Q: What are real-world uses of stacks?**
Function call stack, undo/redo in editors, expression evaluation, backtracking algorithms, DFS.

---

## Experiment 4a: Product Sorting System

### Code

```python
class Product:
    def __init__(self, name, price, popularity):
        self.name = name
        self.price = price
        self.popularity = popularity

    def __repr__(self):
        return f"{self.name} - Price: {self.price}, Popularity: {self.popularity}"

def sort_products(products, criteria):
    if criteria == "price":
        return sorted(products, key=lambda x: x.price)
    elif criteria == "popularity":
        return sorted(products, key=lambda x: x.popularity)
    elif criteria == "alphabetical":
        return sorted(products, key=lambda x: x.name)
    else:
        raise ValueError("Invalid sorting criteria")
```

### Concepts Covered

| Concept | Explanation |
|---|---|
| **`sorted()` with `key`** | Python's Timsort — stable, O(n log n) |
| **Lambda functions** | `lambda x: x.price` — anonymous, single-expression function |
| **Sorting by attribute** | Dynamic comparison using object attribute access |
| **Timsort** | Hybrid sorting algorithm (merge + insertion sort) — Python's default |

---

## Experiment 4b: Priority Queue Ticketing System

### Code

```python
import heapq
import time

class Ticket:
    _id_counter = 1
    def __init__(self, customer_name, issue, priority=2):
        self.id = Ticket._id_counter
        Ticket._id_counter += 1
        self.customer_name = customer_name
        self.issue = issue
        self.priority = priority
        self.timestamp = time.time()

    def __lt__(self, other):
        if self.priority == other.priority:
            return self.timestamp < other.timestamp
        return self.priority < other.priority

class TicketingSystem:
    def __init__(self):
        self.queue = []

    def submit_ticket(self, name, issue, priority):
        ticket = Ticket(name, issue, priority)
        heapq.heappush(self.queue, ticket)

    def process_ticket(self):
        ticket = heapq.heappop(self.queue)
        print(f"Processing: {ticket}")
```

### Concepts Covered

| Concept | Explanation |
|---|---|
| **Priority Queue** | Elements dequeued by priority, not insertion order |
| **Min-Heap (`heapq`)** | Parent ≤ children; `heappop` always returns smallest element |
| **`__lt__` method** | Defines how objects compare for heap ordering |
| **FCFS tie-breaking** | Same priority → handled by `timestamp` (earlier first) |
| **Min-heap property** | `heapq` is a binary heap; push/pop both O(log n) |

### Viva Q&A

**Q: How does `heapq` work internally?**
It maintains a binary heap where each parent is ≤ its children. The smallest element is always at index 0.

**Q: Why define `__lt__`?**
`heapq` uses `<` comparisons between elements. Custom `__lt__` tells heapq how to order `Ticket` objects — by priority first, then by timestamp.

**Q: What is the time complexity of `heappush` and `heappop`?**
Both O(log n) — the heap is restructured after each operation.

**Q: Priority Queue vs regular Queue?**
Regular Queue: FIFO. Priority Queue: highest priority item is extracted first regardless of order.

---

## Experiment 5: Merge Sort (E-Commerce Sorting)

### Code

```python
class Product:
    def __init__(self, name, price, popularity):
        self.name = name
        self.price = price
        self.popularity = popularity

def merge_sort(product_list, attribute):
    if len(product_list) <= 1:
        return product_list
    mid = len(product_list) // 2
    left = merge_sort(product_list[:mid], attribute)
    right = merge_sort(product_list[mid:], attribute)
    return merge(left, right, attribute)

def merge(left, right, attribute):
    result = []
    i = j = 0
    while i < len(left) and j < len(right):
        if getattr(left[i], attribute) <= getattr(right[j], attribute):
            result.append(left[i])
            i += 1
        else:
            result.append(right[j])
            j += 1
    result.extend(left[i:])
    result.extend(right[j:])
    return result
```

### Concepts Covered

| Concept | Explanation |
|---|---|
| **Merge Sort** | Divide-and-conquer: split → sort recursively → merge sorted halves |
| **Divide & Conquer** | Break into subproblems, solve each, combine results |
| **`getattr()`** | Dynamic attribute access: `getattr(obj, "price")` = `obj.price` |
| **Time Complexity** | O(n log n) — always (best, average, worst) |
| **Space Complexity** | O(n) — requires auxiliary arrays for merging |

### Viva Q&A

**Q: Why is Merge Sort O(n log n)?**
The array is split log n times (halving), and at each level we merge O(n) elements total. So n elements × log n levels = O(n log n).

**Q: How is Merge Sort different from Quick Sort?**
Merge Sort: O(n log n) always, stable, O(n) space. Quick Sort: O(n log n) average, O(n²) worst, in-place O(log n) space, not stable.

**Q: What is the base case in recursion?**
When `len(product_list) <= 1` — a single-element list is already sorted.

**Q: Why use `getattr` instead of direct access?**
It makes the sort generic — you can sort by any attribute without changing the function.

---

## Experiment 6a: Linear & Binary Search

### Code

```python
class Product:
    def __init__(self, name, price):
        self.name = name
        self.price = price

def linear_search(products, target_name):
    for index, product in enumerate(products):
        if product.name.lower() == target_name.lower():
            return index
    return -1

def binary_search(products, target_name):
    sorted_products = sorted(products, key=lambda x: x.name.lower())
    low, high = 0, len(sorted_products) - 1
    target_name = target_name.lower()
    while low <= high:
        mid = (low + high) // 2
        mid_name = sorted_products[mid].name.lower()
        if mid_name == target_name:
            return mid, sorted_products
        elif mid_name < target_name:
            low = mid + 1
        else:
            high = mid - 1
    return -1, sorted_products
```

### Concepts Covered

| Concept | Explanation |
|---|---|
| **Linear Search** | Scan each element sequentially — O(n) |
| **Binary Search** | Repeatedly halve the search space — O(log n) |
| **Prerequisite for Binary Search** | Data must be **sorted** |
| **Case-insensitive search** | `.lower()` normalizes both target and data |

### Viva Q&A

**Q: When should you use Linear Search vs Binary Search?**
Linear Search: unsorted data, small datasets, single search. Binary Search: sorted data, large datasets, many searches (sorting once pays off).

**Q: Why does Binary Search require a sorted array?**
The algorithm relies on comparing the target with the middle element to decide which half to eliminate. This only works if elements are ordered.

**Q: What is the worst-case for Linear Search?**
Element at last position or not present — O(n).

**Q: What is the recurrence relation for Binary Search?**
T(n) = T(n/2) + O(1). Solves to O(log n) via Master Theorem.

---

## Experiment 6b: AVL Tree Implementation

### Code

```python
class TreeNode:
    def __init__(self, key, value):
        self.key = key
        self.value = value
        self.left = None
        self.right = None
        self.height = 1

class AVLTree:
    def __init__(self):
        self.root = None

    def _get_h(self, n): return n.height if n else 0
    def _get_b(self, n): return self._get_h(n.left) - self._get_h(n.right) if n else 0

    def _rotate(self, y, left=True):
        x = y.right if left else y.left
        T2 = x.left if left else x.right
        if left: x.left, y.right = y, T2
        else: x.right, y.left = y, T2
        y.height = 1 + max(self._get_h(y.left), self._get_h(y.right))
        x.height = 1 + max(self._get_h(x.left), self._get_h(x.right))
        return x

    def insert(self, key, value, node=None, first_call=True):
        if first_call: self.root = self.insert(key, value, self.root, False); return
        if not node: return TreeNode(key, value)
        if key < node.key: node.left = self.insert(key, value, node.left, False)
        elif key > node.key: node.right = self.insert(key, value, node.right, False)
        else: return node
        node.height = 1 + max(self._get_h(node.left), self._get_h(node.right))
        b = self._get_b(node)
        if b > 1:
            if key > node.left.key: node.left = self._rotate(node.left, True)
            return self._rotate(node, False)
        if b < -1:
            if key < node.right.key: node.right = self._rotate(node.right, False)
            return self._rotate(node, True)
        return node

    def search(self, key, node=None, first_call=True):
        curr = self.root if first_call else node
        if not curr or curr.key == key: return curr
        return self.search(key, curr.left if key < curr.key else curr.right, False)
```

### Concepts Covered

| Concept | Explanation |
|---|---|
| **AVL Tree** | Self-balancing BST where height difference (balance factor) between subtrees is ≤ 1 |
| **Balance Factor** | `height(left) - height(right)` — must be -1, 0, or +1 |
| **Rotations** | LL (Right rotate), RR (Left rotate), LR (Left-Right), RL (Right-Left) |
| **Height property** | Every node stores its subtree height for O(1) balance factor |
| **Recurrence** | T(n) = 2T(n/2) + O(1) → height = O(log n) |

### Viva Q&A

**Q: What are the four rotation cases in an AVL Tree?**
1. **LL** (Left-Left): Insert into left subtree of left child → Right rotate
2. **RR** (Right-Right): Insert into right subtree of right child → Left rotate
3. **LR** (Left-Right): Insert into right subtree of left child → Left rotate on child, then Right rotate
4. **RL** (Right-Left): Insert into left subtree of right child → Right rotate on child, then Left rotate

**Q: What is the maximum height of an AVL Tree?**
Approximately 1.44 × log₂(n) — much better than BST's worst-case O(n).

**Q: Why use AVL over a regular BST?**
BST can degenerate to O(n) height (e.g., inserting sorted data). AVL guarantees O(log n) height through rotations.

**Q: AVL vs Red-Black Tree?**
AVL is more strictly balanced (tighter height bound), giving faster lookups. Red-Black trees have fewer rotations during insertion/deletion, making them faster for write-heavy workloads.

---

## Experiment 7: Hash Table with Chaining & Rehashing

### Code

```python
class Product:
    def __init__(self, name, price):
        self.name = name
        self.price = price

class HashTable:
    def __init__(self, size=5, threshold=0.7):
        self.size = size
        self.threshold = threshold
        self.count = 0
        self.table = [[] for _ in range(self.size)]

    def _hash_function(self, key):
        return sum(ord(char) for char in key) % self.size

    def get_load_factor(self):
        return self.count / self.size

    def insert(self, product):
        if self.get_load_factor() >= self.threshold:
            self._rehash()
        index = self._hash_function(product.name)
        for item in self.table[index]:
            if item.name == product.name:
                item.price = product.price
                return
        self.table[index].append(product)
        self.count += 1

    def _rehash(self):
        old_table = self.table
        self.size *= 2
        self.table = [[] for _ in range(self.size)]
        self.count = 0
        for bucket in old_table:
            for product in bucket:
                self.insert(product)

    def search(self, name):
        index = self._hash_function(name)
        for product in self.table[index]:
            if product.name == name:
                return product
        return None
```

### Concepts Covered

| Concept | Explanation |
|---|---|
| **Hash Function** | Maps key to index: `sum(ASCII) % size` |
| **Chaining** | Each bucket is a list; collisions handled by appending |
| **Load Factor** | `count / size` — measure of fullness |
| **Rehashing** | Double table size, redistribute all entries when load factor exceeds threshold |
| **O(1) average search** | Good hash + low load factor → near-constant time |

### Viva Q&A

**Q: What is a hash collision?**
When two distinct keys produce the same hash index. Our code handles this via chaining (storing both in the same bucket list).

**Q: Why rehash when load factor exceeds a threshold?**
High load factor increases collision probability, degrading performance from O(1) to O(n). Rehashing restores O(1) average complexity.

**Q: What makes a good hash function?**
Uniform distribution (keys spread evenly across buckets), deterministic (same key → same hash), fast to compute.

**Q: What are other collision resolution methods?**
- **Open Addressing**: Linear probing, quadratic probing, double hashing
- **Separate Chaining**: Each bucket holds a linked list or vector

---

## Experiment 8: Simple Hash Table Implementation

### Code

```python
class Product:
    def __init__(self, name, price):
        self.name = name
        self.price = price

class HashTable:
    def __init__(self, size=10):
        self.size = size
        self.table = [None] * size

    def hash_function(self, key):
        return len(key) % self.size

    def rehash(self):
        self.size *= 2
        old_table = self.table
        self.table = [None] * self.size
        for entry in old_table:
            if entry:
                for product in entry:
                    self.add_product(product[1])

    def add_product(self, product):
        key = product.name
        index = self.hash_function(key)
        if self.table[index] is None:
            self.table[index] = [(key, product)]
        else:
            for i, (ek, _) in enumerate(self.table[index]):
                if ek == key:
                    self.table[index][i] = (key, product)
                    return
            self.table[index].append((key, product))
        if sum(1 for b in self.table if b) / self.size > 0.7:
            self.rehash()

    def search_product(self, product_name):
        index = self.hash_function(product_name)
        bucket = self.table[index]
        if bucket:
            for key, product in bucket:
                if key == product_name:
                    return product
        return None
```

### Concepts Covered

| Concept | Explanation |
|---|---|
| **Simple hash: `len(key) % size`** | Uses string length — prone to collisions |
| **Chaining with tuples** | Each bucket stores `(key, product)` pairs |
| **Rehashing on load factor > 0.7** | Same concept as Exp 7 |
| **Update on duplicate** | If key exists, replace value instead of appending |

### Viva Q&A

**Q: Compare the hash functions in Exp 7 and Exp 8.**  
Exp 7: `sum(ASCII) % size` — better distribution. Exp 8: `len(key) % size` — many keys can have the same length, causing more collisions.

**Q: What happens when `rehash()` is called?**
Table size doubles. All existing entries are re-inserted using the new size, so their hash indices change.

**Q: Why store `(key, product)` instead of just `product`?**
To handle collisions — when searching a bucket, we compare by the original key to distinguish between different products that hash to the same index.

---

## Experiment 9: Dijkstra's Shortest Path Algorithm

### Code

```python
import heapq

class CityGraph:
    def __init__(self):
        self.graph = {}

    def add_edge(self, city1, city2, distance):
        self.graph.setdefault(city1, []).append((city2, distance))
        self.graph.setdefault(city2, []).append((city1, distance))

    def shortest_path(self, start_city, end_city):
        pq = [(0, start_city)]
        visited = set()
        while pq:
            current_distance, current_city = heapq.heappop(pq)
            if current_city in visited:
                continue
            visited.add(current_city)
            if current_city == end_city:
                return current_distance
            for neighbor, dist in self.graph.get(current_city, []):
                if neighbor not in visited:
                    heapq.heappush(pq, (current_distance + dist, neighbor))
        return float('inf')
```

### Concepts Covered

| Concept | Explanation |
|---|---|
| **Graph (Adjacency List)** | Dictionary mapping each node to list of `(neighbor, weight)` pairs |
| **Dijkstra's Algorithm** | Finds shortest path from source to all nodes in weighted graph (non-negative) |
| **Priority Queue (Min-Heap)** | Always processes the nearest unvisited node |
| **Greedy Approach** | At each step, pick the closest unvisited node |
| **Time Complexity** | O((V + E) log V) with heap |

### Viva Q&A

**Q: What is Dijkstra's algorithm used for?**
Shortest path in weighted graphs with non-negative edges — GPS navigation, network routing, social networks (friend suggestions).

**Q: Why use a priority queue?**
To efficiently get the nearest unvisited node in O(log V) instead of O(V) by scanning all nodes.

**Q: What happens if there are negative edge weights?**
Dijkstra fails — it assumes adding more edges only increases distance. Use Bellman-Ford instead.

**Q: What does `visited` prevent?**
Prevents reprocessing nodes whose shortest distance is already finalized.

**Q: Why is the complexity O((V+E) log V)?**
Each node is popped once (V pops × O(log V)), each edge is relaxed once (E pushes × O(log V)).

---

## Experiment 10: Sudoku Solver using Backtracking

### Code

```python
def is_valid(board, row, col, num):
    for i in range(9):
        if board[row][i] == num or board[i][col] == num or \
           board[row - row % 3 + i // 3][col - col % 3 + i % 3] == num:
            return False
    return True

def find_empty_location(board):
    for i in range(9):
        for j in range(9):
            if board[i][j] == 0:
                return i, j
    return None

def solve_sudoku(board):
    empty = find_empty_location(board)
    if not empty:
        return True
    row, col = empty
    for num in range(1, 10):
        if is_valid(board, row, col, num):
            board[row][col] = num
            if solve_sudoku(board):
                return True
            board[row][col] = 0
    return False
```

### Concepts Covered

| Concept | Explanation |
|---|---|
| **Backtracking** | DFS + pruning — try a choice, recurse, undo if it fails |
| **Recursion** | `solve_sudoku` calls itself with updated board |
| **Constraint Checking** | Row, column, and 3×3 subgrid must all be valid |
| **Base Case** | No empty cells → puzzle solved |
| **Worst-case Complexity** | O(9^(n)) where n = empty cells, but constraints prune massively |

### Viva Q&A

**Q: What is backtracking?**
A brute-force search that incrementally builds candidates and abandons ("backtracks" from) a candidate as soon as it determines it cannot lead to a valid solution.

**Q: How does the algorithm know when the puzzle is solved?**
`find_empty_location` returns `None` when no cell has value 0, meaning all cells are filled. This triggers `return True`.

**Q: What happens if a number doesn't work?**
It sets the cell back to 0 (backtrack) and tries the next number. If no number works, it returns `False` to the previous recursive call.

**Q: How does `is_valid` check the 3×3 box?**
`row - row % 3` gives the starting row of the box (0, 3, or 6). `col - col % 3` gives the starting column. Index `i // 3, i % 3` iterates the 3×3 cells.

**Q: Can this solver handle any 9×9 Sudoku?**
Yes — any valid Sudoku with a unique solution. For invalid or unsolvable puzzles, it returns `False`.

---

## Common Viva Questions

### Q: What is the difference between a data structure and an algorithm?
**Data structure**: Organization and storage of data (list, tree, graph). **Algorithm**: Step-by-step procedure to solve a problem (searching, sorting, pathfinding). They are interdependent — choosing the right data structure simplifies the algorithm.

### Q: What is time complexity and why is it important?
Time complexity describes how runtime grows with input size, expressed using Big-O notation (O(1), O(n), O(log n), O(n²)). It helps choose efficient algorithms for large inputs.

### Q: What is recursion and what are its components?
A function calling itself. Two mandatory parts:
1. **Base case** — stops recursion (e.g., `if not empty: return True`)
2. **Recursive case** — function calls itself with smaller input

### Q: Stable vs Unstable sorting?
**Stable**: Equal elements preserve original order (Merge Sort, Timsort). **Unstable**: Equal elements may swap order (Quick Sort, Heap Sort).

### Q: In-place vs Out-of-place?
**In-place**: Uses O(1) extra space (Quick Sort, selection sort). **Out-of-place**: Uses O(n) extra space (Merge Sort).

### Q: What is the Master Theorem used for?
Solving recurrences of form T(n) = aT(n/b) + f(n). Examples:
- Binary Search: T(n) = T(n/2) + O(1) → O(log n)
- Merge Sort: T(n) = 2T(n/2) + O(n) → O(n log n)

### Q: Difference between DFS and BFS?
| Feature | DFS | BFS |
|---|---|---|
| Data Structure | Stack (LIFO) | Queue (FIFO) |
| Strategy | Go deep first | Go level by level |
| Space | O(h) height | O(w) width |
| Use Case | Maze solving, topological sort | Shortest path (unweighted), web crawling |

### Q: What is the difference between a Tree and a Graph?
**Tree**: Connected, acyclic, exactly one path between any two nodes, hierarchical. **Graph**: May have cycles, multiple paths, no hierarchy.

### Q: Big-O vs Big-Theta vs Big-Omega?
- **Big-O** (O): Upper bound — worst-case
- **Big-Omega** (Ω): Lower bound — best-case
- **Big-Theta** (Θ): Tight bound — both upper and lower

### Q: What is Greedy vs Dynamic Programming?
**Greedy**: Make the locally optimal choice at each step (Dijkstra, Huffman). **DP**: Break into overlapping subproblems, store results (Fibonacci, Knapsack). Greedy is faster but doesn't always give the global optimum.
