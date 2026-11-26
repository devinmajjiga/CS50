menu = {
    "Baja Taco": 4.25,
    "Burrito": 7.50,
    "Bowl": 8.50,
    "Nachos": 11.00,
    "Quesadilla": 8.50,
    "Super Burrito": 8.50,
    "Super Quesadilla": 9.50,
    "Taco": 3.00,
    "Tortilla Salad": 8.00
}
print("Welcome to Felipe's Taqueria. What would you like to order.")
price = 0
while True:
    try:
        food = input("Item: ")
    except (KeyboardInterrupt, EOFError):
        pass
        break
    food = food.title()
    food = food.strip()
    try:
        if food in menu.keys():
            item_price = menu[food]
            price = price + item_price
            print(f"Total: ${price:.2f}")
    except (KeyError):
        pass

