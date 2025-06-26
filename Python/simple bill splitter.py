import math

# Lambda to calculate each person's share
split_bill = lambda total, count: round(total / count, 2)

# Function to start the bill splitting process
def start_splitter():
    print("🍽️  Welcome to the Bill Splitter!")
    try:
        num_people = int(input("Enter number of people: "))
        if num_people <= 0:
            print("❌ Number must be greater than 0.")
            return
        
        names = []
        for i in range(num_people):
            name = input(f"Enter name of person {i+1}: ")
            names.append(name)

        total = float(input("Enter total bill amount: ₹"))
        if total <= 0:
            print("❌ Amount must be positive.")
            return

        per_person = split_bill(total, num_people)
        print("\n🧾 Split Summary:")
        for name in names:
            print(f"  {name} should pay: ₹{per_person}")

        print(f"\nTotal: ₹{math.fsum([per_person]*num_people)}")

    except ValueError:
        print("❌ Invalid input. Please enter numbers properly.")

# Run the app
start_splitter()
