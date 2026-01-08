from objects import Product, Book, Movie

prod1 = Product("Projector", 58000.0, 2)
book1 = Book("Attitude", 380.0, 10, "John C Maxwell")
movie1 = Movie("Bahubali", 800.0, 0, 2015)

# call getDescription() method of 3 objects
print(prod1.getDescription())
print()
print(book1.getDescription())
print()
print(movie1.getDescription())