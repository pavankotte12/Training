# Zero Division Exception Handling
# Try block will handle possible errors
try:
    # Take two numbers as input from the user 
    num1 = int(input("Enter first number: "))
    num2 = int(input("Enter second number: "))
    
    result = num1/num2

# Handle divison by zero error
except ZeroDivisionError:
     print("Can not divide with zero. Please enter non-zero number")

# Execute only if no exception occurs
else:
     print(f"Result {result}")

# Always execute this block
finally:
     print("Done")