from FileHandler import FileHandler
from TransactionManager import TransactionManager
from Transaction import Transaction
from decimal import Decimal

tm = TransactionManager()
fh = FileHandler()

def test_addTransaction():
    category = "Groceries"
    type = "Expense"
    amount = Decimal("13.12")
    description = "Apples"
    transaction = Transaction(category, type, amount, description)
    assert f"{transaction.category} {transaction.type} — ${transaction.amount}, {transaction.description}" == "Groceries Expense — $13.12, Apples"
    tm.addTransaction(transaction, fh)
