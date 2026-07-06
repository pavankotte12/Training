# Display text from a file 
# Open file for reading
with open("notes.txt","r") as file:

    # Store the file
    content = file.read()
print(content)