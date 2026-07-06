# Display employee salary from the dictionary if not exist, handle the exception
emp_salaries = {
                "priya" : 200000,
                "rahul" : 175000,
                "kartik" : 150000,
                "raj" : 50000,
                "abhishek" : 300000

} 

#Ask the user for a key
key = input("Enter a employee name: ")

# Access and print the value for the entered key
try:
    print(f"{key}'s salary: {emp_salaries[key]}")

except KeyError:
    # Runs if entered key is not found in the dictionary
    print("key does not exist in the dictionary")

finally:
    # Always run
    print("Done")
