# Inputs and while Loops 
message = input("Tell me something, and I will repeat it back to you: ") # input() function pauses the program and waits for the user
print(message)                                                           # to enter some text. Once the user presses Enter, the input() function
                                                                         # passes that input back to the program. The input is stored in the 
                                                                         # variable message.
name = input("Please enter your name: ")
print("Hello, " + name + "!")
age = input("How old are you? ")
age = int(age) # The int() function converts a string representation of a number to a numerical representation. The same goes for str(), float(), etc.
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
while current_number <= 5: # The while loop runs as long as the condition is true
    print(current_number)
    current_number += 1 # Increments the value of current_number by 1 until it reaches 5


# Own Example: Health Slowly drains until 0 and then prints "You are dead."
health = 100
while health > 0:
    print("You are still alive.")
    health -= 10
print("You are dead.")


# Letting the user choose when to quit
prompt = "\nTell me something, and I will repeat it back to you:"
prompt += "\nEnter 'quit' to end the program. "
message = ""
while message != 'quit': # The loop runs as long as the value of message is not 'quit'
    message = input(prompt)
    if message != 'quit':
        print(message)

