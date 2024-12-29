from FileHandler import FileHandler
from TransactionManager import TransactionManager
from Transaction import Transaction
from decimal import Decimal
from datetime import datetime

tm = TransactionManager()
fh = FileHandler(tm)

category = "Groceries"
type = "Expense"
amount = Decimal("13.12")
description = "Apples"
date = datetime.now()

def test_createTransaction():
    transaction = Transaction(category, type, amount, description)
    assert str(transaction) == f"{date.isoformat(timespec="seconds")} Groceries Expense — $13.12, Apples"

def test_writeAndReadTransaction():
    transaction = Transaction(category, type, amount, description)
    tm.addTransactionToFile(transaction, fh)
    tm.addTransactionToList(transaction)
    assert fh.readRecentTransaction() == ({"_category": transaction.category,
                              "_type": transaction.type,
                              "_description": transaction.description,
                              "_amount": transaction.amount,
                              "_date": transaction.date})
    assert fh.readRecentTransaction() == tm.transactions[-1]