# Saving students details to a JSON file 
import json

# Create a list of dictionaries for 3 hardcoded students
students = [
            {"name": "pavan", "mark" : 75},
            {"name" : "raj", "mark" : 90},
            {"name" : "vishal", "mark" : 80}
]

# Open JSON file in write mode
with open("students.json","w") as file:
    # Write each student data to the file
    json.dump(students, file)

# Open JSON file in read mode
with open("students.json", "r") as file:
    # Read the student data from the JSON file
    students = json.load(file)

# Find the student with highest mark
highest = students[0]
for student in students:
    if student["mark"] > highest["mark"]:
        highest = student

# Print the name of the student with highest mark    
print(f"Student with the highest mark: {highest["name"]}")