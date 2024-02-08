import datetime
from data import warehouse1, warehouse2
from data1 import stock


def list_items():
    print("Items in Warehouse 1:")
    for item in warehouse1:
        print(f"- {item}")

    print("**************************************************")

    print("Items in Warehouse 2:")
    for item in warehouse2:
        print(f"- {item}")

    total_items_warehouse1 = len(warehouse1)
    total_items_warehouse2 = len(warehouse2)
    print(f"Total items in Warehouse 1: {total_items_warehouse1}")
    print(f"Total items in Warehouse 2: {total_items_warehouse2}")


def search_and_order():
    item_name = input("What is the name of the item? ").lower()
    total_available = 0
    locations = []

    for item in stock:
        if item_name.lower() in f"{item['state']} {item['category']}".lower():
            total_available += 1
            locations.append(f"Warehouse {item['warehouse']} (in stock for {item['date_of_stock']})")

    if total_available == 0:
        print("Amount available: 0")
        print("Location: Not in stock")
    else:
        print(f"Amount available: {total_available}")
        print("Location:")
        for location in locations:
            print(f"- {location}")

        max_avail = max(stock, key=lambda x: x['date_of_stock'])
        if locations.count(max_avail) > 1:
            print(f"Maximum availability: {locations.count(max_avail)} in Warehouse {max_avail['warehouse']}")

    order = input("Would you like to order this item? (y/n) ").lower()

    if order == 'y':
        desired_amount = int(input("How many would you like? "))

        if desired_amount <= total_available:
            print(f"{desired_amount} {item_name} have been ordered.")
        else:
            print("There are not this many available.")
            order_max = input("Would you like to order the maximum available? (y/n) ").lower()

            if order_max == 'y':
                print(f"{total_available} {item_name} have been ordered.")


def browse_category():
    categories = {}
    category_items = {}

    for item in stock:
        category = item['category']
        if category not in categories:
            categories[category] = 0
            category_items[category] = []
        categories[category] += 1
        category_items[category].append(item)

    
    menu = []
    for i, category in enumerate(categories, start=1):
        menu.append((i, category, categories[category]))

    print("Available categories:")
    for i, category, item_count in menu:
        print(f"{i}. {category} ({item_count})")

    category_number = int(input("Type the number of the category to browse: "))

    if 1 <= category_number <= len(menu):
        selected_category = menu[category_number - 1][1]
        print(f"List of {selected_category} available:")
        items_in_category = category_items[selected_category]
        for item in items_in_category:
            print(f"{item['state']} {selected_category}, Warehouse {item['warehouse']}")
    else:
        print("Invalid category number.")


user_name = input("What is your user name? ")
print(f"Hello, {user_name}!")


while True:
    print("\nWhat would you like to do?")
    print("1. List items by warehouse")
    print("2. Search an item and place an order")
    print("3. Browse by category")
    print("4. Quit")

    choice = input("Type the number of the operation: ")

    if choice == '1':
        list_items()
    elif choice == '2':
        search_and_order()
    elif choice == '3':
        browse_category()
    elif choice == '4':
        print(f"\nThank you for your visit, {user_name}!")
        break
    else:
        print("\n**************************************************")
        print("Invalid operation. Please enter a valid option (1, 2, 3, or 4).")
        print("**************************************************")
