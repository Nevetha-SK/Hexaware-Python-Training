#--Use else after a loop to run code only if no break occurred: for i in range(1, 4):

for i in range(1, 4):
    print(f"Checking i = {i}")
    if i == 5:
        print("Found 5!")
        break
else:
    print("Loop finished without break.")


#--Nested If : if x > 10: and if x > 20:
x = 25

if x > 10:
    print("x is greater than 10")
    if x > 20:
        print("x is also greater than 20")


#--Combine multiple conditions in one if: using age,has_license

age = 22
has_license = False

if age >= 18 and has_license:
    print("You are allowed to drive.")
else:
    print("You are not allowed to drive.")


#--ages = [78, 34, 21, 47, 9] , condition = True , Use if else
ages = [78, 34, 21, 47, 9]
condition = True

if condition:
    for age in ages:
        print(f"Age is {age}")
else:
    print("Condition is False, so no ages are shown.")


#--Factorial (using recursive)
def factorial(n):
    if n == 0 or n == 1:
        return 1
    else:
        return n * factorial(n - 1)
num = 5
print(f"Factorial of {num} is {factorial(num)}")


#--Fibonacci
n = 10  # number of terms
a, b = 0, 1  # first two terms
print("Fibonacci series:")
for i in range(n):
    print(a, end=" ")
    a, b = b, a + b


#-----=Student Class with Instance Attributes------
class Student:
    def __init__(self, student_id, student_name):
        self.student_id = student_id        # Instance attribute for student ID
        self.student_name = student_name    # Instance attribute for student name

    def display(self):
        print("Student ID:", self.student_id)
        print("Student Name:", self.student_name)

# Create an instance of the Student class
student1 = Student(101, "Nevetha")
# Display the student details
student1.display()


#------Rectangle Class------
class Rectangle:
    def __init__(self, length, width):
        self.length = length   # Instance variable for length
        self.width = width     # Instance variable for width

    def compute_area(self):
        return self.length * self.width   # Formula for area of rectangle

# Create a Rectangle object
rect1 = Rectangle(10, 5)
# Compute and display the area
print("Area of rectangle:", rect1.compute_area())


#------Employee Class with Overtime Calculation------
class Employee:
    def __init__(self, emp_id, name, salary, department):
        self.emp_id = emp_id
        self.name = name
        self.salary = salary            # Monthly basic salary
        self.department = department

    def calculate_overtime_pay(self, overtime_hours, rate_per_hour):
        overtime_pay = overtime_hours * rate_per_hour
        return overtime_pay

    def display_employee(self):
        print("Employee ID:", self.emp_id)
        print("Name:", self.name)
        print("Department:", self.department)
        print("Basic Salary:", self.salary)

# Create an employee object
emp1 = Employee(101, "Nevetha", 30000, "HR")
# Display employee details
emp1.display_employee()
# Calculate and display overtime pay
overtime_hours = 10
rate_per_hour = 200
print("Overtime Pay:", emp1.calculate_overtime_pay(overtime_hours, rate_per_hour))


#-------Sum and product of a list------

numbers = [2, 3, 4, 5]
# Calculate sum
total_sum = sum(numbers)
# Calculate product
product = 1
for num in numbers:
    product *= num

print("Sum of list:", total_sum)
print("Product of list:", product)


#--------String Reversal------
text = "Hello, World!"
# Reverse the string using slicing
reversed_text = text[::-1]

print("Original string:", text)
print("Reversed string:", reversed_text)




