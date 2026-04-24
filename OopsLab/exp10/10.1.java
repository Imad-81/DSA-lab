/* 10.1. Write a Java program to implement a stack with push and

pop operations. Find the top element of the stack and check

whether it is empty.
*/
class Stack {

   int arr[] = new int[10];

   int top = -1;

 

   // Push operation

   void push(int value) {

       if (top == arr.length - 1) {

           System.out.println("Stack Overflow");

       } else {

           arr[++top] = value;

           System.out.println(value + " pushed into stack");

       }

   }

 

   // Pop operation

   void pop() {

       if (top == -1) {

           System.out.println("Stack Underflow");

       } else {

           System.out.println(arr[top] + " popped from stack");

           top--;

       }

   }

 

   // Peek (Top element)

   void peek() {

       if (top == -1) {

           System.out.println("Stack is empty");

       } else {

           System.out.println("Top element: " + arr[top]);

       }

   }

 

   // Check if stack is empty

   void isEmpty() {

       if (top == -1) {

           System.out.println("Stack is empty");

       } else {

           System.out.println("Stack is not empty");

       }

   }

}

 

public class StackDemo {

   public static void main(String[] args) {

 

       Stack s = new Stack();

 

       s.push(10);

       s.push(20);

       s.push(30);

 

       s.peek();      // Find top element

       s.pop();       // Remove element

       s.isEmpty();   // Check if stack is empty

   }

}