username = input("Enter username: ")
password = input("Enter password: ")

def account_creation(username, password):
    if len(username) < 6:
        print("Username must be at least 6 characters long")
    if len(password) < 8:
        print("Password must be at least 8 characters long")