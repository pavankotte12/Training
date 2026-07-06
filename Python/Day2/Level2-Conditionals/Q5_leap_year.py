# Ask user to enter year and check whether it is a leap year 
try:
    y = int(input("Enter a year: "))

    if y%4==0:
        if y%100==0:
            if y%400==0:
                print("Leap year")
            else:
                print("Not a leap year")
        else:
            print("Leap year")
    else: 
        print("Not a Leap year")

except ValueError:
    print("Invalid input: Please enter a valid year (integer).")
