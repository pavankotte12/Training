# Class with unrelated shapes and displaying type of shape

# Define Circle class
class Circle:
    # Constructor to initialize radius
    def __init__(self, radius):
        self.radius = radius
        
    # Method to calculate area
    def area(self):
        return 3.14 * self.radius * self.radius

# Define Suare class
class Square:
    # Constructor to initialize side
    def __init__(self, side):
        self.side = side

    # Method to calculate area
    def area(self):
        return self.side * self.side

# Define Rectangle class
class Rectangle:
    # Constructor to initialize length and width
    def __init__(self, length, width):
        self.length = length
        self.width = width
    
    # Method to calculate area
    def area(self):
        return self.length * self.width

# Create object of each class
circle = Circle(5)
square = Square(4)
rectangle = Rectangle(6, 3)

# Store all objects in a single list
shapes = [circle, square, rectangle]

# Loop through the list and print the area of each shape
for shape in shapes:
    print(f"Area: {shape.area()}")