#----------Class & Object----------
# Define a class
class Person:
    # Constructor
    def __init__(self, name, age):
        self.name = name
        self.age = age

    # Method to greet
    def greet(self):
        print(f"Hello, My name is {self.name} and I am {self.age} years old.")

# Create an object of the class
person1 = Person("Nivi", 21)

# Call the greet method
person1.greet()


#----------Ecapsulation----------
class BankAccount:
    def __init__(self, owner, balance=0):
        self.owner = owner
        self.__balance = balance  # Private attribute

    def deposit(self, amount):
        if amount > 0:
            self.__balance += amount
            print(f"${amount} deposited. New balance: ${self.__balance}")
        else:
            print("Invalid deposit amount.")

    def withdraw(self, amount):
        if 0 < amount <= self.__balance:
            self.__balance -= amount
            print(f"${amount} withdrawn. New balance: ${self.__balance}")
        else:
            print("Insufficient balance or invalid amount.")

# --- Testing the class ---
account = BankAccount("Nivi", 200)
account.deposit(50)
account.withdraw(30)

# Accessing private attribute will throw an error
# print(account.__balance)


#----------Encapsulation + Inheritance + Polymorphism----------
class BankAccount:
    def __init__(self, account_holder, balance=0):
        self.account_holder = account_holder
        self.__balance = balance  # Private attribute

    def deposit(self, amount):
        if amount > 0:
            self.__balance += amount
            print(f"${amount} deposited. New balance: ${self.__balance}")
        else:
            print("Invalid deposit amount.")

    def withdraw(self, amount):
        if amount <= self.__balance:
            self.__balance -= amount
            print(f"${amount} withdrawn. New balance: ${self.__balance}")
        else:
            print("Insufficient balance.")

    def get_balance(self):
        return self.__balance

class SavingsAccount(BankAccount):
    def __init__(self, account_holder, balance=0, interest_rate=0.03):
        super().__init__(account_holder, balance)
        self.interest_rate = interest_rate

    def add_interest(self):
        interest = self.get_balance() * self.interest_rate
        self.deposit(interest)
        print(f"Interest added: ${interest}")

# --- Usage ---
acc = SavingsAccount("Nivi", 2000)
acc.deposit(500)
acc.add_interest()
acc.withdraw(200)


#----------Library Management System----------
class Book:
    def __init__(self, title, author, copies):
        self.title = title
        self.author = author
        self.copies = copies

    def borrow_book(self):
        if self.copies > 0:
            self.copies -= 1
            print(f"You borrowed '{self.title}'. Copies left: {self.copies}")
        else:
            print(f"'{self.title}' is currently unavailable.")

    def return_book(self):
        self.copies += 1
        print(f"You returned '{self.title}'. Copies available: {self.copies}")

# --- Usage Example ---
book = Book("No Exit", "Taylor Adams", 6)

book.borrow_book()   # Copies: 5
book.borrow_book()   # Copies: 4
book.return_book()   # Copies: 5


#----------Hospital Management----------
class Patient:
    def __init__(self, name, age, ailment):
        self.name = name
        self.age = age
        self.ailment = ailment

    def display_info(self):
        print(f"Patient Name: {self.name}, Age: {self.age}, Ailment: {self.ailment}")

class Doctor:
    def __init__(self, name, specialty):
        self.name = name
        self.specialty = specialty

    def diagnose(self, patient):
        print(f"Dr. {self.name} ({self.specialty}) is diagnosing {patient.name}.")

# --- Usage ---
patient = Patient("Nivi", 21, "Fever")
doctor = Doctor("Dr. Ruth", "General Physician")

patient.display_info()
doctor.diagnose(patient)


#----------Exception Handling----------
try:
    file = open("sample.txt", "r")  # Change filename if needed
    content = file.read()
except FileNotFoundError:
    print("File not found.")
else:
    print("File content read successfully.")
    print("Content:\n", content)
finally:
    print("Closing file.")
    if 'file' in locals() and not file.closed:
        file.close()


#----------File pointer using tell()----------

with open("sample.txt", "r") as file:
    print("Initial pointer position:", file.tell())  # Should be 0

    # Read the first 5 characters
    data = file.read(5)
    print("Read data:", data)
    
    # Show pointer position after reading
    print("Pointer position after reading 5 characters:", file.tell())

    # Read 10 more characters
    more_data = file.read(10)
    print("Next 10 characters:", more_data)
    
    # Final pointer position
    print("Final pointer position:", file.tell())


#----------Seek() with existing sample.txt----------

with open("sample.txt", "rb") as file:
    file.seek(5)
    print("Character at position 6:", file.read(1).decode())

    file.seek(-3, 2)
    print("Character 3 bytes before end:", file.read(1).decode())
