# Experiment 6: Searching Algorithms

**Aim:** To study and compare the efficiency of Linear Search and Binary Search algorithms.

**Algorithm:**
1. Initialize a dataset of `Product` objects.
2. For **Linear Search**, scan through the list sequentially until the target element is found ($O(n)$).
3. For **Binary Search**, first sort the dataset by the search key ($O(n \log n)$).
4. Repeatedly divide the search interval in half to find the target element ($O(\log n)$).
5. Compare search results and performance.

**Output:** Search results (Found/Not Found) and their indices are printed for both algorithms.
