# Experiment 4: Ticketing System using Priority Queue

**Aim:** To design and implement a customer support ticketing system implementing First-Come-First-Served (FCFS) for elements with the same priority using a Priority Queue.

**Algorithm:**
1. Create a `Ticket` class with attributes: `name`, `issue`, `priority`, and `timestamp`.
2. Use Python's `heapq` module to implement a min-heap where a lower numerical value represents higher priority.
3. Define the `__lt__` method in the `Ticket` class to compare priority first, then timestamp if priorities are equal.
4. `heappush` adds a ticket to the heap while preserving the heap property.
5. `heappop` removes and returns the highest priority ticket from the top.

**Output:** Urgent tickets are processed before normal ones, and equal priority tickets are handled in order of arrival.
