def load_expenses():
    expenses = []

    with open("expenses.txt", "r") as file:
        for line in file:
            name, amount, category = line.strip().split(",")
            expenses.append({
                "name": name,
                "amount": float(amount),
                "category": category
            })

    return expenses

def save_expenses(expenses):
    with open("expenses.txt", "w") as file:
        for expense in expenses:
            file.write(
                f"{expense['name']},{expense['amount']},{expense['category']}\n"
            )

def add_expense(expenses):
    name = input("Enter expense name: ")

    try:
        amount = float(input("Enter amount: "))
    except ValueError:
        print("Invalid amount! Please enter a number.")
        return

    category = input("Enter category: ")

    expense = {
        "name": name,
        "amount": amount,
        "category": category
    }

    expenses.append(expense)
    save_expenses(expenses)

    print("Expense added successfully!")

def view_expenses(expenses):
    if not expenses:
        print("No expenses found.")
    else:
        for expense in expenses:
            print("Name:", expense["name"])
            print("Amount:", expense["amount"])
            print("Category:", expense["category"])
            print("--------------------")

def total_spent(expenses):
    total = 0

    for expense in expenses:
        total += expense["amount"]

    print(f"Total spent: Rs. {total:.2f}")

def total_by_category(expenses):
    category = input("Enter category: ")
    total = 0

    for expense in expenses:
        if expense["category"].lower() == category.lower():
            total += expense["amount"]

    print(f"Total spent on {category}: Rs. {total:.2f}")

def main():
    expenses = load_expenses()

    while True:
        print("\n===== EXPENSE TRACKER =====")
        print("1. Add Expense")
        print("2. View All Expenses")
        print("3. Total Spent")
        print("4. Total By Category")
        print("5. Exit")

        choice = input("Enter your choice: ")

        if choice == "1":
            add_expense(expenses)
        elif choice == "2":
            view_expenses(expenses)
        elif choice == "3":
            total_spent(expenses)
        elif choice == "4":
            total_by_category(expenses)
        elif choice == "5":
            print("Thank you for using Expense Tracker!")
            break
        else:
            print("Invalid choice. Try again.")

main()
