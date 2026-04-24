/* 10.2. (a) Write a Java program to sort the elements of the stack

in descending order.​
*/
import java.util.Stack;

import java.util.Collections;

 

public class StackSort {

   public static void main(String[] args) {

 

       Stack<Integer> stack = new Stack<>();

 

       stack.push(10);

       stack.push(40);

       stack.push(20);

       stack.push(30);

 

       System.out.println("Original Stack: " + stack);

 

       // Sort in descending order

       Collections.sort(stack, Collections.reverseOrder());

 

       System.out.println("Stack in Descending Order: " + stack);

   }

}

