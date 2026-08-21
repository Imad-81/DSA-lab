# Experiment 5: Greedy Algorithms
# 5(a) - Fractional Knapsack Problem & Activity Selection Problem
# 5(b) - Huffman Coding and Time Complexity Analysis

import heapq


# ==========================================================
# 5(a) - Part 1: Fractional Knapsack Problem using Greedy
# ==========================================================
def fractional_knapsack(weights, profits, capacity):
    items = []

    # Calculate profit/weight ratio
    for i in range(len(weights)):
        ratio = profits[i] / weights[i]
        items.append((ratio, weights[i], profits[i], i + 1))

    # Sort according to profit/weight ratio in descending order
    items.sort(reverse=True)

    total_profit = 0

    print("\nSelected Items:")

    for ratio, weight, profit, item_no in items:

        if capacity == 0:
            break

        # Take the complete item
        if weight <= capacity:
            capacity -= weight
            total_profit += profit

            print("Item", item_no,
                  "-> Complete item, Profit =", profit)

        # Take fraction of the item
        else:
            fraction = capacity / weight
            total_profit += profit * fraction

            print("Item", item_no,
                  "-> Fraction =", round(fraction, 2),
                  ", Profit =", round(profit * fraction, 2))

            capacity = 0

    return total_profit


# ==========================================================
# 5(a) - Part 2: Activity Selection Problem using Greedy
# ==========================================================
def activity_selection(start, finish):
    activities = []

    # Store activities as (finish, start, activity number)
    for i in range(len(start)):
        activities.append((finish[i], start[i], i + 1))

    # Sort according to finish time
    activities.sort()

    selected = []

    # Select the first activity
    selected.append(activities[0])
    last_finish = activities[0][0]

    # Select compatible activities
    for i in range(1, len(activities)):

        current_finish = activities[i][0]
        current_start = activities[i][1]

        if current_start >= last_finish:
            selected.append(activities[i])
            last_finish = current_finish

    return selected


# ==========================================================
# 5(b) - Huffman Coding using Greedy Algorithm
# ==========================================================
class Node:
    def __init__(self, char, freq):
        self.char = char
        self.freq = freq
        self.left = None
        self.right = None

    # Compare nodes according to frequency
    def __lt__(self, other):
        return self.freq < other.freq


def generate_codes(root, code="", codes=None):

    if codes is None:
        codes = {}

    # Leaf node
    if root.char is not None:
        codes[root.char] = code
        return codes

    # Traverse left
    generate_codes(root.left, code + "0", codes)

    # Traverse right
    generate_codes(root.right, code + "1", codes)

    return codes


def huffman_coding(chars, frequencies):

    heap = []

    # Create nodes and insert into min-heap
    for char, freq in zip(chars, frequencies):
        node = Node(char, freq)
        heapq.heappush(heap, node)

    # Build Huffman Tree
    while len(heap) > 1:

        # Remove two minimum-frequency nodes
        left = heapq.heappop(heap)
        right = heapq.heappop(heap)

        # Create new internal node
        new_node = Node(None, left.freq + right.freq)

        new_node.left = left
        new_node.right = right

        # Insert new node back into heap
        heapq.heappush(heap, new_node)

    # Root of Huffman Tree
    root = heap[0]

    # Generate codes
    codes = generate_codes(root)

    return codes


# ==========================================================
# Main Interactive Runner
# ==========================================================
def main():
    print("==========================================================")
    print("  EXPERIMENT 5: GREEDY ALGORITHMS")
    print("==========================================================")
    print("1. 5(a) - Fractional Knapsack Problem")
    print("2. 5(a) - Activity Selection Problem")
    print("3. 5(b) - Huffman Coding")
    print("4. Run All Experiments (Interactive)")
    print("==========================================================")

    choice = input("Enter choice (1-4) [default: 4]: ").strip()
    if not choice:
        choice = "4"

    if choice in ["1", "4"]:
        print("\n--- 5(a) Fractional Knapsack Problem ---")
        n = int(input("Enter number of items: "))
        weights = []
        profits = []
        for i in range(n):
            w = float(input(f"Enter weight of item {i + 1}: "))
            p = float(input(f"Enter profit of item {i + 1}: "))
            weights.append(w)
            profits.append(p)
        capacity = float(input("Enter knapsack capacity: "))
        max_profit = fractional_knapsack(weights, profits, capacity)
        print("\nMaximum Profit =", round(max_profit, 2))

    if choice in ["2", "4"]:
        print("\n--- 5(a) Activity Selection Problem ---")
        n = int(input("Enter number of activities: "))
        start = []
        finish = []
        for i in range(n):
            s = int(input(f"Enter start time of activity {i + 1}: "))
            f = int(input(f"Enter finish time of activity {i + 1}: "))
            start.append(s)
            finish.append(f)
        selected = activity_selection(start, finish)
        print("\nSelected Activities:")
        for finish_time, start_time, activity_no in selected:
            print("Activity", activity_no,
                  "-> Start:", start_time,
                  "Finish:", finish_time)
        print("\nMaximum number of activities =", len(selected))

    if choice in ["3", "4"]:
        print("\n--- 5(b) Huffman Coding ---")
        n = int(input("Enter number of characters: "))
        chars = []
        frequencies = []
        for i in range(n):
            char = input(f"Enter character {i + 1}: ")
            freq = int(input(f"Enter frequency of {char}: "))
            chars.append(char)
            frequencies.append(freq)
        codes = huffman_coding(chars, frequencies)
        print("\nHuffman Codes:")
        for char in chars:
            print(char, ":", codes[char])


if __name__ == "__main__":
    main()
