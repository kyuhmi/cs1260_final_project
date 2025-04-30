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

    def calculate_total_cost(self):
        """Calculates the total cost of all items in the receipt.

        Returns:
            float: The total cost of the receipt.
        """
        return sum(item.price * quantity for item, quantity in self.item_quantities.items())

    def __str__(self):
        """
        Returns a string representation of the receipt.

        The string includes the customer, department, timestamp,
        a list of items purchased with their quantities and costs, and the total cost.

        Returns:
            str: A string representation of the receipt.
        """
        timestamp_str = self.timestamp.strftime("%Y-%m-%d %H:%M:%S")
        sorted_items = sorted(self.item_quantities.items(), key=lambda x: x[0].name)
        item_strings = [f"\n{item.name} ({quantity}) = ${item.price * quantity:.2f}"
                        for item, quantity in sorted_items]
        total_cost = self.calculate_total_cost()

        return (f"Customer: {self.customer}\n" +
                f"Department: {self.department}\n" +
                f"{timestamp_str}\n" +
                "=================" +
                "".join(item_strings) +
                "\n=================\n" +
                f"Total: ${total_cost:.2f}")
