from typing import List

from src.order_item import OrderItem

class Department:
    """
    Represents a department within a store, managing its inventory.

    Attributes:
        name (str): The name of the department.
        inventory (List[OrderItem]): A list of OrderItem objects representing the department's inventory.
                                      Defaults to an empty list if no inventory is provided.
    """
    def __init__(self, name: str, inventory: List[OrderItem] = None):
        """
        Initializes a new Department object.

        Args:
            name (str): The name of the department.
            inventory (List[OrderItem], optional): A list of OrderItem objects to initialize the department's inventory.
                                                    Defaults to None, which initializes an empty list.
        """
        self.name = name
        self.inventory = inventory if inventory is not None else []

    def __str__(self):
        """
        Returns the name of the department.

        Returns:
            str: The name of the department.
        """
        return self.name

    def __lt__(self, other: 'Department') -> bool:
        """
        Compares two Department objects based on their names.

        Args:
            other (Department): The other Department object to compare to.

        Returns:
            bool: True if this department's name is less than the other department's name, False otherwise.
        """
        return self.name < other.name
