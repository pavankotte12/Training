try:
    # Function to add all numbers from 1 to given number
    def add_recursion(n):

        # Stop when the number is less than or equal to 1
        if n<=1:
            return n
        
        # Add current number to total of the numbers
        else:
            return n + add_recursion(n-1)
        
    print(add_recursion(5))
except RecursionError:
    print("Number too large: recursion limit exceeded.")

except TypeError as te:
    print(f"Type error: {te}")

except ValueError as ve:
    print(f"Value error: {ve}")

except Exception as e:
    print(f"Unexpected error: {e}")