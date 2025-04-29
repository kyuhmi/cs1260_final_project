from typing import Any, List

from src.order_item import OrderItem

def get_option_from_user(menu_header: str, options_dict: dict[int, Any]):
    """Function to print out a menu with options for a user to pick from."""
    print(f"=== {menu_header} ===")
    ordered_options = sorted(options_dict.items())
    while True:
        for key, value in ordered_options:
            print(f"  {key}. {value}")

        # get input from user
        try:
            user_input_int = int(input("Enter choice: ").strip())
            if user_input_int not in options_dict.keys():
                print("Invalid option. Try again.")
                continue
            else:
                return options_dict[user_input_int] # validated
        except ValueError:
            print("Could not parse number. Try again.")
            continue

def get_item_quantity(item: OrderItem):
    while True:
        try:
            quantity = int(input(f"Enter number of {item.name} you want: ").strip())
            if quantity < 0:
                print("Negative numbers are invalid. Try again.")
                continue
            else:
                return quantity
        except ValueError:
            print("Could not parse number. Try again.")

def get_customer_name():
    return input("Enter customer name: ").strip()

def prompt_order_again():
    while True:
        user_input = input("Would you like to make another order? [y/n]: ").strip()
        if user_input.lower() in ["y", "n"]:
            return True if user_input.lower() == "y" else False
        else:
            print("Invalid input. Try again.")

def enumerate_list_to_dict(input_list: List):
    """Function to get an enumerated dictionary (1 indexed) given a list. Integers are keys."""
    return dict(zip(range(1, len(input_list) + 1), input_list))
