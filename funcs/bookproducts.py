class Product:
    def __init__(self, name, price, quantity):
        self.name = name
        self.price = price
        self.quantity = quantity

    def display_info(self):
        print(f"Name: {self.name}")
        print(f"Price: ${self.price:.2f}")
        print(f"Quantity: {self.quantity}")


class Book(Product):
    def __init__(self, name, price, quantity, author):
        super().__init__(name, price, quantity)
        self.author = author

    def read(self):
        print(f"Book title: {self.name}")
        print(f"Author: {self.author}")
        self.display_info()
