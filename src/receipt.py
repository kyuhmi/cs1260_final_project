from itertools import count

from src.customer import Customer
from src.department import Department
from src.order_item import OrderItem

import datetime

class Receipt:
    def __init__(self, department: Department, item_quantities: dict[OrderItem, int], customer: Customer):
        self.item_quantities = item_quantities
        self.department = department
        self.customer = customer
        self.timestamp = datetime.datetime.now()

    def write_to_file(self, filepath: str):
        pass

    def __str__(self):
        build_str = f"Customer: {self.customer}\nDepartment: {self.department}\n{self.timestamp.strftime("%Y-%m-%d %H:%M:%S")}"
        build_str += "\n================="
        cost_acc = 0.0
        for item, quantity in self.item_quantities.items():
            cost = item.price * quantity
            build_str += f"\n{item.name} x {quantity} = ${cost:.2f}"
            cost_acc += cost
        build_str += "\n================="
        build_str += f"\nTotal: ${cost_acc:.2f}"
        return build_str