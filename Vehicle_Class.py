# define vehicle class
class Vehicle:
    def __init__(self, vehicle_type):
        self.vehicle_type = vehicle_type
 # define subclass in vehicle 
class Automobile(Vehicle):
    def __init__(self, vehicle_type, year, make, model
                 ,doors, roof):
        super().__init__(vehicle_type) #inititialize superclass

        self.year = year
        self.make = make
        self.model = model
        self.doors = doors
        self.roof = roof

def validate_year(year):
    if year.isdigit():   # ensure numeric entry
        return True
    return False

def validate_doors(doors):
    return doors in ["2", "4"] # ensure either 2 or 4 is selected

def validate_roof(roof):
    return roof.lower() in ["solid", "sun roof"] # ensure one of the two selected

def main():
    vehicle_type = "car"  # Fixed as "car" for this application
# inputs and validation
    while True:
        year = input("Enter the Year: ")
        if validate_year(year):
            break
        else:
            print("Invalid year. Please enter a valid year between 1886 and 2024.")

    make = input("Enter the Make: ")
    model = input("Enter the Model: ")

    while True:
        doors = input("Enter the number of doors (2 or 4): ")
        if validate_doors(doors):
            break
        else:
            print("Invalid number of doors. Please enter 2 or 4.")

    while True:
        roof = input("Enter the type of roof (solid or sun roof): ")
        if validate_roof(roof):
            break
        else:
            print("Invalid roof type. Please enter 'solid' or 'sun roof'.")

    car = Automobile(vehicle_type, year, make, model, doors, roof)
    
#display given details

    print("\nVehicle Information:")
    print(f"  Vehicle type: {car.vehicle_type}")
    print(f"  Year: {car.year}")
    print(f"  Make: {car.make}")
    print(f"  Model: {car.model}")
    print(f"  Number of doors (2 or 4): {car.doors}")
    print(f"  Type of roof (solid or sunroof): {car.roof}")

if __name__ == "__main__":
    main()




