# Asking the user to input department and displaying total number of employees work
departments = {
                "IT" : ['Pavan', 'Charan', 'Arjun'],
                "HR" : ['Priya', 'Harika'],
                "Sales" :['Varun', 'Kalyan', 'Kartik', 'Ritika']
}

# Take department name from user
dept_name = input("Enter department name: ")

#Check and print the number of employees

if dept_name in departments:
    print(f"Total number of employees:{len(departments[dept_name])}")
else:
    print("Department not found")