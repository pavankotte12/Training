# Adding new student details to the existing students.csv file
import csv

# Ask the user for a new student's details
name = input("Enter student's name: ")
mark = int(input("Enter student's mark: "))

# Open the file in append mode
with open("students.csv", "a", newline="") as file:
    writer = csv.writer(file)
    writer.writerow([name, mark])

# Display updated contents of the file
with open("students.csv", "r") as file:
    reader = csv.reader(file)
    print("Updated students.csv")
    for row in reader:
        print(row)