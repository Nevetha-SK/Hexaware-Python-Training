#For Json File
import json

try:
    with open('data.json', 'r') as file:
        data = json.load(file)
        print(data)

except FileNotFoundError:
    print("The file was not found.")

except json.JSONDecodeError:
    print("Invalid JSON format.")

except Exception as e:
    print("An unexpected error occurred:", e)
