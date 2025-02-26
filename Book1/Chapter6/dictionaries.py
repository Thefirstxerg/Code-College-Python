# Dictionaries/Objects

alien_0 = {'color': 'green', 'points': 5} # A dictionary is a collection of key-value pairs. Each key is connected to a value, 
                                          # and you can use a key to access the value associated with that key.
print(alien_0['color'])
print(alien_0['points'])


# Accessing Values in a Dictionary
alien_0 = {'color': 'green'}
print(alien_0['color'])
# print(alien_0['points'])  # KeyError: You cannot access a key that does not exist in the dictionary.


# Adding and removing New Key-Value Pairs
alien_0 = {'color': 'green', 'points': 5}
print(alien_0)
alien_0['x_position'] = 0
alien_0['y_position'] = 25
print(alien_0)
del alien_0['points'] # The del statement removes the key-value pair from the dictionary.
print(alien_0)


# Modifying Values in a Dictionary
alien_0 = {'color': 'green'}
print(f"The alien is {alien_0['color']}.")
alien_0['color'] = 'yellow' # Modifying the value of the key color.
print(f"The alien is now {alien_0['color']}.")
alien_0['color'] = 'red'
print(f"The alien is now {alien_0['color']}.")
alien_0['color'] = 'blue'
print(f"The alien is now {alien_0['color']}.")


# A Dictionary of Similar Objects
favorite_languages = {
    'jen': 'python',
    'sarah': 'c',
    'edward': 'ruby',
    'phil': 'python',
} 
print(f"Sarah's favorite language is {favorite_languages['sarah'].title()}.") # The title() method capitalizes the first letter of each
print(f"Phil's favorite language is {favorite_languages['phil'].title()}.")   # word in the string.
print(f"Edward's favorite language is {favorite_languages['edward'].title()}.")
print(f"Jen's favorite language is {favorite_languages['jen'].title()}.")
print()


# Using get() to Access Values
alien_0 = {'color': 'green', 'speed': 'slow'}
print(alien_0.get('color'))

point_value = alien_0.get('points', 'No point value assigned.') # WHen the key is not found in the dictionary, the second argument is returned.
print(point_value)





# Own example: looping through a dictionary and printing the key and value
alien_0 = {'color': 'green', 
           'points': 5,
           'x_position': 0,
           'y_position': 25}

for key, value in alien_0.items(): # The items() method returns a list of key-value pairs, 
    print(f"\n{key}: {value}")     # key variable is assigned to the key and value variable is assigned to the value.
    if key == 'color': # Checking if the key is color, then print the color value of the alien.
        print(f"\nThe alien is {value}.")
    elif key == 'points':
        print(f"The alien has {value} points.")
    elif key == 'x_position': # Checking if the key is x_position, modify the x_position, then print the x_position value of the alien.
        value = alien_0['x_position']
        print(f"The alien is now at position {value}.")
    elif key == 'y_position':
        value = alien_0['y_position']
        print(f"The alien is now at position {value}.") 


# Nesting
# A list of dictionaries
dad = {'name': 'Dad', 'age': 50, 'hometown': 'Pretor'}
mom = {'name': 'Mom', 'age': 45, 'hometown': 'Johannesburg'}
son = {'name': 'Son', 'age': 20, 'hometown': 'Pretoria'}
daughter = {'name': 'Daughter', 'age': 15, 'hometown': 'Pretoria'}

family = [dad, mom, son, daughter]

for member in family: # Looping through the list of dictionaries and printing the key-value pairs.
    print(f"{member}")