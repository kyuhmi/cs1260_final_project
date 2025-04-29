class OrderItem:
    """Class to represent order items"""
    def __init__(self, name: str, price: float):
        self.name = name
        self.price = price

    def __str__(self):
        return f"{self.name} - ${self.price:.2f} each"