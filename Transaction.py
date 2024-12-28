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

    @property
    def category(self):
        return self._category
    
    @category.setter
    def category(self, category):
        self._category = category

    @property
    def type(self):
        return self._type
    
    @type.setter
    def type(self, type):
        self._type = type

    @property
    def amount(self):
        return self._amount
    
    @amount.setter
    def amount(self, amount):
        self._amount = amount

    @property
    def description(self):
        return self._description
    
    @description.setter
    def description(self, description):
        self._description = description