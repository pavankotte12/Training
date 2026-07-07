# Ask user to enter sentence and first and last five characters and reversed sentence 
str = input("Enter a sentence:")
try:
    print(str[0:5])
    print(str[-5:])
    print(str[::-1])
except Exception as e:
    print(f"An unexpected error occurred: {e}")