# Reading one line at a time from file along with its length 
# Open file for reading
with open("notes.txt","r") as file:
    # Read the file one line at a time
    for line in file:
        #Remove new line character at the end of each line
        line = line.rstrip("\n")
        # Print the number of characters in the line and the line itself
        print(f"Character count {len(line)},{line}")