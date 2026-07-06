# Convert age and height to correct types

name = input("Enter name: ")
age = input("Enter age: ")
height = input("Enter height: ")

age = int(age)
height = float(height)

print("Name is", name)
print("Age is", age, ',' "Type is ", type(age))
print("Height is", height, ',' "Type is ", type(height))
