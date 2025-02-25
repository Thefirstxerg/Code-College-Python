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



# 3-8. Seeing the World: Think of at least five places in the world you’d like
# to visit.
# • Store the locations in a list. Make sure the list is not in alphabetical order.
# • Print your list in its original order. Don’t worry about printing the list neatly;
# just print it as a raw Python list.
# • Use sorted() to print your list in alphabetical order without modifying the
# actual list.
# • Show that your list is still in its original order by printing it.
# • Use sorted() to print your list in reverse-alphabetical order without changing the order of the original list.
# • Show that your list is still in its original order by printing it again.
# • Use reverse() to change the order of your list. Print the list to show that its
# order has changed.
# • Use reverse() to change the order of your list again. Print the list to show
# it’s back to its original order.
# • Use sort() to change your list so it’s stored in alphabetical order. Print the
# list to show that its order has been changed.
# • Use sort() to change your list so it’s stored in reverse-alphabetical order.
# Print the list to show that its order has changed

places = ["Paris", "New York", "Tokyo", "Cape Town", "London"]
print(places)
print(sorted(places))
print(places)
print(sorted(places.reverse()))
print(places)
places.reverse()
print(places)
places.sort()
print(places)
places.sort(reverse=True)   
print(places)


