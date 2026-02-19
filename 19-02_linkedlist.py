class Node:
    def __init__(self, name, roll_number, marks):
        self.name = name 
        self.roll_number = roll_number
        self.marks = marks

class LinkedList: 
    def __init__(self):
        self.head = None

    def add_student(self, name, roll_number, marks):
        new_student = Node(name, roll_number, marks)
        


        

 