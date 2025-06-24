import json

# Reading JSON data from a file
with open('data.json', 'r') as file:
    data = json.load(file)

print(data)


import json

# JSON string
json_string = '{"name": "John", "age": 30, "city": "New York"}'

# Parse JSON string into a Python dictionary
data = json.loads(json_string)

print(data)


import json

# Python data to save as JSON
data = {
    "name": "Alice",
    "age": 25,
    "city": "Boston",
    "skills": ["Python", "SQL", "Machine Learning"]
}

# Write JSON data to a file
with open('output.json', 'w') as file:
    json.dump(data, file, indent=4)


import json

# Python data to convert into a JSON string
data = {
    "name": "Bob",
    "age": 40,
    "city": "Chicago"
}

# Convert Python data to a JSON string
json_string = json.dumps(data, indent=2)
print(json_string)


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
