# Lists/Arrays 
my_list = ["Aidan", "Asanda", "Cadee", "Courtney", "Ethan", "Lindo", "Phomello", "Ronny", "Sibu", "Tom", "Ulrich", "Mieke"]
print(my_list)
print(my_list[1])

print(my_list[-1]) # Prints the last element
print(my_list[1:3]) # Prints the second and third elements (from index1 to index3)
print(my_list[:3]) # Prints the first three elements

# Modifying Lists
my_list[1] = "Asanda M"
my_list.append("Mieke") # Adds an element to the end of the list
my_list.insert(0, "Aidan M") # Adds an element at a specific index
my_list.extend(["Mieke", "Ulrich"]) # Adds multiple elements to the end of the list
my_list.remove("Tom") # alt is del my_list[my_list.index("Tom")]
my_list.pop() # Removes the last element
my_list.pop(0) # Removes the element at index 0
my_list.clear() # Removes all elements
print(my_list)


# Sorting lists 
my_list.sort() # Sorts the list in ascending order
my_list.reverse() # Reverses the order of the list
my_list.sorted() # Returns a sorted list without modifying the original list(Temp changes)
print(sorted(my_list)) # Alternative to the above
print(my_list)

