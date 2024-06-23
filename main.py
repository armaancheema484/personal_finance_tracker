# main.py

from transaction import Transaction, FinanceTracker
from datetime import datetime

def main():
    tracker = FinanceTracker()

    while True:
        print("1. Add Transaction")
        print("2. View Transactions")
        print("3. Save Transactions")
        print("4. Load Transactions")
        print("5. Exit")

        choice = input("Choose an option: ")

        if choice == '1':
            date = input("Enter date (YYYY-MM-DD): ")
            amount = float(input("Enter amount: "))
            category = input("Enter category: ")
            description = input("Enter description: ")
            transaction = Transaction(date, amount, category, description)
            tracker.add_transaction(transaction)
        elif choice == '2':
            for t in tracker.get_transactions():
                print(t)
        elif choice == '3':
            filename = input("Enter filename to save: ")
            tracker.save_to_file(filename)
        elif choice == '4':
            filename = input("Enter filename to load: ")
            tracker.load_from_file(filename)
        elif choice == '5':
            break
        else:
            print("Invalid choice. Try again.")

if __name__ == "__main__":
    main()
