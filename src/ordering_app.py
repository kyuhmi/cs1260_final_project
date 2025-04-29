from typing import List
import json

from menus import get_option_from_user, enumerate_list_to_dict, get_item_quantity
from src.department import Department
from src.order_item import OrderItem

ITEM_SELECTION_END_STR = "Done selecting items"

class OrderingApp:
    def __init__(self):
        self.departments = []
        self.order = dict()

    def application_routine(self):
        department = self.get_department()
        item = None
        item_quantity = 0

        while True:
            item = self.get_item_from_department(department)
            if item is None:
                break # done selecting items

            item_quantity = get_item_quantity(item)
            if item_quantity > 0:
                # non-zero quantity, add quantity to the current count in order
                if item in self.order.keys():
                    self.order[item] = self.order[item] + item_quantity
                else:
                    self.order[item] = item_quantity

        print(self.order)


    def get_department(self):
        return get_option_from_user("Select Department", enumerate_list_to_dict(self.departments))

    @staticmethod
    def get_item_from_department(department: Department):
        item = get_option_from_user("Select Item", OrderingApp.make_department_item_menu_dict(department))
        return item if item is not ITEM_SELECTION_END_STR else None

    @staticmethod
    def make_department_item_menu_dict(department: Department):
        menu_dict = enumerate_list_to_dict(department.inventory)
        menu_dict[len(menu_dict) + 1] = ITEM_SELECTION_END_STR
        return menu_dict

    def load_departments(self, filepaths: List[str]):
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