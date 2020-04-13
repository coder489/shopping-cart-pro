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


