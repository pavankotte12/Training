# Look up for positions entered by the user 
# Hard coded list of values
values = [10,20,30,40,50]
try:
    # Take input and convert into integer
    index = int(input("Enter a index position (0 to 4): "))
    
    # Try accessing the list
    print(f"Value at postion {index} is {values[index]}")

except IndexError:
    print("Position does not exist in the list. Please enter a valid index (0 to 4)")

except ValueError:
    print("Please enter a whole number: ")

finally:
    print("Lookup attempt finished")
