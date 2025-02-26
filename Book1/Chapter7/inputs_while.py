# Inputs and while Loops 
message = input("Tell me something, and I will repeat it back to you: ")
print(message)

name = input("Please enter your name: ")
print("Hello, " + name + "!")
age = input("How old are you? ")
age = int(age)
if age >= 18:
    print("You are an adult.")
else:
    print("You are a minor.")


# Using the modulo operator
number = input("Enter a number, and I'll tell you if it's even or odd: ")
number = int(number)
if number % 2 == 0: # Mod operator returns the remainder of a division
    print("The number " + str(number) + " is even.")
else:
    print("The number " + str(number) + " is odd.")



# While Loops
current_number = 1
while current_number <= 5:
    print(current_number)
    current_number += 1

health = 100
while health > 0:
    print("You are still alive.")
    health -= 10
print("You are dead.")