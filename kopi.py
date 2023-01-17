#class language_m(language_malay)


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
#malay version
class Bahasa:
    def __init__(self):
        self.Bahasa = melayu


melayu ='selamat datang ke Richiamocoffee machine!'

print(melayu)

# Ask user for their name
name = input("Boleh saya dapatkan nama anda? \n")

# Ask user for their order
print("encik/cik " + name + " mahu order apa?")

# Print menu options
menu = [
    "Espresso", "Americano", "Cappuccino", "caramello cappuccino", "Hazelnut cappuccino", 
    "Caffe latte", "Caramello latte", "Hazelnut latte", "caffe mochaccino", "white mochaccino", "caffe vanilla"
]
print(menu)

order = input()

# Ask user for the quantity of their order
quantity = int(input("Berapa banyak " + order + " yang anda mahukan?\n"))

# Define a function to calculate the total price of the order
def calculate_total(quantity, price):
    total = quantity * price[order]
    return total
total = calculate_total(quantity, price)

# Ask user if they would like to add more to their order
add_more = input("adakah anda mahu tambah order? (ya/tidak) ")

while add_more == "ya":                                                           
    order = input("encik/cik " + name + " mahu order apa?\n")
    quantity = int(input("Berapa banyak " + order + " yang anda mahukan?\n"))
    total += calculate_total(quantity, price)
    add_more = input("adakah anda mahu tambah order? (ya/tidak) ")       

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
print("Baki anda adalah: " + formatted_change)
