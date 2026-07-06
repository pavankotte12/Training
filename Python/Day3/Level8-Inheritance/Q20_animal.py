# Animal class with dog and cat subclass which overrides generic sound with their own sound

# Define the base class
class Animal:

    # Constructor to initialize the animal's name
    def __init__(self, name):
        self.name = name

    # Method to return generic sound
    def speak(self):
        return "Some generic sound"

# Define the dog subclass
class Dog(Animal):
    # Override the speak method
    def speak(self):
        return "Bow Bow!"

# Define the cat subclass   
class Cat(Animal):
    # Override the speak method
    def speak(self):
        return "Meow Meow!"

# Create objects
dog = Dog("max")
cat = Cat("kitty")

# Print what each animal says
print(dog.name, "says:", dog.speak())
print(cat.name, "says:", cat.speak())