# Keep asking user until they enter a valid whole number
while True:
    try:
        # Take input and convert it to a integer
        num = int(input("Enter a whole number: "))
        print("You entered:", num)
        break
   
    # Executes only if no exception occurs in try block
    except ValueError:
        print("Invalid input. Enter whole number.")
    
    # Always execute this block
    finally:
        print("")