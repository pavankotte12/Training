class LowAverageError(Exception):
    # Custom exception raised when a student's average is below 40
    pass

# Define Student class
class Student:
    
    def __init__(self, name, marks):
        self.name = name
        self.marks = marks

    def get_average(self):
        average = sum(self.marks) / len(self.marks)
        if average < 40:
            raise LowAverageError(f"{self.name}'s average is below 40.")
        return average


# List of hardcoded Student objects
students = [
    Student("Pavan", [75, 80, 70]),
    Student("Raj", [30, 35, 40]),
    Student("Vishal", [90, 85, 88]),
    Student("priya",[20, 25, 30])
]

# Write passing students results to the file
with open("results.txt", "w") as file:
    for student in students:
        try:
            average = student.get_average()
            file.write(f"{student.name}: {average:.2f}\n")
        except LowAverageError:
            print(f"Warning: {student.name} has failed (average below 40)")

# Read and print the contents of the file
print("\nContents of results.txt:")
with open("results.txt", "r") as file:
    print(file.read())