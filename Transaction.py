class Transaction:
    def __init__(self, category, type, description, amount, date):
        self.category = category
        self.type = type # income or expense
        self.description = description
        self.amount = amount
        self.date = date
    
    def __str__(self):
        return f"{self.date} {self.category} {self.type} — {self.amount}, {self.description} "