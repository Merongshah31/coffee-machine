#english + main.py

#dictinory


price = {
    "Espresso": 5.80,
    "Americano": 6.90,
    "Cappuccino": 7.90,
    "caramello cappuccino": 9.00,
    "Hazelnut cappuccino": 9.00,
    "Caffe latte": 7.90,
    "Caramello latte": 9.00,
    "Hazelnut latte": 9.00,
    "caffe mochaccino": 9.00,
    "white mochaccino": 9.00,
    "caffe vanilla": 9.00,
}

currency = "RM"

class Language:
    def __init__(self):
        self.language = english


english ='Welcome to Richiamocoffee machine!'

print(english)

# Ask user for their name
name = input("Can I get your name? \n")




# Ask user for their order
print("What would you like to order, Mr/Ms. " + name + "?")



# Print menu options
menu = [
    "Espresso", "Americano", "Cappuccino", "caramello cappuccino", "Hazelnut cappuccino", 
    "Caffe latte", "Caramello latte", "Hazelnut latte", "caffe mochaccino", "white mochaccino", "caffe vanilla"
]
print(menu)


order = input()


# Ask user for the quantity of their order
quantity = int(input("How many " + order + " would you like?\n"))

# Define a function to calculate the total price of the order


def calculate_total(quantity, price):
    total = quantity * price[order]
    return total
total = calculate_total(quantity, price)

# Ask user if they would like to add more to their order
add_more = input("Would you like to add more to your order? (yes/no) ")

while add_more == "yes":                                                            #loop problem?
    order = input("What would you like to order, Mr/Ms. " + name + "?\n")
    quantity = int(input("How many " + order + " would you like?\n"))
    total += calculate_total(quantity, price)
    add_more = input("Would you like to add more to your order? (yes/no) ")         #continue-the loop

# Print the total cost of the order
print(currency, total)                                                              #problem_decimal

# Ask user for cash
cash = float(input("Enter cash: RM "))

# Calculate change
change = cash - total

# Format change to display as currency value
from decimal import Decimal
value = Decimal(change)
formatted_change = 'RM{:,.2f}'.format(value)
print("Your change is: " + formatted_change)

