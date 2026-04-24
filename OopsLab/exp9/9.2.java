/* 9.2. Write a Java program to illustrate the usage of the

ReadWriteLock interface for concurrent read- write accessto

a shared resource.

import java.util.concurrent.locks.ReadWriteLock;

import java.util.concurrent.locks.ReentrantReadWriteLock;

*/

class SharedResource {

   private int value = 0;

 

   // Create ReadWriteLock

   private final ReadWriteLock lock = new ReentrantReadWriteLock();

 

   // Read method

   public void readValue() {

       lock.readLock().lock();

       try {

           System.out.println(Thread.currentThread().getName() + " reads value: " + value);

       } finally {

           lock.readLock().unlock();

       }

   }

 

   // Write method

   public void writeValue(int newValue) {

       lock.writeLock().lock();

       try {

           System.out.println(Thread.currentThread().getName() + " writes value: " + newValue);

           value = newValue;

       } finally {

           lock.writeLock().unlock();

       }

   }

}

 

class ReadThread extends Thread {

   SharedResource resource;

 

   ReadThread(SharedResource resource, String name) {

       super(name);

       this.resource = resource;

   }

 

   public void run() {

       resource.readValue();

   }

}

 

class WriteThread extends Thread {

   SharedResource resource;

   int value;

 

   WriteThread(SharedResource resource, int value, String name) {

       super(name);

       this.resource = resource;

       this.value = value;

   }

 

   public void run() {

       resource.writeValue(value);

   }

}

 

public class ReadWriteLockDemo {

   public static void main(String[] args) {

 

       SharedResource resource = new SharedResource();

 

       ReadThread r1 = new ReadThread(resource, "Reader-1");

       ReadThread r2 = new ReadThread(resource, "Reader-2");

 

       WriteThread w1 = new WriteThread(resource, 100, "Writer-1");

 

       w1.start();

       r1.start();

       r2.start();

   }

}