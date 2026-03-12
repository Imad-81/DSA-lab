# Linked List to manage student information and calculate GPA

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
            print(
                f"Name: {current.name}, "
                f"Roll Number: {current.roll_number}, "
                f"Marks: {current.marks}"
            )
            current = current.next

    def calculate_gpa(self):
        total_marks = 0
        total_students = 0

        current = self.head
        while current:
            total_marks += current.marks
            total_students += 1
            current = current.next

        if total_students == 0:
            return 0  # Avoid division by zero

        average_marks = total_marks / total_students

        # GPA calculation logic
        if average_marks >= 90:
            return "A"
        elif average_marks >= 80:
            return "B"
        elif average_marks >= 70:
            return "C"
        elif average_marks >= 60:
            return "D"
        else:
            return "F"


if __name__ == "__main__":
    student_list = LinkedList()

    # Add students
    student_list.add_student("Alice", "A001", 85)
    student_list.add_student("Bob", "A002", 92)
    student_list.add_student("Charlie", "A003", 78)

    # Display students
    print("List of Students:")
    student_list.display_students()

    # Calculate and display GPA
    gpa = student_list.calculate_gpa()
    print(f"\nCalculated GPA: {gpa}")