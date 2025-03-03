#9.3 User class

class user:
    def __init__(self, first_name, last_name, username, email, location):
        self.first_name = first_name
        self.last_name = last_name
        self.username = username
        self.email = email
        self.location = location

    def describe_user(self):
        print(f"\n{self.first_name} {self.last_name}")
        print(f"Username: {self.username}")
        print(f"Email: {self.email}")
        print(f"Location: {self.location}")

    def greet_user(self):
        print(f"\nWelcome back, {self.username}!")


user.profile = user('john', 'doe', 'johndoe', "johndoe@gmail.com", "Pretoria")
user.profile.describe_user()
user.profile.greet_user()

user.profile = user('jane', 'doe', 'janedoe', "janedoe@gmail.com", "Johannesburg")
user.profile.describe_user()
user.profile.greet_user()

user.profile = user(input("Enter a first name: "), input("Enter a last name: "), input("Enter a username: "), input("Enter an email: "), input("Enter a location: "))
user.profile.describe_user()
user.profile.greet_user()