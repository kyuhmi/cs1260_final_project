import json
from typing import List

from src.customer import Customer
from src.menus import *
from src.department import Department
from src.order_item import OrderItem
from src.receipt import Receipt

ITEM_SELECTION_END_STR = "Done selecting items"

class OrderingApp:
    """
    A class that simulates a grocery ordering application.

    Attributes:
        departments (List[Department]): A list of departments available in the store.
        item_quantities (dict): A dictionary storing the quantities of each item in the current order.
        receipt_output_file (str): The file path where receipts will be written.
    """
    def __init__(self, receipt_output_file: str = "grocery_orders.txt"):
        """
        Initializes the OrderingApp with an empty list of departments, an empty item quantities dictionary,
        and a specified receipt output file.

        Args:
            receipt_output_file (str, optional): The name of the file to write receipts to.
                Defaults to "grocery_orders.txt".
        """
        self.departments = []
        self.item_quantities = dict()
        self.receipt_output_file = receipt_output_file

    def application_routine(self):
        """
        The main application routine that guides the user through the ordering process.
        It allows the user to select departments, add items to their order, specify quantities,
        and finalize the order, generating a receipt.  The routine loops, allowing multiple orders
        until the user quits.
        """
        if len(self.departments) == 0:
            print("No departments available.")
            return

        while True:
            department = self.get_department_from_user()

            while True:
                item = self.get_item_from_department(department)
                if item is None:
                    break # done selecting items

                item_quantity = get_item_quantity(item)
                if item_quantity > 0:
                    # non-zero quantity, add quantity to the current count in order
                    if item in self.item_quantities.keys():
                        self.item_quantities[item] = self.item_quantities[item] + item_quantity
                    else:
                        self.item_quantities[item] = item_quantity

            if len(self.item_quantities) == 0:
                print("Order cancelled.")
            else:
                # get customer name and make obj
                customer_name = get_customer_name()
                customer = Customer(customer_name)

                # create receipt
                receipt = Receipt(department, self.item_quantities, customer)

                # print receipt and write it to a file.
                print(f"\n{receipt}\n")
                self.write_to_file(self.receipt_output_file, str(receipt) + "\n\n", True)
                print("Written to file.\n")

            # prompt order again
            if prompt_order_again():
                self.item_quantities.clear()
                continue
            else:
                break

    def get_department_from_user(self):
        """
        Prompts the user to select a department from the available list.

        Returns:
            Department: The department selected by the user.
        """
        return get_option_from_user("Select Department", enumerate_list_to_dict(self.departments))

    @staticmethod
    def get_item_from_department(department: Department):
        """
        Prompts the user to select an item from the given department.

        Args:
            department (Department): The department from which to select an item.

        Returns:
            OrderItem: The item selected by the user, or None if the user is done selecting items.
        """
        item = get_option_from_user("Select Item", OrderingApp.make_department_item_menu_dict(department))
        return item if item is not ITEM_SELECTION_END_STR else None

    @staticmethod
    def make_department_item_menu_dict(department: Department):
        """
        Creates a menu dictionary of items from the given department.

        Args:
            department (Department): The department to create the menu from.

        Returns:
            dict: A dictionary where keys are menu numbers and values are OrderItem objects from the department,
                  plus an option to finish item selection.
        """
        menu_dict = enumerate_list_to_dict(department.inventory)
        menu_dict[len(menu_dict) + 1] = ITEM_SELECTION_END_STR
        return menu_dict

    @staticmethod
    def write_to_file(filepath:str, data:str, append=True):
        """
        Writes the given data to a file.

        Args:
            filepath (str): The path to the file to write to.
            data (str): The data to write to the file.
            append (bool, optional): Whether to append to the file or overwrite it. Defaults to True.

        Returns:
            bool: True if the write was successful, False otherwise.
        """
        try:
            mode = 'a' if append else 'w'
            with open(filepath, mode) as file:
                file.write(data)
            return True
        except Exception as e:
            print(f"Error writing to file: {e}")
            return False

    def load_departments(self, filepaths: List[str]):
        """
        Loads department data from JSON files specified by the given filepaths.

        Args:
            filepaths (List[str]): A list of filepaths to JSON files containing department data.
        """
        if len(filepaths) == 0:
            return # nothing to do

        for filepath in filepaths:
            try:
                with open(filepath, 'r') as file:
                    department_data = json.load(file)

                    # get department name
                    name = department_data.get("name", "Unknown Department")

                    # get inventory items
                    inventory_data = department_data.get("inventory", [])

                    inventory = []
                    for item_data in inventory_data:
                        item_name = item_data.get("name", "Unknown Item")
                        item_price = float(item_data.get("price", 0.0))
                        inventory.append(OrderItem(item_name, item_price))

                    # create and add department
                    department = Department(name, inventory)
                    self.departments.append(department)
            except FileNotFoundError:
                print(f"File not found: {filepath}")
            except json.JSONDecodeError:
                print(f"Warning: Invalid JSON format in file: {filepath}")
            except Exception as e:
                print(f"Error processing file {filepath}: {str(e)}")
