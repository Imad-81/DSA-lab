/* (b) Write a Java program to reverse the elements of a stack.
*/ 
import java.util.Stack;

 

public class ReverseStack {

   public static void main(String[] args) {

 

       Stack<Integer> stack = new Stack<>();

 

       stack.push(1);

       stack.push(2);

       stack.push(3);

       stack.push(4);

 

       System.out.println("Original Stack: " + stack);

 

       Stack<Integer> reversedStack = new Stack<>();

 

       // Reverse stack

       while (!stack.isEmpty()) {

           reversedStack.push(stack.pop());

       }

 

       System.out.println("Reversed Stack: " + reversedStack);

   }

}