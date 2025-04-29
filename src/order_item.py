class OrderItem:
    """
    Represents an item in an order.

    Attributes:
        name (str): The name of the item.
        price (float): The price of the item.
    """
    def __init__(self, name: str, price: float):
        """
        Initializes a new OrderItem object.

        Args:
            name (str): The name of the item.
            price (float): The price of the item.
        """
        self.name = name
        self.price = price

    def __str__(self):
        """
        Returns a string representation of the OrderItem object.

        Returns:
            str: A string representation of the OrderItem object in the format "name - $price each".
        """
        return f"{self.name} - ${self.price:.2f} each"
