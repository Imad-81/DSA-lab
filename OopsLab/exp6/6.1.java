/*6.1. Write a Java program to create a class known as

"BankAccount" with methods called deposit() and

withdraw(). Create a subclass called SavingsAccount that

overrides the withdraw() method to prevent withdrawals if

the account balance falls below one hundred.

*/

class BankAccount {

   double balance;

 

   // Constructor

   BankAccount(double balance) {

       this.balance = balance;

   }

 

   // Deposit method

   void deposit(double amount) {

       balance = balance + amount;

       System.out.println("Amount Deposited: " + amount);

       System.out.println("Current Balance: " + balance);

   }

 

   // Withdraw method

   void withdraw(double amount) {

       if (amount <= balance) {

           balance = balance - amount;

           System.out.println("Amount Withdrawn: " + amount);

       } else {

           System.out.println("Insufficient Balance");

       }

       System.out.println("Current Balance: " + balance);

   }

}

 

// Subclass

class SavingsAccount extends BankAccount {

 

   // Constructor

   SavingsAccount(double balance) {

       super(balance);

   }

 

   // Overriding withdraw method

   @Override

   void withdraw(double amount) {

       if ((balance - amount) < 100) {

           System.out.println("Withdrawal denied! Minimum balance of 100 must be maintained.");

       } else {

           balance = balance - amount;

           System.out.println("Amount Withdrawn: " + amount);

           System.out.println("Current Balance: " + balance);

       }

   }

}

 

// Main class

public class Main {

   public static void main(String[] args) {

 

       SavingsAccount acc = new SavingsAccount(500);

 

       acc.deposit(200);

       acc.withdraw(300);

       acc.withdraw(400); // This should be denied

   }

}

