# Loops
movies = ["Arrival", "Blade Runner 2049", "The Matrix"]

for movie in movies:
    print(f"\nThis movie is \t{movie.title()}")

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
for player in players[:3]:
    print(player.title())



# Tuples 
simple_tuple = (1, 2, 3, 4, 5) # Like constants, tuples are immutable
simple_list = ["value1", "value2", "value3"]
print(simple_list)
print(simple_tuple)

