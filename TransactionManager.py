from decimal import Decimal

class TransactionManager:
    def __init__(self):
        self.transactions = []

    def addTransactionCategory(self):
        category = input("Category")
        return category
    
    def addTransactionType(self):
        type = input("Type")
        return type

    def addTransactionAmount(self):
        amount = input("Amount")
        return Decimal(amount)
    
    def addTransactionDescription(self):
        description = input("Description")
        return description

    def addTransactionToFile(self, transaction, fileHandler):
        fileHandler.writeTransaction(transaction)

    def addTransactionToList(self, transaction):
        if type(transaction) == dict:
            self.transactions.append(transaction)
        else:
            self.transactions.append(vars(transaction))

    