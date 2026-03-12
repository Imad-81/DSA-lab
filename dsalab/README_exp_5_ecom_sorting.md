# Experiment 5: E-commerce Product Sorting

## Objective
To develop a Python program that efficiently sorts a list of products based on multiple criteria: price, popularity, and alphabetical order.

## Core Concepts Used

### 1. Merge Sort Algorithm
We implemented **Merge Sort**, a classic divide-and-conquer algorithm.
- **Divide**: The list is recursively split into two halves until each sub-list contains only one element.
- **Conquer**: The sub-lists are merged back together in a sorted manner.
- **Time Complexity**: $O(n \log n)$ in all cases (best, average, and worst), making it highly efficient for large datasets compared to simpler algorithms like Bubble Sort ($O(n^2)$).
- **Stability**: It is a stable sort, meaning it preserves the relative order of elements with equal keys.

### 2. Object-Oriented Programming (OOP)
- **Product Class**: We used a `Product` class to encapsulate product attributes (Name, Price, Popularity).
- **Encapsulation**: This allows us to handle complex data structures as single objects, making the code more readable and maintainable.

### 3. Dynamic Attribute Access
- **getattr()**: The program uses Python's built-in `getattr()` function to dynamically access product attributes based on user input. This makes the sorting function generic and capable of sorting by any field without redundant code.

## Real-World Relevance
Efficient sorting is critical in e-commerce to help users find products quickly. For a platform with millions of items, an $O(n^2)$ algorithm would be too slow, whereas an $O(n \log n)$ algorithm provides the performance needed for a smooth user experience.
