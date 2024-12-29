from FileHandler import FileHandler
from TransactionManager import TransactionManager
from Transaction import Transaction
from decimal import Decimal
from datetime import datetime
from random import choice, randint

tm = TransactionManager()
fh = FileHandler(tm)

category = ["Groceries", "Rent", "Bill"]
type = ["Expense","Income"]
AMTSTART = 1
AMTEND = 100
description = "_"
date = datetime.now()
NUMBER_TRANSACTIONS = 10

def test_createTransaction():
    for i in range(NUMBER_TRANSACTIONS):
        transaction = Transaction(choice(category), choice(type), randint(AMTSTART, AMTEND), description)
        assert str(transaction) == f"{date.isoformat(timespec="seconds")} {transaction.category} {transaction.type} — ${transaction.amount}, {transaction.description}"

def test_writeAndReadTransaction():
    for i in range(NUMBER_TRANSACTIONS):
        transaction = Transaction(choice(category), choice(type), randint(AMTSTART, AMTEND), description)
        tm.addTransactionToFile(transaction, fh)
        tm.addTransactionToList(transaction)
        assert fh.readRecentTransaction() == ({"_category": transaction.category,
                              "_type": transaction.type,
                              "_description": transaction.description,
                              "_amount": transaction.amount,
                              "_date": transaction.date})
        assert fh.readRecentTransaction() == tm.transactions[-1]

def test_numberTransactions():
    assert len(tm.transactions) == NUMBER_TRANSACTIONS

def test_filterExpenses():
    for transaction in tm.filterExpenses():
        assert transaction["_type"] == "Expense"

def test_filterIncome():
    for transaction in tm.filterIncomes():
        assert transaction["_type"] == "Income"