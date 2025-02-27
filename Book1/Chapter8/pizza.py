# Pizza Order Program
def make_pizza(size, *toppings):
    print(f"\nMaking a {size}-inch pizza with the following toppings:")
    if not toppings or toppings[0] == '': # If no toppings are provided, default to plain cheese
        toppings = ['plain cheese']
        print("- Plain cheese")
    else:
        for topping in toppings: # Print each topping that was selected
            print(f"- {topping}")
    print("Your pizza will be ready shortly. Thank you for your order!")

print("Welcome to Python Pizza!")
make_pizza(input("What size pizza do you want?"), input("What toppings would you like?")) # Prompt user for pizza size and toppings
make_pizza(12, 'mushrooms', 'green peppers', 'extra cheese')
make_pizza(18)
print("We hope you enjoy your meal!")