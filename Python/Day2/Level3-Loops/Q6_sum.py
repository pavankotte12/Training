# Ask user to enter number and print sum of one to n and same sum with another loop type
try:
    n = int(input("Enter a number: "))
    sum = 0
    for i in range(1,n+1):
        sum+=i
        print(sum)
        
    count = 1
    while count<=n:
        sum=sum+count
        count=count+1
        print(sum)

except ValueError:
    print("Invalid input: Please enter only integers.")
