# Experiment 3: Stack Data Structure & Postfix Evaluator

**Aim:** To implement a Stack data structure and use it to evaluate postfix mathematical expressions.

**Algorithm:**
1. Define a `Stack` class with `push()`, `pop()`, and `is_empty()` methods using a Python list.
2. For postfix evaluation, scan the expression from left to right.
3. If the character is an operand, push it onto the stack.
4. If it's an operator, pop two operands, apply the operation, and push the result back.
5. After scanning, the last remaining element in the stack is the final result.

**Output:** User-entered postfix expressions return computed results (e.g., `23*5+` returns `11`).
