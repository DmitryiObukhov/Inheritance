from funcs.restaurant import Restaurant, FastFood

menu = {
    'burger': {'price': 5, 'quantity': 10},
    'pizza': {'price': 10, 'quantity': 20},
    'drink': {'price': 1, 'quantity': 15}
}

mc = FastFood('McDonalds', 'Fast Food', menu, True)
order_items = {'burger': 3, 'pizza': 1, 'drink': 3}
mc.order(order_items)
