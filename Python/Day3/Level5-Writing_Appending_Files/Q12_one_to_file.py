# Writing one line at a time to the movies.txt

with open("movies.txt","w") as file:

    movie1 = input("Enter your first favourite movie: ")
    file.write(movie1 + "\n")

    movie2 = input("Enter your second favourite movie: ")
    file.write(movie2 + "\n")

    movie3 = input("Enter your third favourite movie: ")
    file.write(movie3 + "\n")

print("Your favourite movies saved in movies.text")
    