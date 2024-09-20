class Pizza:
    def __init__(self, size, name):
        self.size = size
        self.name = name
        
class Customer:
    def __init__(self, name, address):
        self.name = name
        self.address = address
        
class Order:
    def __init__(self, customer, pizzas):
        self.customer = customer
        self.pizzas = pizzas
    

customer1 = Customer("Mārtiņš", "Talsi, Skaista iela 1")
customer2 = Customer("Anna", "Rīga, Programmētāju iela 1010")

pizza1 = Pizza(30, "Margarita")
pizza2 = Pizza(20, "Salami")
pizza3 = Pizza(30, "Con Verdure")

order1 = Order(customer1, [pizza1, pizza2])
order2 = Order(customer2, [pizza3])

print(f"{order1.customer.name} uz adresi {order1.customer.address} pasutīja sekojošas picas:")
for pizza in order1.pizzas:
    print(f"{pizza.name}, {pizza.size}cm")
