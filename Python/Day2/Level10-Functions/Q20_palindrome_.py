try:
    # Function to check if a word is palindrome 
    def is_palindrome(word):
        return word == word[::-1]

    words = ["madam","python","level"]

    # Check each word and print result
    for word in words:
        if is_palindrome(word):
            print(f"{word} is a palindrome")
        else:
            print(f"{word} is not a palindrome")

except TypeError as te:
    print(f"Type error: {te}")

except Exception as e:
    print(f"Unexpected error: {e}")