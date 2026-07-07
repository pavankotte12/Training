# Ask user to enter number and print sum of one to n and same sum with another loop type
try:
    n = int(input("Enter a number: "))
    #Print using for loop
    print(f"Printing data using for loop")
    sum = 0
    for i in range(1,n+1):
        sum+=i
        print(sum)    
    
    #Print using while loop
    print(f"Printing data using while loop")
    sum2 = 0
    i = 1
    while i <= n:
        sum2 += i
        print(sum2)
        i += 1

except ValueError:
    print("Invalid input: Please enter only integers.")
