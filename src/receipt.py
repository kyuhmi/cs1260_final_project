from itertools import count

from src.customer import Customer
from src.department import Department
from src.order_item import OrderItem

import datetime

class Receipt:
    """
    Represents a receipt for a purchase made by a customer at a department.

    Attributes:
        item_quantities (dict[OrderItem, int]): A dictionary mapping OrderItem objects to the quantity purchased.
        department (Department): The department where the purchase was made.
        customer (Customer): The customer who made the purchase.
        timestamp (datetime): The date and time the receipt was generated.
    """
    def __init__(self, department: Department, item_quantities: dict[OrderItem, int], customer: Customer):
        """
        Initializes a new Receipt object.

        Args:
            department (Department): The department where the purchase was made.
            item_quantities (dict[OrderItem, int]): A dictionary mapping OrderItem objects to the quantity purchased.
            customer (Customer): The customer who made the purchase.
        """
        self.item_quantities = {k:v for k, v in item_quantities.items()}
        self.department = department
        self.customer = customer
        self.timestamp = datetime.datetime.now()

    def __str__(self):
        """
        Returns a string representation of the receipt.

        The string includes the customer, department, timestamp,
        a list of items purchased with their quantities and costs, and the total cost.

        Returns:
            str: A string representation of the receipt.
        """
        build_str = f"Customer: {self.customer}\nDepartment: {self.department}\n{self.timestamp.strftime("%Y-%m-%d %H:%M:%S")}"
        build_str += "\n================="
        cost_acc = 0.0
        for item, quantity in self.item_quantities.items():
            cost = item.price * quantity
            build_str += f"\n{item.name} ({quantity}) = ${cost:.2f}"
            cost_acc += cost
        build_str += "\n================="
        build_str += f"\nTotal: ${cost_acc:.2f}"
        return build_str
