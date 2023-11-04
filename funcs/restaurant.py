class Restaurant:
    def __init__(self, name, cuisine, menu):
        self.name = name
        self.cuisine = cuisine
        self.menu = menu


class FastFood(Restaurant):
    def __init__(self, name, cuisine, menu, drive_thru=True):
        super().__init__(name, cuisine, menu)
        self.drive_thru = drive_thru

    def order(self, dishes):
        bill = 0
        for dish, quantity in dishes.items():
            if dish in self.menu:
                dish_price = self.menu[dish]['price']
                dish_quantity = self.menu[dish]['quantity']
                if dish_quantity >= quantity:
                    bill += dish_price * quantity
                    self.menu[dish]['quantity'] -= quantity
                else:
                    print(f"Sorry, we dont have enouh {dish}")
            else:
                print(f"Sorry, {dish} is not on the menu.")
        print(f"Your total bill is ${bill:.2f}")
