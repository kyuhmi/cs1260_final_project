from typing import List

from src.order_item import OrderItem

class Department:
    """Class to represent departments, and their associated inventory."""
    def __init__(self, name: str, inventory: List[OrderItem] = None):
        self.name = name
        self.inventory = inventory if inventory is not None else []

    def __str__(self):
        return self.name