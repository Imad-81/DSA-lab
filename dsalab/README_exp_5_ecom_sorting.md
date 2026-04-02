# Experiment 5: E-commerce Product Sorting

**Aim:** To develop a Python program that efficiently sorts a list of products based on multi-criteria: price, popularity, and alphabetical order.

**Algorithm:**
1. Define a `Product` class to encapsulate attributes like name, price, and popularity.
2. Implement **Merge Sort**, a divide-and-conquer algorithm ($O(n \log n)$).
3. **Divide**: Recursively split the list into two halves until single-element sublists remain.
4. **Conquer**: Merge the sublists back together in the desired order (ascending/descending).
5. Use `getattr()` to dynamically access product attributes based on the sorting criteria.

**Output:** Product list sorted by specified criteria (e.g., price ascending or popularity descending) is printed.
