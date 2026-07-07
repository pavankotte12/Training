#Fetching published year of the books and displaying titles published after 2010
books = [
    {"title":"Educated", "year":2007, "author":"Tara Westover"},
    {"title":"Project Hail Mary", "year":2021, "author":"Andy Weir"},                
    {"title":"Silent Patient", "year":2010, "author":"Alex Michaelides"},                
    {"title":"Fifth Season", "year":2015, "author":"N.K.Jemisin"}
]
print(f"Titles of the books published after 2010:");
for book in books:
    if book["year"]>2010:
        print(book["title"])