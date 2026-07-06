# Custom exception class for age validation
class InvalidAgeError(Exception):
    pass

try:
    # Ask user to enter their age 
    age = int(input("Enter your age: "))

    # Check if the age is invalid
    if age < 0: 
        raise InvalidAgeError("Age cannot be negative")
    elif age > 120:
        raise InvalidAgeError("Age cannot be greater than 120")
    
    # Print a greeting if the age is valid
    print(f"Welcome! Your age is {age}")

# Handle invalid number input    
except ValueError:
    print("Please enter valid number") 

# Handle the custom exception
except InvalidAgeError as e:
    print(f"Error : {e}") 

finally:
    print("Done")
    