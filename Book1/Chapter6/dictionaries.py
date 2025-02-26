# # Dictionaries/Objects

# alien_0 = {'color': 'green', 'points': 5}
# print(alien_0['color'])
# print(alien_0['points'])


# # Accessing Values in a Dictionary
# alien_0 = {'color': 'green'}
# print(alien_0['color'])
# # print(alien_0['points'])  # KeyError: 'points'


# # Adding and removing New Key-Value Pairs
# alien_0 = {'color': 'green', 'points': 5}
# print(alien_0)
# alien_0['x_position'] = 0
# alien_0['y_position'] = 25
# print(alien_0)
# del alien_0['points']
# print(alien_0)


# # Modifying Values in a Dictionary
# alien_0 = {'color': 'green'}
# print(f"The alien is {alien_0['color']}.")
# alien_0['color'] = 'yellow'
# print(f"The alien is now {alien_0['color']}.")
# alien_0['color'] = 'red'
# print(f"The alien is now {alien_0['color']}.")
# alien_0['color'] = 'blue'
# print(f"The alien is now {alien_0['color']}.")


# # A Dictionary of Similar Objects
# favorite_languages = {
#     'jen': 'python',
#     'sarah': 'c',
#     'edward': 'ruby',
#     'phil': 'python',
# }
# print(f"Sarah's favorite language is {favorite_languages['sarah'].title()}.")
# print(f"Phil's favorite language is {favorite_languages['phil'].title()}.")
# print(f"Edward's favorite language is {favorite_languages['edward'].title()}.")
# print(f"Jen's favorite language is {favorite_languages['jen'].title()}.")
# print()


# # Using get() to Access Values
# alien_0 = {'color': 'green', 'speed': 'slow'}
# print(alien_0.get('color'))

# point_value = alien_0.get('points', 'No point value assigned.') # WHen the key is not found in the dictionary, the second argument is returned.
# print(point_value)





# Own example: looping through a dictionary and printing the key and value
alien_0 = {'color': 'green', 
           'points': 5,
           'x_position': 0,
           'y_position': 25}

for key, value in alien_0.items():
    print(f"\n{key}: {value}")
    if key == 'color':
        print(f"\nThe alien is {value}.")
    elif key == 'points':
        print(f"The alien has {value} points.")
    elif key == 'x_position':
        value = alien_0['x_position']
        print(f"The alien is now at position {value}.")
    elif key == 'y_position':
        value = alien_0['y_position']
        print(f"The alien is now at position {value}.") 


# Nesting
# A list of dictionaries
dad = {'name': 'Dad', 'age': 50}
mom = {'name': 'Mom', 'age': 45}
son = {'name': 'Son', 'age': 20}
daughter = {'name': 'Daughter', 'age': 15}

family = [dad, mom, son, daughter]
for member in family:
    print(member)
