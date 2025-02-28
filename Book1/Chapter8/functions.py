# Functions 

def greet_user(): # Function definition 
    print("Hello!")
greet_user()

def greet_user(username): # Function definition with parameter
    print(f"Hello, {username.title()}!")
greet_user('jesse')


# Positional Arguments
def describe_pet(animal_type, pet_name): # Function definition with multiple parameters
    print(f"I have a {animal_type}.")
    print(f"My {animal_type}'s name is {pet_name.title()}.")
describe_pet('dog', 'buddy')


# Keyword Arguments
def describe_pet(animal_type, pet_name): # Function definition with multiple parameters
    print(f"I have a {animal_type}.")
    print(f"My {animal_type}'s name is {pet_name.title()}.")
describe_pet(animal_type='dog', pet_name='buddy') # Function call with keyword arguments


# Default Values
def describe_pet(pet_name, animal_type='dog'): # Function definition with default value
    print(f"I have a {animal_type}.")
    print(f"My {animal_type}'s name is {pet_name.title()}.")
describe_pet(pet_name='buddy')


# Return Values
def get_formatted_name(first_name, last_name): # Function definition with return value
    full_name = f"{first_name} {last_name}"
    return full_name.title() # Return value is the output of the function
musician = get_formatted_name('jimi', 'hendrix')
print(musician)


# Making an Argument Optional
def get_formatted_name(first_name, last_name, middle_name=''): # Function definition with optional parameter
    if middle_name:
        full_name = f"{first_name} {middle_name} {last_name}"
    else:
        full_name = f"{first_name} {last_name}"
    return full_name.title() # Using if else statements and return to make function output have optional amounts of parameters
musician = get_formatted_name('john', 'hooker')
print(musician)
musician = get_formatted_name('john', 'lee', 'hooker')
print(musician)

 
# Returning a Dictionary
def build_person(first_name, last_name): # Function definition with return value
    person = {'first': first_name, 'last': last_name}
    return person
musician = build_person('jimi', 'hendrix')
print(musician)


# Using a Function with a while Loop
def get_formatted_name(first_name, last_name): # Just formats inputted names
    full_name = f"{first_name} {last_name}"
    return full_name.title()

while True:
    print("\nPlease tell me your name:")
    print("(enter 'q' at any time to quit)")
    f_name = input("First name: ")
    if f_name == 'q':
        break
    l_name = input("Last name: ") 
    if l_name == 'q':
        break
    formatted_name = get_formatted_name(f_name, l_name) # Uses input methods to get user input and put it into the parameters of the function
    print(f"\nHello, {formatted_name}!")


# Passing a List
def greet_users(names):
    for name in names:
        msg = f"Hello, {name.title()}!" 
        print(msg)
usernames = ['hannah', 'ty', 'margot']
greet_users(usernames) # Function calls all the values in the list and uses them inside the function


# Modifying a List in a Function
def print_models(unprinted_designs, completed_models): 
    while unprinted_designs: # This function takes the last value of the list and puts it into the completed_models list
        current_design = unprinted_designs.pop() # The last value of the list is removed
        print(f"Printing model: {current_design}") 
        completed_models.append(current_design) # The last value of the list is added to the completed_models list

def show_completed_models(completed_models): # This function prints all the values in the completed_models list
    print("\nThe following models have been printed:")
    for completed_model in completed_models:
        print(completed_model)
        
unprinted_designs = ['iphone case', 'robot pendant', 'dodecahedron']
completed_models = []
print_models(unprinted_designs, completed_models)
show_completed_models(completed_models)


# Preventing a Function from Modifying a List
def print_models(unprinted_designs, completed_models): # This function takes the last value of the list and puts it into the completed_models list
    while unprinted_designs:
        current_design = unprinted_designs.pop()
        print(f"Printing model: {current_design}")
        completed_models.append(current_design)

def show_completed_models(completed_models): # This function prints all the values in the completed_models list
    print("\nThe following models have been printed:")
    for completed_model in completed_models:
        print(completed_model)

unprinted_designs = ['iphone case', 'robot pendant', 'dodecahedron']
completed_models = []
print_models(unprinted_designs[:], completed_models) # The colon makes a copy of the entire list, thus preventing the original list from being modified
show_completed_models(completed_models)


# Passing an Arbitrary Number of Arguments
def make_pizza(*toppings): # This function takes an arbitrary amount of arguments and puts them into a tuple
                           # , the * is used to indicate that the function can take any amount of arguments
    print(toppings)
make_pizza('pepperoni') # a tuple is created with the value of the argument
make_pizza('mushrooms', 'green peppers', 'extra cheese')

import pizza # Importing the pizza module
pizza.make_pizza(16, 'pepperoni') # Calling the make_pizza function from the pizza module
pizza.make_pizza(12, 'mushrooms', 'green peppers', 'extra cheese')
 




#Own example of function with inputs and return values
def describe_city(city, country= "RSA"):
    print(f"{city} is in {country}")
    if city=="Pretoria":
        return f"{city}, ooh so you use a Gautrain.."
    elif city == "Jhb":
        return f"{city}, have you seen Vilakazi street"
    elif city == "Cpt":
        return f"{city}, have you been to Camps bay"
    elif city == "Kimberly":
        return f"{city}, have you seen the big hole of Diamonds"
    else:
        return f"I don't know {city}"

output = describe_city(input("Enter your city: "))
print(output)




# Try it yourself
from car import Car # Importing a single class called Car from car.py
from car import read_odometer as ro # Importing a single function called read_odometer from car.py and renaming it to ro using aliasing
import car as c # You can also create an alias for the entire module
# From is used to import a specific class or function from a module
# Import is used to import the entire module


my_new_car = Car('audi', 'a4', 2024)
print(my_new_car.get_descriptive_name())

my_new_car.odometer_reading = 23
my_new_car.ro()
