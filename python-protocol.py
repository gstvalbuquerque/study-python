#IMPLEMENTAÇÃO BÁSICA DO PYTHON PROTOCOL
# PEP 544 https://peps.python.org/pep-0544/

from typing import List, Protocol


class Item(Protocol):
    quantity: float
    price: float

class Product:
    def __init__(self, name: str, quantity: float, price: float):
        self.name = name
        self.quantity = quantity
        self.price = price

class Stock:
    def __init__(self, product_name, quantity, price):
        self.product_name = product_name
        self.quantity = quantity
        self.price = price

def calculate_total(items: List[Product]) -> float:
    return sum([item.quantity * item.price for item in items])
    
def calculate_total_using_protocol(items: List[Item]) -> float:
    return sum([item.quantity * item.price for item in items])
    
product1 = Product('caixa', 2.0, 3.5)
product2 = Product('tampa', 10, 1.99)
stock1 = Stock('bty1', 112, 53.02)
stock2 = Stock('tat1', 56, 25.01)
product_list = [product1, product2]
stock_list = [stock1, stock2]
total_products = calculate_total(product_list)
total_using_protocol_products = calculate_total_using_protocol(product_list)
total_stocks = calculate_total(stock_list)
total_using_protocol_stocks = calculate_total_using_protocol(stock_list)

print(total_products)
print(total_using_protocol_products)

print(total_stocks)
print(total_using_protocol_stocks)
