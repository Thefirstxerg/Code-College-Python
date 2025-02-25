# Loops
movies = ["Arrival", "Blade Runner 2049", "The Matrix"]

for i in movies:
    print(f"\nThis movie is \t{i.title()}")

print("Because this is not indented, it is not part of the loop")


# Range
for int in range(1, 6): #from 1(included) to 6(excluded)
    print(int)

for int2 in range(2, 11, 2): #from 2(included) to 11(excluded) in steps of 2
    print(int2)

squares = []
for value in range(1, 11):
    square = value ** 2
    squares.append(square)
print(squares)
print(min(squares))
print(max(squares)) 
print(sum(squares))


# List Comprehensions
squares = [value**2 for value in range(1, 11)]
print(squares)  


players = ['charles', 'martina', 'michael', 'florence', 'eli']
print("Here are the first three players on my team:")
for player in players[:3]: # First Three
    print(player.title())



# Tuples 
simple_tuple = (1, 2, 3, 4, 5) # Like constants, tuples are immutable, and are defined by (), not []
simple_list = ["value1", "value2", "value3"]
print(simple_list)
print(simple_tuple)

simple_list.append("value4") 
simple_list.insert(4, "value5")
simple_list.pop() #simple_list[-1].remove
print(simple_list)
print(sorted(simple_list, reverse = True))


# 4-13. Buffet: A buffet-style restaurant offers only five basic foods. Think of five
# simple foods, and store them in a tuple.
# • Use a for loop to print each food the restaurant offers.
# • Try to modify one of the items, and make sure that Python rejects the
# change.
# • The restaurant changes its menu, replacing two of the items with different
# foods. Add a line that rewrites the tuple, and then use a for loop to print
# each of the items on the revised menu.

buffet = ("Pasta", "Pizza", "Burger", "Salad", "Fries")
for food in buffet:
    print(food)

# buffet[0] = "Spaghetti" # This will not work
buffet = ("Spaghetti", "Pizza", "Burger", "Salad", "Fries")
for food in buffet:
    print(food)



# https://python.org/dev/peps/pep-0008