# visualization.py

import matplotlib.pyplot as plt
from transaction import FinanceTracker

def plot_expenses(tracker):
    categories = {}
    for t in tracker.get_transactions():
        if t.category in categories:
            categories[t.category] += t.amount
        else:
            categories[t.category] = t.amount

    labels = categories.keys()
    sizes = categories.values()

    plt.pie(sizes, labels=labels, autopct='%1.1f%%')
    plt.title("Expenses by Category")
    plt.show()

if __name__ == "__main__":
    tracker = FinanceTracker()
    filename = input("Enter filename to load: ")
    tracker.load_from_file(filename)
    plot_expenses(tracker)
