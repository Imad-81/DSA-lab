/*8.2. (a) Write a Java program to get a substring of a given string at

two specified positions.
*/

public class SubstringExample {

   public static void main(String[] args) {

 

       String str = "Programming";

 

       int start = 3;

       int end = 8;

 

       String result = str.substring(start, end);

 

       System.out.println("Original String: " + str);

       System.out.println("Substring: " + result);

   }

}