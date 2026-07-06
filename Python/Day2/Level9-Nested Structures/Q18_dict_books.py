#Fetching published year of the book and displaying titles published after 2010

books = [
                {"title":"Educated", "year":2007, "Author":"Tara Westover"},

                {"title":"Project Hail Mary", "year":2021, "Author":"Andy Weir"},
                
                {"title":"Silent Patient", "year":2010, "Author":"Alex Michaelides"},
                
                {"title":"Fifth Season", "year":2015, "Author":"N.K.Jemisin"}
]

for book in books:
    if book["year"]>2010:
        print(f"Titles of the books published after 2010: {book["title"]}")
    
    else:
        print("No books to display")
