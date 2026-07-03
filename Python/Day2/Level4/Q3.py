n=1
res = []
for i in range(1,51):
    if i%3==0:
        res.append("Fizz")
    elif i%5==0:
        res.append("Buzz")
    elif i%3==0 and i%5==0:
        res.append("FizzBuzz")
    else:
        res.append(str(i))
    print(res)


