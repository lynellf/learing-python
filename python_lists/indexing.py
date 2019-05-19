# indexing

books = [
    "Automate the Boring Stuff with Python: Practical Programming for Total Beginners - Al Sweigart",
    "Python for Data Analysis",
    "Fluent Python: Clear, Concise, and Effective Programming - Luciano Ramalho",
    "Python for Kids: A Playful Introduction To Programming - Jason R. Briggs",
    "Hello Web App: Learn How to Build a Web App - Tracy Osborn",
]

first_book = books[0]
last_book = books[4]
template = 'The first book selected is {}. The second book selected is {}'
print(template.format(first_book, last_book))

# Negative indexing
# The last item of a list is always -1, and will count incrementally to index backwards
first_book = books[-5]
last_book = books[-1]
print(template.format(first_book, last_book))

# Inserting At...
# A new item will insert itself before the previously indexed item
new_book = 'How to Get Rich - Felix Dennis'
books.insert(1, new_book)
print(books)