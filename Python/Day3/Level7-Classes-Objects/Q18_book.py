# Book that display title, author and price in a sentence

# Define Book class
class Book:

    # Constructor to intialize title, author and price
    def __init__(self,title,author,price):
        self.title = title
        self.author = author
        self.price = price

    # Method to display book details
    def display(self):
        print(f"Title : {self.title}, Author : {self.author}, Price : {self.price:.2f}")

# Create three Book objects with hardcoded values   
book1 = Book("The Alchemist", "Paulo Coelho", 499)
book2 = Book("1984", "George Orwell", 999)
book3 = Book("To kill a Mockingbird", "Harper Lee", 1499)

# Display the details of each book
book1.display()
book2.display()
book3.display()