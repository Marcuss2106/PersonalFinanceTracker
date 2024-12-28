import csv
import datetime

class FileHandler:
    def __init__(self):
        self.FIELDNAMES = ["category","type","description","amount","date"]
        self.TRANSACTIONFILE  = "transactions.csv"

    def writeTransaction(self, transaction):
        with open(self.TRANSACTIONFILE,'a') as transactionFile:
            writer = csv.DictWriter(transactionFile, fieldnames=self.FIELDNAMES)
            writer.writerow({"category": transaction.category,
                              "type": transaction.type,
                              "description": transaction.description,
                              "amount": transaction.amount,
                              "date": transaction.date})