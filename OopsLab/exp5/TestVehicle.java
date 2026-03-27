class Vehicle {

    void drive() {

        System.out.println("Driving a vehicle");

    }

}

class Car extends Vehicle {

    @Override

    void drive() {

        System.out.println("Repairing a car");

    }

}

public class TestVehicle {

    public static void main(String[] args) {

        Car c = new Car();

        c.drive();

    }

}