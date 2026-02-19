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
        new_student.next = self.head
        self.head = new_student

    def display_student(self):
        current = self.head
        while current:
            print(f"Name: {current.name}, Roll Number: {current.roll_number}, Marks: {current.marks}")

            current = current.next

    def calculate_cgpa(self):
        total_marks = 0 
        total_students = 0 
        
        



        

 