import math
import datetime

# List to store expenses
expenses = []

# Fixed categories
categories = ("Food", "Travel", "Bills", "Shopping", "Other")

# Add a new expense
def add_expense():
    try:
        amount = float(input("Enter amount: ₹"))
        category = input(f"Enter category {categories}: ").strip()
        date_str = input("Enter date (YYYY-MM-DD): ")

        if category not in categories:
            print("❌ Invalid category.")
            return

        date_obj = datetime.datetime.strptime(date_str, "%Y-%m-%d")

        expense = {
            "amount": math.fabs(amount),
            "category": category,
            "date": date_obj
        }

        expenses.append(expense)
        print("✅ Expense added!")
    except:
        print("❌ Error: Please enter valid amount/date format.")

# Show monthly total
def show_monthly_expense():
    try:
        month = int(input("Enter month (1-12): "))
        year = int(input("Enter year (e.g., 2025): "))
        total = sum(e["amount"] for e in expenses if e["date"].month == month and e["date"].year == year)
        print(f"📅 Total expenses for {month}/{year}: ₹{total:.2f}")
    except:
        print("❌ Invalid input.")

# Show yearly total
def show_yearly_expense():
    try:
        year = int(input("Enter year (e.g., 2025): "))
        total = sum(e["amount"] for e in expenses if e["date"].year == year)
        print(f"📆 Total expenses for {year}: ₹{total:.2f}")
    except:
        print("❌ Invalid input.")

# Show category-wise summary for a specific month and year
def show_monthly_category_summary():
    try:
        month = int(input("Enter month (1-12): "))
        year = int(input("Enter year (e.g., 2025): "))
        print(f"\n📊 Category-wise Summary for {month}/{year}:")
        category_totals = {cat: 0 for cat in categories}

        for e in expenses:
            if e["date"].month == month and e["date"].year == year:
                category_totals[e["category"]] += e["amount"]

        for cat, total in category_totals.items():
            print(f"  {cat}: ₹{total:.2f}")
    except:
        print("❌ Invalid input.")

# Show category-wise summary for a specific year
def show_yearly_category_summary():
    try:
        year = int(input("Enter year (e.g., 2025): "))
        print(f"\n📊 Category-wise Summary for {year}:")
        category_totals = {cat: 0 for cat in categories}

        for e in expenses:
            if e["date"].year == year:
                category_totals[e["category"]] += e["amount"]

        for cat, total in category_totals.items():
            print(f"  {cat}: ₹{total:.2f}")
    except:
        print("❌ Invalid input.")

# Main menu
def main():
    while True:
        print("\n========== Expense Tracker ==========")
        print("1. Add Expense")
        print("2. View Monthly Total")
        print("3. View Yearly Total")
        print("4. View Monthly Category-wise Summary")
        print("5. View Yearly Category-wise Summary")
        print("6. Exit")
        choice = input("Choose an option (1-6): ")

        if choice == "1":
            add_expense()
        elif choice == "2":
            show_monthly_expense()
        elif choice == "3":
            show_yearly_expense()
        elif choice == "4":
            show_monthly_category_summary()
        elif choice == "5":
            show_yearly_category_summary()
        elif choice == "6":
            print("👋 Goodbye!")
            break
        else:
            print("❌ Invalid choice. Please select 1-6.")

# Run the tracker
if __name__ == "__main__":
    main()
