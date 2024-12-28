import datetime
from decimal import Decimal

class Transaction:
    def __init__(self, category, type, amount, description):
        self.category = category
        self.type = type # income or expense
        self.amount = amount
        self.description = description
        self.date = datetime.datetime

    def __str__(self):
        return f"{self.date} {self.category} {self.type} — ${self.amount}, {self.description}"