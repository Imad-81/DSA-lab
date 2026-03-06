/** 
* Write a Java program to print an array after changing the rows and columns of a two-dimensional array. 
* Original Array: 10 20 30 40 50 60 After changing the rows and columns of the said array: 10 40 20 50 30 60.
*/

public class TransposeArray {

   public static void main(String[] args) {

 

       int[][] original = {

           {10, 20, 30},

           {40, 50, 60}

       };

       int rows = original.length;

       int cols = original[0].length;

       int[][] transpose = new int[cols][rows];

       for (int i = 0; i < rows; i++) {

           for (int j = 0; j < cols; j++) {

               transpose[j][i] = original[i][j];

           }

       }

       System.out.println("Original Array:");

       for (int i = 0; i < rows; i++) {

           for (int j = 0; j < cols; j++) {

               System.out.print(original[i][j] + " ");

           }

           System.out.println();

       }

       System.out.println("After changing rows and columns:");

       for (int i = 0; i < transpose.length; i++) {

           for (int j = 0; j < transpose[i].length; j++) {

               System.out.print(transpose[i][j] + " ");

           }

           System.out.println();

       }

   }

}