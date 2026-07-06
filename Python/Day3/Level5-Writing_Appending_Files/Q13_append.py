# Appeding name with date to movies.txt

name = input("Enter your name: ")

with open("movies.txt","a") as file:
    file.write(f"{name} - 05/07/2026\n")

with open("movies.txt","r") as file:
    print("Contents of movies.txt:")
    print(file.read())