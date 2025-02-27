# Classes
from car import Car # Importing a single class called Car from car.py
from car import read_odometer as ro # Importing a single function called read_odometer from car.py and renaming it to ro using aliasing
import car as c # You can also create an alias for the entire module
# From is used to import a specific class or function from a module
# Import is used to import the entire module


my_new_car = Car('audi', 'a4', 2024)
print(my_new_car.get_descriptive_name())

my_new_car.odometer_reading = 23
my_new_car.read_odometer()