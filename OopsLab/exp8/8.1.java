/*8.1. Write a Java program to compare two strings

lexicographically.

Two strings are lexicographically equal if they are the same

length and contain the same charactersin the same positions.
*/

public class LexicoCompare {

   public static void main(String[] args) {

 

       String str1 = "Apple";

       String str2 = "Apple";

 

       int result = str1.compareTo(str2);

 

       if (result == 0) {

           System.out.println("Both strings are lexicographically equal.");

       }

       else if (result > 0) {

           System.out.println(str1 + " is greater than " + str2);

       }

       else {

           System.out.println(str1 + " is smaller than " + str2);

       }

   }

}