# Ask user to enter three numbers and print largest of three
try:
    num1 = int(input("Enter first number: "))
    num2 = int(input("Enter second number: "))
    num3 = int(input("Enter third number: "))

    if num1>=num2 and num1>=num3:
        print(num1)

    elif num2>=num1 and num2>=num3:
        print(num2)

    else:
        print(num3)

except ValueError:
    print("Invalid input: Please enter only integers.")

