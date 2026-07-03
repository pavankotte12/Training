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