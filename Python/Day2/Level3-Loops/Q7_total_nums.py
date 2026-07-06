# Ask user to enter numbers until its zero and print final total
try:
    total = 0
    while True:
        num = int(input("Enter a number: "))
        if num==0:
            break
        total+=num

    print(f"Sum of all numbers is {total}")

except ValueError as e:
    print(f"Invalid input: {e}")

