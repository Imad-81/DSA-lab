/* 7.3. Learn how to perform basic operations on an

ArrayList in Java, including adding, removing, inserting,

and printing elements

*/

import java.util.ArrayList;

 

public class ArrayListDemo {

   public static void main(String[] args) {

 

       // Creating ArrayList

       ArrayList<String> fruits = new ArrayList<>();

 

       // Adding elements

       fruits.add("Apple");

       fruits.add("Banana");

       fruits.add("Mango");

 

       // Inserting element at specific position

       fruits.add(1, "Orange");

 

       // Removing element

       fruits.remove("Banana");

 

       // Printing elements

       System.out.println("Elements in ArrayList:");

       for (String fruit : fruits) {

           System.out.println(fruit);

       }

   }

}