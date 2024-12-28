from FileHandler import FileHandler
from TransactionManager import TransactionManager
from Transaction import Transaction
from decimal import Decimal
from datetime import datetime

tm = TransactionManager()
fh = FileHandler()

def test_addTransaction():
    category = "Groceries"
    type = "Expense"
    amount = Decimal("13.12")
    description = "Apples"
    date = datetime.now()
    transaction = Transaction(category, type, amount, description)
    assert str(transaction) == f"{date.isoformat(timespec="seconds")} Groceries Expense — $13.12, Apples"
