import csv

# Data to write
data = [
    ['Name', 'Age', 'City'],              # Header row
    ['Alice', 28, 'Boston'],              # Row 1
    ['Bob', 35, 'San Francisco']          # Row 2
]

# Open a file in write mode
with open('output.csv', 'w', newline='') as file:
    csv_writer = csv.writer(file)

    # Write rows
    csv_writer.writerows(data)


import csv

with open('output.csv', 'r') as file:
    csv_reader = csv.reader(file)
    
    for row in csv_reader:
        print(row)

