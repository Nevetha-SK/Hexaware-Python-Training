# Define server and database
server = r'DESKTOP-VM2OBVF\SQLEXPRESS'  # if using express edition
database = 'CarRentalDB'  

# Connect to the database
conn = pyodbc.connect(
    r'DRIVER={ODBC Driver 18 for SQL Server};'
    rf'SERVER={server};'
    rf'DATABASE={database};'
    r'Trusted_Connection=yes;'
    r'TrustServerCertificate=yes;'
)

#  Create a cursor and execute a query
cursor = conn.cursor()
cursor.execute("SELECT TOP 5 * FROM Vehicle")  # Example: test query

# Print result
for row in cursor.fetchall():
    print(row)

# Clean up
cursor.close()
conn.close()

