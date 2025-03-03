class Car:
    """A simple attempt to represent a car."""

    def __init__(self, make, model, year):
        """Initialize attributes to describe a car."""
        self.make = make  # Car's make (e.g., Toyota)
        self.model = model  # Car's model (e.g., Corolla)
        self.year = year  # Year of manufacture
        self.odometer_reading = 0  # Initial odometer reading set to 0

    def get_descriptive_name(self):
        """Return a neatly formatted descriptive name."""
        long_name = f"{self.year} {self.make} {self.model}"  # Combine year, make, and model
        return long_name.title()  # Return the formatted string with title case

    def read_odometer(self):
        """Print a statement showing the car's mileage."""
        print(f"This car has {self.odometer_reading} miles on it.")  # Print the current odometer reading

    def update_odometer(self, mileage):
        """Set the odometer reading to the given value."""
        if mileage >= self.odometer_reading:  # Ensure the new mileage is not less than the current reading
            self.odometer_reading = mileage  # Update the odometer reading
        else:
            print("You can't roll back an odometer!")  # Print a warning if an attempt is made to roll back

    def increment_odometer(self, miles):
        """Add the given amount to the odometer reading."""
        self.odometer_reading += miles  # Increment the odometer reading by the given miles


class Battery:
    """A simple attempt to model a battery for an electric car."""

    def __init__(self, battery_size=40):
        """Initialize the battery's attributes."""
        self.battery_size = battery_size  # Set the battery size, default is 40 kWh

    def describe_battery(self):
        """Print a statement describing the battery size."""
        print(f"This car has a {self.battery_size}-kWh battery.")  # Print the battery size

    def get_range(self):
        """Print a statement about the range this battery provides."""
        if self.battery_size == 40:
            range = 150  # Range for 40 kWh battery
        elif self.battery_size == 65:
            range = 225  # Range for 65 kWh battery

        print(f"This car can go about {range} miles on a full charge.")  # Print the range


class ElectricCar(Car):
    """Represent aspects of a car, specific to electric vehicles."""

    def __init__(self, make, model, year):
        """
        Initialize attributes of the parent class.
        Then initialize attributes specific to an electric car.
        """
        super().__init__(make, model, year)  # Call the __init__ method of the parent class (Car) to initialize common attributes
        self.battery = Battery()  # Initialize the battery attribute specific to electric cars

# Create an instance of ElectricCar
my_leaf = ElectricCar('nissan', 'leaf', 2024)

# Print the descriptive name of the car
print(my_leaf.get_descriptive_name())

# Describe the battery of the car
my_leaf.battery.describe_battery()

# Print the range of the car based on the battery size
my_leaf.battery.get_range()