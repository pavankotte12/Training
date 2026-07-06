
# Open file for reading
with open("notes.txt","r") as file:
    # Read all lines into a list
    lines = file.readlines()

# Print the total number of lines
print(f"Total lines : {len(lines)}")

# Print the last line
print(f"Last line : {lines[-1].rstrip()}")