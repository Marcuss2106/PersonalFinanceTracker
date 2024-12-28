from FileHandler import FileHandler
from TransactionManager import TransactionManager
from Transaction import Transaction
from decimal import Decimal
from datetime import datetime

tm = TransactionManager()
fh = FileHandler()

def test_createTransaction():
    category = "Groceries"
    type = "Expense"
    amount = Decimal("13.12")
    description = "Apples"
    date = datetime.now()
    transaction = Transaction(category, type, amount, description)
    assert str(transaction) == f"{date.isoformat(timespec="seconds")} Groceries Expense — $13.12, Apples"

def test_writeTransaction():
    category = "Groceries"
    type = "Expense"
    amount = Decimal("13.12")
    description = "Apples"
    date = datetime.now()
    transaction = Transaction(category, type, amount, description)
    tm.addTransaction(transaction, fh)
    assert fh.readRecentTransaction() == ({"category": transaction.category,
                              "type": transaction.type,
                              "description": transaction.description,
                              "amount": str(transaction.amount),
                              "date": transaction.date.isoformat(timespec="seconds")})
