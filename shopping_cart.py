import datetime
import time

from dotenv import load_dotenv
import os

load_dotenv() #> loads contents of the .env file into the script's environment



products = [
    {"id":1, "name": "Chocolate Sandwich Cookies", "department": "snacks", "aisle": "cookies cakes", "price": 3.50},
    {"id":2, "name": "All-Seasons Salt", "department": "pantry", "aisle": "spices seasonings", "price": 4.99},
    {"id":3, "name": "Robust Golden Unsweetened Oolong Tea", "department": "beverages", "aisle": "tea", "price": 2.49},
    {"id":4, "name": "Smart Ones Classic Favorites Mini Rigatoni With Vodka Cream Sauce", "department": "frozen", "aisle": "frozen meals", "price": 6.99},
    {"id":5, "name": "Green Chile Anytime Sauce", "department": "pantry", "aisle": "marinades meat preparation", "price": 7.99},
    {"id":6, "name": "Dry Nose Oil", "department": "personal care", "aisle": "cold flu allergy", "price": 21.99},
    {"id":7, "name": "Pure Coconut Water With Orange", "department": "beverages", "aisle": "juice nectars", "price": 3.50},
    {"id":8, "name": "Cut Russet Potatoes Steam N' Mash", "department": "frozen", "aisle": "frozen produce", "price": 4.25},
    {"id":9, "name": "Light Strawberry Blueberry Yogurt", "department": "dairy eggs", "aisle": "yogurt", "price": 6.50},
    {"id":10, "name": "Sparkling Orange Juice & Prickly Pear Beverage", "department": "beverages", "aisle": "water seltzer sparkling water", "price": 2.99},
    {"id":11, "name": "Peach Mango Juice", "department": "beverages", "aisle": "refrigerated", "price": 1.99},
    {"id":12, "name": "Chocolate Fudge Layer Cake", "department": "frozen", "aisle": "frozen dessert", "price": 18.50},
    {"id":13, "name": "Saline Nasal Mist", "department": "personal care", "aisle": "cold flu allergy", "price": 16.00},
    {"id":14, "name": "Fresh Scent Dishwasher Cleaner", "department": "household", "aisle": "dish detergents", "price": 4.99},
    {"id":15, "name": "Overnight Diapers Size 6", "department": "babies", "aisle": "diapers wipes", "price": 25.50},
    {"id":16, "name": "Mint Chocolate Flavored Syrup", "department": "snacks", "aisle": "ice cream toppings", "price": 4.50},
    {"id":17, "name": "Rendered Duck Fat", "department": "meat seafood", "aisle": "poultry counter", "price": 9.99},
    {"id":18, "name": "Pizza for One Suprema Frozen Pizza", "department": "frozen", "aisle": "frozen pizza", "price": 12.50},
    {"id":19, "name": "Gluten Free Quinoa Three Cheese & Mushroom Blend", "department": "dry goods pasta", "aisle": "grains rice dried goods", "price": 3.99},
    {"id":20, "name": "Pomegranate Cranberry & Aloe Vera Enrich Drink", "department": "beverages", "aisle": "juice nectars", "price": 4.25}
] # based on data from Instacart: https://www.instacart.com/datasets/grocery-shopping-2017


tax_rate = float(os.environ.get("TAX_RATE"))


def to_usd(my_price):
    """
        Source: https://github.com/prof-rossetti/intro-to-python/blob/master/notes/python/datatypes/numbers.md#formatting-as-currency
    """
    return f"${my_price:,.2f}" 

def tax(pre_tax_amount):
    post_tax_amount = pre_tax_amount * tax rate
    return post_tax_amount

def current_time():
    t = time.localtime()                
    time = time.strftime("%I:%M %p", t) #Code from https://www.programiz.com/python-programming/datetime/current-datetime
    return time                         #Time format was edited by me to make it more readable to the user


product_all_id = []

x = 0

while x < len(products):
    dictionary = products[x]
    product_all_id.append(dictionary["id"])
    x = x+1


#### CASHIER INPUT ####


purchased_products = []
cashier_input = ""


while True:
    cashier_input = input("Please input a product identifier: ")
    if cashier_input == "DONE":
        break
    elif int(cashier_input) in product_all_id:
        matching_products = [item for item in products if item["id"] == int(cashier_input)]
        purchased_products.append(matching_products[0])
    else:
        print("Product not found.")


#### RECEIPT ####

## HEADER ##

print("---------------------------------")
print("Basque Country Groceries")
print("www.basque-country-groceries.com")
print("---------------------------------")




print("---------------------------------")
print(f"CHECKOUT AT: {str(datetime.date.today())} {current_time}")
print("---------------------------------")


## PRODUCTS ##

print("SELECTED PRODUCTS:")

#y=0
#
#while y < len(purchased_products):
#    dictionary = purchased_products[y]
#    print("..." + str(dictionary["name"]) + " ($" + str(dictionary["price"]) + ")" )
#    y = y + 1

subtotal = 0

for each_product in purchased_products:
    print("..." + str(each_product["name"]) + " " + to_usd(each_product["price"]))
    subtotal = subtotal + each_product["price"]


## PRINT, SUBTOTAL, TAX, AND TOTAL ##

#Desired Output:
#> ---------------------------------
#> SUBTOTAL: $61.24
#> TAX: $5.35
#> TOTAL: $66.59
#> ---------------------------------


### TAX ###

def sales_tax(subtotal):
    return subtotal*tax_rate

tax = sales_tax(subtotal)


### TOTAL ###

sum =  subtotal + tax


print("---------------------------------")
print("SUBTOTAL: " + to_usd(subtotal))
print("TAX: " + to_usd(tax))
print("TOTAL: " + to_usd(sum))
print("---------------------------------")


## FINAL THANKS ##

#Desired Output:
#> THANKS, SEE YOU AGAIN SOON!
#> ---------------------------------

print("ESKERRIK ASKO! (THANK YOU!) SEE YOU AGAIN SOON!")
print("---------------------------------")



