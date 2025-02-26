# If statements, Booleans and conditional tests

cars = ['audi', 'bmw', 'subaru', 'toyota']
for car in cars:
    if car == 'bmw':
        print(car.upper())
    else:
        print(car.title())

# Conditional tests
car = 'bmw'     
print(car == 'bmw') # True
print(car == 'audi') # False

# Inequality
requested_topping = 'mushrooms'
if requested_topping != 'anchovies':
    print("Hold the anchovies!")

# Numerical comparisons
age = 18
print(age == 18) # True
print(age < 21) # True
print(age <= 21) # True
print(age > 21) # False
print(age >= 21) # False


# Multiple conditions
age_0 = 22
age_1 = 18
print(age_0 >= 21 and age_1 >= 21) # False
print(age_0 >= 21 or age_1 >= 21) # True
print(age_0 >= 21 and age_1 >= 21) # True


# Checking whether a value is in a list 
requested_toppings = ['mushrooms', 'onions', 'pineapple']
print('mushrooms' in requested_toppings) # True
print('pepperoni' in requested_toppings) # False

# Checking whether a value is not in a list
banned_users = ['andrew', 'carolina', 'david']
user = 'marie'
if user not in banned_users:
    print(user.title() + ", you can post a response if you wish.")


# Boolean expressions
game_active = True
can_edit = False


# If statements
age = 19
if age >= 18:
    print("You are old enough to vote!")
    print("Have you registered to vote yet?")
else:
    print("Sorry, you are too young to vote.")
    print("Please register to vote as soon as you turn 18!")


# If-elif-else chain
age = 12
if age < 4:
    print("Your admission cost is $0.")
elif age < 18:
    print("Your admission cost is $25.")
else:
    print("Your admission cost is $40.")


# Multiple elif blocks
age = 12
if age < 4:
    price = 0
elif age < 18:
    price = 25
elif age < 65:
    price = 40
else:
    price = 20
print("Your admission cost is $" + str(price) + ".")





# Own example: Cycles through a list of moods and prints a statement based on the mood
moods = ['happy', 'sad', 'angry', 'excited', 'tired', 'bored', 'hungry', 'confused', 'anxious', 'stressed']
for mood in moods:
    if 'happy' in mood:
        print("I am happy!")
    elif 'sad' in mood:
        print("I am sad.")
    elif 'angry' in mood:
        print("I am angry.")
    elif 'excited' in mood:
        print("I am excited!")
    elif 'tired' in mood:
        print("I am tired.")
    elif 'bored' in mood:
        print("I am bored.")
    elif 'hungry' in mood:
        print("I am hungry.")
    elif 'confused' in mood:
        print("I am confused.")
    elif 'anxious' in mood:
        print("I am anxious.")
    elif 'stressed' in mood:
        print("I am stressed.")
    else:
        print("I am feeling fine.")