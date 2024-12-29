import csv
import datetime
from decimal import Decimal
from TransactionManager import TransactionManager

class FileHandler:
    def __init__(self, transactionManager):
        self.FIELDNAMES = ["category","type","description","amount","date"]
        self.TRANSACTIONFILE  = "transactions.csv"
        self.tm = transactionManager
        with open(self.TRANSACTIONFILE) as transactionFile:
            reader = csv.DictReader(transactionFile)
            if reader:
                for row in reader:
                    row["amount"] = Decimal(row["amount"])
                    row["date"] = datetime.datetime.fromisoformat(row["date"])
                    self.tm.addTransactionToList(row)

    def writeTransaction(self, transaction):
        with open(self.TRANSACTIONFILE,'a', newline='') as transactionFile:
            writer = csv.DictWriter(transactionFile, fieldnames=self.FIELDNAMES)
            writer.writerow({"category": transaction.category,
                              "type": transaction.type,
                              "description": transaction.description,
                              "amount": str(transaction.amount),
                              "date": transaction.date.isoformat(timespec="seconds")})
                 
    def readRecentTransaction(self):
        return self.tm.transactions[-1]