# transaction.py

import json

class Transaction:
    def __init__(self, date, amount, category, description):
        self.date = date
        self.amount = amount
        self.category = category
        self.description = description

    def __repr__(self):
        return f"Transaction({self.date}, {self.amount}, {self.category}, {self.description})"

class FinanceTracker:
    def __init__(self):
        self.transactions = []

    def add_transaction(self, transaction):
        self.transactions.append(transaction)

    def get_transactions(self):
        return self.transactions

    def save_to_file(self, filename):
        with open(filename, 'w') as f:
            json.dump([t.__dict__ for t in self.transactions], f)

    def load_from_file(self, filename):
        with open(filename, 'r') as f:
            transactions_data = json.load(f)
            self.transactions = [Transaction(**data) for data in transactions_data]
