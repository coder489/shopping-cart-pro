import datetime
import time

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

purchased_products = []
product_all_id = []
tax_rate = 0.0875

def to_usd(my_price):
    """
    Converts a numeric value to usd-formatted string, for printing and display purposes.
    
    Parameters: 
    
        my_price (int or float): a price value that is not formatted like 4000.444444
        
    Source: https://github.com/prof-rossetti/intro-to-python/blob/master/notes/python/datatypes/numbers.md#formatting-as-currency
    """
    return f"${my_price:,.2f}" 

def current_time():
    """
    Used to get the current time, format it, and then return it.
        
    Source: https://www.programiz.com/python-programming/datetime/current-datetime
    """
    t = time.localtime()                
    time_now = time.strftime("%I:%M %p", t) 
    return time_now

def selected_products(product_list):
    """
    Loops through, compiles and prints a formatting element, the name of, and price of all of the items in a list of dictionaries.

    Parameters:

        product_list (list): a list of dictionaries of specified products
    """
    result = ""
    for each_product in product_list:
        result = result + ("..." + str(each_product["name"]) + " " + str(to_usd(each_product["price"]) + "\n")) #found "\n" at https://stackoverflow.com/questions/13872049/print-empty-line/22534622
    return result

def subtotal(product_list):
    """
    Calculates the subtotal of the prices associated with all of the dictionaries in a list of dictionaries.

    Parameters:

        product_list (list): a list of dictionaries of specified products
    """
    subtotal = 0
    for each_product in product_list:
        subtotal = subtotal + float(each_product["price"])
    return subtotal

def sales_tax(total):
    """
    Calculates the tax owed on a given amount.

    Parameters:

    total (float or int): a price value, like 45.6868 or 45
    """
    taxes = total * tax_rate
    return taxes

def total(cost):
    """
    Calculates the total amount owed by adding the total and the tax on that total.

    Parameters:

    cost (float or int): a price value, like 45.6868 or 45
    """
    total_cost = cost + sales_tax(cost)
    return total_cost

def line(symbol):
    """
    Creates a divider out of a specified symbol.
    
    Parameters: 
    
        symbol (str): any symbol that you wish to use repeatedly to form a divider, like "*" or "-"

    """
    return symbol * 50


if __name__ == "__main__":
    ## CASHIER INPUTS (collecting the products)

    x = 0

    while x < len(products):
        dictionary = products[x]
        product_all_id.append(dictionary["id"])
        x = x+1

    while True:
        cashier_input = input("Please input a product identifier: ")
        if cashier_input == "DONE":
            break
        elif int(cashier_input) in product_all_id:
            matching_products = [item for item in products if item["id"] == int(cashier_input)]
            purchased_products.append(matching_products[0])
        else:
            print("Product not found.")

    ## RECEIPT OUTPUT
    
    print("\n")
    print(line("-"))
    print("Basque Country Groceries")
    print("www.basque-country-groceries.com")
    print(line("-"))
    print(f"CHECKOUT AT: {str(datetime.date.today())} {current_time()}")
    print(line("-"))
    print("\n" + "SELECTED PRODUCTS:")
    print(selected_products(purchased_products))
    print(line("-"))
    print(f"SUBTOTAL: {to_usd(subtotal(purchased_products))}")
    print(f"TAX: {to_usd(sales_tax(subtotal(purchased_products)))}")
    print(f"TOTAL: {to_usd(total(subtotal(purchased_products)))}")
    print(line("-"))
    print("ESKERRIK ASKO! (THANK YOU!) SEE YOU AGAIN SOON!")
    print(line("-"))
    print("\n")

