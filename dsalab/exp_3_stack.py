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
    
    def evaluate_expression(expression):
        stack = Stack()
        operators = {'+', '-', '*', '/'}
        for char in expression: 
            if char.isdigit():
                stack.push(int(char))

            elif char in operators:
                operand2 = stack.pop()  #last in first out
                operand1 = stack.pop()

                if char == '+':
                    stack.push(operand1 + operand2)
                elif char == '-':
                    stack.push(operand1 - operand2)
                elif char == '*':
                    stack.push(operand1 * operand2)
                elif char == '/':
                    stack.push(operand1/operand2)
            
        return stack.pop()

if __name__ == "__main__":
    expression = input("Enter the expression: ")
    result = Stack.evaluate_expression(expression)
    print(f"Result of the expression {expression} is {result}")
                


