from database import conn, cursor


# Add expense
def add_expense():
    title = input("Enter expense title: ")
    amount = float(input("Enter amount: "))
    category = input("Enter category: ")
    date = input("Enter date (YYYY-MM-DD): ")

    cursor.execute(
        "INSERT INTO expenses (title, amount, category, date) VALUES (?, ?, ?, ?)",
        (title, amount, category, date)
    )
    conn.commit()
    print("Expense added successfully!")


# View expenses
def view_expenses():
    cursor.execute("SELECT * FROM expenses")
    expenses = cursor.fetchall()

    if expenses:
        print("\nExpense Records:")
        for expense in expenses:
            print(expense)
    else:
        print("No expenses found.")


# Monthly summary
def monthly_summary():
    cursor.execute("SELECT SUM(amount) FROM expenses")
    total = cursor.fetchone()[0]

    if total:
        print("\nTotal Monthly Expense:", total)
    else:
        print("No expenses available.")


# Main menu
while True:
    print("\nExpense Tracker System")
    print("1. Add Expense")
    print("2. View Expenses")
    print("3. Monthly Summary")
    print("4. Exit")

    choice = input("Enter your choice: ")

    if choice == "1":
        add_expense()
    elif choice == "2":
        view_expenses()
    elif choice == "3":
        monthly_summary()
    elif choice == "4":
        print("Thank you for using Expense Tracker!")
        break
    else:
        print("Invalid choice! Please try again.")
