#Ask user to enter 1 to 20 and print squares of number if its divisible by 3
n=[1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18,19,20]
squares = [num**2 for num in n if num%3!=0]

print(squares)
