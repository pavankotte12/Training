# Handling Type Error
try:
    # Take a number input from the user and convert it to integer
    num = int(input("Enter a number: "))

    # Take a word(string) input from the user
    word = input("Enter a word: ")

    # Try to directly add integer and string(caused error)
    result = num + word
    print(f"result {result}")

# This error occurs when trying to add integer and string 
except TypeError as e:
    print(f"Error: , {e}, Can not add number and text")
    
# Always runs
finally:
    print("Done")