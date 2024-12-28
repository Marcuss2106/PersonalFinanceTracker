import csv

class TransactionManager:
    def __init__(self):
        pass

    def addTransaction(self, transaction, fileHandler):
        fileHandler.writeTransaction(transaction)