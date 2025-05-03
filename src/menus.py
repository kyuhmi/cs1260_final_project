from typing import Any, List

from src.order_item import OrderItem

def get_option_from_user(menu_header: str, options_dict: dict[int, Any]) -> Any:
    """Presents a menu to the user and retrieves their selection.

    Args:
        menu_header: The title of the menu to display.
        options_dict: A dictionary where keys are integer options and values are the
                      corresponding selectable items.

    Returns:
        The value associated with the user's selected option from the options_dict.
    """
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

def get_item_quantity(item: OrderItem) -> int:
    """Prompts the user to enter the quantity of a specific item.

    Args:
        item: The OrderItem object for which the quantity is being requested.

    Returns:
        The validated quantity of the item entered by the user as an integer.
    """
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

def get_customer_name() -> str:
    """Prompts the user to enter the customer's name.

    Returns:
        The validated customer name entered by the user.
    """
    while True:
        name = input("Enter customer name: ").strip()
        if len(name) == 0:
            print("Name must not be blank. Try again.")
        else:
            return name

def prompt_order_again() -> bool:
    """Asks the user if they would like to place another order.

    Returns:
        True if the user wants to place another order, False otherwise.
    """
    while True:
        user_input = input("Would you like to make another order? [y/n]: ").strip()
        # process only first character.
        if user_input[0].lower() in ["y", "n"]:
            return True if user_input[0].lower() == "y" else False
        else:
            print("Invalid input. Try again.")

def enumerate_list_to_dict(input_list: List[Any]) -> dict[int, Any]:
    """Converts a list into a dictionary with enumerated keys. 1-indexed in ascending order of list items.

    Args:
        input_list: The list to be converted.

    Returns:
        A dictionary where the keys are integers starting from 1, and the values
        are the corresponding elements from the input list.
    """
    return dict(zip(range(1, len(input_list) + 1), sorted(input_list)))
