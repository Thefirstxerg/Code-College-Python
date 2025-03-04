# 10-11. Favorite Number: Write a program that prompts for the user’s favorite
# number. Use json.dumps() to store this number in a file. Write a separate program that reads in this value and prints the message “I know your favorite
# number! It’s _____.”
# 10-12. Favorite Number Remembered: Combine the two programs you wrote in
# Exercise 10-11 into one file. If the number is already stored, report the favorite
# number to the user. If not, prompt for the user’s favorite number and store it in a
# file. Run the program twice to see that it works.
# 10-13. User Dictionary: The remember_me.py example only stores one piece of
# information, the username. Expand this example by asking for two more pieces
# of information about the user, then store all the information you collect in a
# dictionary. Write this dictionary to a file using json.dumps(), and read it back
# in using json.loads(). Print a summary showing exactly what your program
# remembers about the user.
# 10-14. Verify User: The final listing for remember_me.py assumes either that the
# user has already entered their username or that the program is running for the
# first time. We should modify it in case the current user is not the person who last
# used the program.
# Before printing a welcome back message in greet_user(), ask the user if
# this is the correct username. If it’s not, call get_new_username() to get the correct
# username.


from pathlib import Path
import json

# Function to prompt the user for their information and store it in a file
def get_user_info():
    username = input("What is your name? ")  # Ask the user for their name
    favorite_number = input("What is your favorite number? ")  # Ask the user for their favorite number
    favorite_color = input("What is your favorite color? ")  # Ask the user for their favorite color
    user_info = {
        "username": username,
        "favorite_number": favorite_number,
        "favorite_color": favorite_color
    }
    path = Path("user_info.json")  # Define the path to the file where the information will be stored
    with open(path, "w") as file:  # Open the file in write mode
        json.dump(user_info, file)  # Store the information in the file using json.dump()
    return user_info  # Return the user information

# Function to read the user information from the file
def read_user_info():
    path = Path("user_info.json")  # Define the path to the file where the information is stored
    if path.exists():  # Check if the file exists
        with open(path, "r") as file:  # Open the file in read mode
            user_info = json.load(file)  # Load the information from the file using json.load()
        return user_info  # Return the user information
    else:
        return None  # Return None if the file does not exist

# Function to verify if the current user is the same as the stored user
def verify_user(user_info):
    is_correct_user = input(f"Is this your username: {user_info['username']}? (yes/no) ")
    if is_correct_user.lower() == 'yes':
        return True
    else:
        return False

# Main function to check if the user information is already stored and print appropriate messages
def main():
    user_info = read_user_info()  # Read the user information from the file
    if user_info:  # If the information is found
        if verify_user(user_info):  # Verify if the current user is the same as the stored user
            print(f"I know you! Your name is {user_info['username']}, your favorite number is {user_info['favorite_number']}, and your favorite color is {user_info['favorite_color']}.")  # Print the user information
        else:
            user_info = get_user_info()  # Prompt the user for their information
            print(f"Your information has been stored: {user_info}")  # Inform the user that the information has been stored
    else:
        user_info = get_user_info()  # Prompt the user for their information
        print(f"Your information has been stored: {user_info}")  # Inform the user that the information has been stored

# Check if the script is being run directly (not imported as a module)
if __name__ == "__main__": 
    main()  # Call the main function

