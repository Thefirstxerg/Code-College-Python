#Dog class

class Dog(): # A class is a blueprint for creating instances, each instance created from the class will store a name and an age in this case
             # Instances are the objects you create from the class
    """A simple attempt to model a dog."""
    
    def __init__(self, name, age): # self is required in the method definition, self makes the method call itself
                                   # self is required because it tells python to create a new instance of Dog, or any class
        """Initialize name and age attributes."""
        self.name = name # Any variable prefixed with self is available to every method in the class
        self.age = age
        
    def sit(self):
        """Simulate a dog sitting in response to a command."""
        print(self.name.title() + " is now sitting.")
        
    def roll_over(self):
        """Simulate rolling over in response to a command."""
        print(self.name.title() + " rolled over!")

my_dog = Dog('willie', 6)

print(f"My dog's name is {my_dog.name.title()}.")
print(f"My dog is {my_dog.age} years old.")


# Calling methods
my_dog.sit()
my_dog.roll_over()


# Creating multiple instances
my_dog = Dog('willie', 6)
your_dog = Dog('lucy', 3)

print(f"\nMy dog's name is {my_dog.name.title()}.")
print(f"My dog is {my_dog.age} years old.")
my_dog.sit()

print(f"\nYour dog's name is {your_dog.name.title()}.")
print(f"Your dog is {your_dog.age} years old.")
your_dog.sit()


# Modifying attributes
my_dog = Dog('willie', 6)
my_dog.age = 7 # Modifying the age attribute
print(f"My dog is now {my_dog.age} years old.")
my_dog.sit()