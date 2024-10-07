name = "Snack Wagon"
sales_tax = 0.07
cart = {}


menu = {
    "sku1": {
        "name": "Chicken Burger",
        "price": 4.50
    },

    "sku2": {
        "name": "Cheese Burger",
        "price": 5.00
    },

    "sku3": {
        "name": "Milkshake",
        "price": 3.50
    },

    "sku4": {
        "name": "Fries",
        "price": 2.30
    },

    "sku5": {
        "name": "Sandwich",
        "price": 3.50
    },

    "sku6": {
        "name": "Ice Cream",
        "price": 1.99
    },

    "sku7": {
        "name": "Coca Cola",
        "price": 1.00
    },

    "sku8": {
        "name": "Cookie",
        "price": 2.15
    },

    "sku9": {
        "name": "Brownie",
        "price": 2.50
    },

    "sku10": {
        "name": "Sauce",
        "price": 0.20
    },

}

menu_actions = {
    "1": "Add a new menu item to cart",
    "2": "Remove an item from the cart",
    "3": "Modify a cart item's quantity",
    "4": "View cart",
    "5": "Checkout",
    "6": "Exit",
}

def display_menu():
    print("\n***MENU***\n")
    for key, value in menu.items():
        if len(key) > 4:
                menu_number = key[-2:]

        else:
            menu_number = key[-1]

        menu_name = menu [key] ['name']
        menu_price = menu [key] ['price']

        print(f"{menu_number}: {menu_name} {menu_price}")

def add_to_cart(sku, quantity = 1):
    if sku in menu:
        if sku in cart:
            cart[sku] += quantity
        else:
            cart[sku] = quantity
        print(f"\nAdded ", {quantity}," of ", {menu[sku]['name']}, " to the cart.")

def remove_from_cart(sku):
    if sku in cart:
        removed_val = cart.pop(sku)
        print(f"\nRemoved, {removed_val['name']} from the cart")
    else:
        print("\nThis item does not exist in the cart\n")

def modify_cart(sku, quantity = 1):
    if sku in cart:
        if quantity > 0:
            cart[sku] = quantity
        elif quantity <= 0:
            remove_from_cart(sku)
        print(f"\nModified, {menu[sku]['name']} quantity has been changed to, {quantity} in the cart\n")
    else:
        print("\nThis item is not available in the cart")

def view_cart():
    print("****Cart Contents****")
    subtotal = 0.00
    for sku in cart:
        if sku in menu:
            quantity = cart[sku]
            subtotal += menu[sku]["price"] * quantity
            print(f"{quantity} x {menu[sku]['name']}")
        tax = subtotal * sales_tax
        total = subtotal + tax
        print(f"Total: £", round(total, 2))
        print("\n")

def checkout():
    print("****Checkout****")
    view_cart()
    print("\nYour order has been submitted")

def get_sku_and_quantity(sku, quantity_prompt = None):
    sku_number = input("Please enter the SKU number")
    sku_number = f"sku{sku_number}"
    if quantity_prompt:
        quantity = input("Please enter the quantity ")
        if not quantity.isdigit():
            quantity = 1
        quantity = int(quantity)

        return sku_number, quantity
    else:
        return sku_number

def app_loop():
    print(f"***** Welcome to {name}! *****")
    ordering = True
    while ordering:
        print("\n**** Ordering Actions ****\n")
        for number in menu_actions:
            description = menu_actions[number]
            print(f"{number} {description}")
        action_number = input("Which action would you like to do? ")
        if action_number == "1":
            display_menu()
            sku = "Please enter the SKU number for the menu item you want "
            quantity_prompt = input("Please enter the quantity ")
            ordered_sku, quantity = get_sku_and_quantity(sku, quantity_prompt)
            add_to_cart(ordered_sku, quantity)

        if action_number == "2":
            display_menu()
            sku_prompt = "Please enter the SKU number for the menu item"
            item_sku = get_sku_and_quantity(sku_prompt)
            remove_from_cart(item_sku)

        if action_number == "3":
            display_menu()
            sku, quantity = get_sku_and_quantity(sku, quantity)
            modify_cart(sku, quantity)

        if action_number == "4":
            view_cart()

        if action_number == "5":
            checkout()
            ordering = False
        if action_number == "6":
            ordering = False
        else:
            print("This is an invalid input, please try again")


app_loop()