class Expense:
    def __init__(self, category, amount, date):
        self.category = category
        self.amount = amount
        self.date = date

    def to_dict(self):
        return {
            "category": self.category,
            "amount": self.amount,
            "date": self.date
        }