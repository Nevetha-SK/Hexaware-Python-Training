import pandas as pd

# Load the Excel file
df = pd.read_excel("c:\\Users\\Dell\\Documents\\person-marks.xlsx", engine='openpyxl')

# Display contents
print(df)

# Add 1 person's data
new_row = pd.DataFrame([{"Name": "Frank", "Marks": 89}])

# Append the new row
df = pd.concat([df, new_row], ignore_index=True)

# Write it back to the same Excel file
df.to_excel("c:/Users/Dell/Documents/person-marks.xlsx", index=False, engine='openpyxl')


