class Customer:
    """
    Represents a customer with a name.
    """
    def __init__(self, name: str):
        """
        Initializes a Customer object.

        Args:
            name (str): The name of the customer.
        """
        self.name = name

    def __str__(self):
        """
        Returns the name of the customer as a string.

        Returns:
            str: The name of the customer.
        """
        return self.name
