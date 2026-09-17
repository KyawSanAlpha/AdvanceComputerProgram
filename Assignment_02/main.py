from rental import Vehicle, Renter, ElectricCar, Motorbike

def main():
    print("--- 1. Vehicle and Renter Operations ---")
    car = Vehicle("Toyota", "Yaris", "1AB234")
    renter = Renter("John Doe", 1001)

    print(f"Initial state: {car}")
    car.rent()
    renter.rented.append(car)
    print(f"After rent: {car}")
    
    car.return_vehicle()
    renter.rented.remove(car)
    print(f"After return: {car}")
    print()

    print("--- 2. Encapsulation / Input Validation ---")
    try:
        invalid_renter = Renter("", 12345)
    except ValueError as e:
        print(f"Caught expected error: {e}")

    try:
        invalid_license = Renter("Jane Doe", -5)
    except ValueError as e:
        print(f"Caught expected error: {e}")
    print()

    print("--- 3. Polymorphism Demonstration ---")
    fleet = [
        Vehicle("Honda", "Civic", "2CD567"),
        ElectricCar("Tesla", "Model 3", "EV9999", 75.0),
        Motorbike("Yamaha", "R15", "3EF890", 155)
    ]

    for vehicle in fleet:
        print(vehicle)

if __name__ == "__main__":
    main()