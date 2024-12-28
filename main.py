import Menu
from FileHandler import FileHandler
from TransactionManager import TransactionManager
from Transaction import Transaction
from decimal import Decimal

def main():
    menu = Menu()
    tm = TransactionManager()
    fh = FileHandler()
    choice = menu.choice()
    if choice == 1:
        category = tm.addTransactionCategory()
        type = tm.addTransactionType()
        amount = tm.addTransactionAmount()
        description = tm.AddTransactionDescription()
        transaction = Transaction(category, type, amount, description)
        tm.addTransaction(transaction, fh)
        


main()

if __name__ == "__main__":
    main()