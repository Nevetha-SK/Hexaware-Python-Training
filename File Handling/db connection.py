import pyodbc

# Step 1: Define your server and database
server = r'DESKTOP-VM2OBVF\SQLEXPRESS'  # if using express edition
database = 'CarRentalDB'  # Replace with the actual DB name if not 'master'

# Step 2: Connect to the database
conn = pyodbc.connect(
    r'DRIVER={ODBC Driver 18 for SQL Server};'
    rf'SERVER={server};'
    rf'DATABASE={database};'
    r'Trusted_Connection=yes;'
    r'TrustServerCertificate=yes;'
)

# Step 3: Create a cursor and execute a query
cursor = conn.cursor()
cursor.execute("SELECT TOP 5 * FROM Vehicle")  # Example: test query

# Step 4: Print result
for row in cursor.fetchall():
    print(row)

# Step 5: Clean up
cursor.close()
conn.close()

