# Displaying highest average of a stundent from list of students
students =[
            {"name":"Raj", "marks":[70,95,80]},
            {"name":"Aryan", "marks":[75,60,80]},
            {"name":"Abhishek", "marks":[60,89,92]},
            {"name":"Shardul", "marks":[87,65,91]},
            
]

# Function to find the student with highest average
def highest_average(students):
    highest_name = ""
    highest_average = 0

    for student in students:
       average = sum(student["marks"]) / len(student["marks"])
       if average>highest_average:
           highest_average = average
           highest_name = student["name"]
    
    return highest_name

# Call the function and print result
result = highest_average(students)
print(f"Student with highest average marks is {result}")