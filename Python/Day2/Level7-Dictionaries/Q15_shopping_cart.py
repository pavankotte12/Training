#Taking product name from user and displaying price of it

shopping_cart = {'shirt':2000,'pant':3000, 'shoes':3500, 'watch':5000, 'Accessories':1000}

user_item = input("Enter product name: ")

if user_item in shopping_cart:
        price = shopping_cart[user_item]
        print(f"The price of {user_item} is {price}")
else:
    print(f"Sorry,{user_item} is not in the shopping cart")



