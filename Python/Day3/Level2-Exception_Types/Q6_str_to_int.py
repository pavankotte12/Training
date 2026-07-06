# Conversion of string to integer and handling failed conversion
# Ask user to enter comma separated values
values = input("Enter comma separated values: ")

# Split the input into a list
items = values.split(",")

# Initialize the total
total = 0

# Process each value
for item in items:
    # Remove extra spaces
    item = item.strip()

    try:
        # Convert the value into an integer
        num = int(item)

        #Add the number to the running total
        total += num

    except ValueError:
        # Print a message if the value cannot be converted
        print(f"conversion failed for item : {item}")
    finally:
        print("Done")
        
# Display final total
print(f"Total = {total}")