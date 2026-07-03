list = []
n = int(input("Total numbers:"))

for i in range(n):
    items = input(f"Enter a number {i+1}:")
    list.append(items)
print(list)

list.sort()
print(list)

min = min(list)
print(f"Minimum number is {min}")

max = max(list)
print(f"Maximum number {max}")

