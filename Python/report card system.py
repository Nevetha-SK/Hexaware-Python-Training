import math
import datetime

# List to store student records
students = []

# Tuple for fixed subjects
subjects = ("Math", "Science", "English", "History", "Computer")

# Lambda to assign grade based on percentage
grade_lambda = lambda p: (
    "A+" if p >= 90 else
    "A" if p >= 80 else
    "B" if p >= 70 else
    "C" if p >= 60 else
    "D" if p >= 50 else
    "F"
)

# Add student record
def add_student():
    try:
        name = input("Enter Student Name: ")
        roll = input("Enter Roll Number: ")
        marks = {}
        
        for sub in subjects:
            m = float(input(f"Enter marks for {sub} (out of 100): "))
            if m < 0 or m > 100:
                print("❌ Marks should be between 0 and 100")
                return
            marks[sub] = math.fabs(m)

        total = sum(marks.values())
        average = total / len(subjects)
        percentage = round((total / (100 * len(subjects))) * 100, 2)
        grade = grade_lambda(percentage)
        timestamp = datetime.datetime.now()

        student = {
            "name": name,
            "roll": roll,
            "marks": marks,
            "total": total,
            "average": average,
            "percentage": percentage,
            "grade": grade,
            "timestamp": timestamp
        }

        students.append(student)
        print("✅ Student record added successfully!")

    except Exception as e:
        print(f"❌ Error: {e}")

# Show report for a student
def show_report():
    roll = input("Enter roll number to view report: ")
    found = False

    for student in students:
        if student["roll"] == roll:
            found = True
            print("\n========== Report Card ==========")
            print(f"🧑 Name       : {student['name']}")
            print(f"🔢 Roll No    : {student['roll']}")
            print(f"🕒 Created on : {student['timestamp'].strftime('%Y-%m-%d %H:%M:%S')}")
            print("\n📚 Subject Marks:")
            for subject, mark in student["marks"].items():
                print(f"  {subject}: {mark}/100")

            print(f"\n📊 Total      : {student['total']}")
            print(f"📈 Average    : {student['average']:.2f}")
            print(f"🎯 Percentage : {student['percentage']}%")
            print(f"🏅 Grade      : {student['grade']}")
            print("===================================")
            break

    if not found:
        print("❌ No student found with that roll number.")

# Main menu
def main():
    while True:
        print("\n======= Student Report Card Menu =======")
        print("1. Add Student Record")
        print("2. View Student Report")
        print("3. Exit")
        choice = input("Enter your choice (1-3): ")

        if choice == "1":
            add_student()
        elif choice == "2":
            show_report()
        elif choice == "3":
            print("👋 Exiting... Goodbye!")
            break
        else:
            print("❌ Invalid choice. Please select 1-3.")

# Run the system
if __name__ == "__main__":
    main()
