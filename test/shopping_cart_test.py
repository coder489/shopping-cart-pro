import datetime
import time

from app.shopping_cart import to_usd, sales_tax, total, selected_products, subtotal

def test_to_usd():
    result = to_usd(70.6)
    assert result == "$70.60"

    result = to_usd(70.389394)
    assert result == "$70.39"

    result = to_usd(70.8)
    assert result == "$70.80"

def test_sales_tax():
    result = sales_tax(10)
    assert result == 0.875

def test_total():
    result = total(10)
    assert result == 10.875


def test_selected_products():
    test_products = [
    {"id":1, "name": "Chocolate Sandwich Cookies", "department": "snacks", "aisle": "cookies cakes", "price": 3.50},
    {"id":2, "name": "All-Seasons Salt", "department": "pantry", "aisle": "spices seasonings", "price": 4.99},
    {"id":3, "name": "Robust Golden Unsweetened Oolong Tea", "department": "beverages", "aisle": "tea", "price": 2.49}
    ]
    result = selected_products(test_products)
    assert result == {"...Chocolate Sandwich Cookies $3.50"
                        "...All-Seasons Salt $4.99"
                    "...Robust Golden Unsweetened Oolong Tea $2.49"}



