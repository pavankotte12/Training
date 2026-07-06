# Saving students details to a CSV file 
import csv

# Create a list of dictionaries for 3 hardcoded students
students = [
            {"name": "pavan", "mark" : 75},
            {"name" : "raj", "mark" : 90},
            {"name" : "vishal", "mark" : 80}
]

# Open CSV file in write mode
with open("students.csv", "w", newline="") as file:
    # Create a DictWriter object with the column headings
    writer = csv.DictWriter(file, fieldnames = ["name", "mark"])
    # Write the header row 
    writer.writeheader()
    # Write each student's data to the file
    writer.writerows(students)

# Open CSV file in read mode
with open("students.csv", "r") as file:
    # Create a DictReader object
    reader = csv.DictReader(file)

    # Print each row from the CSV file
    for row in reader:
        print(row)