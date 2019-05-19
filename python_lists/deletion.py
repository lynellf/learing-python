# Deletion

books = [
    "Automate the Boring Stuff with Python: Practical Programming for Total Beginners - Al Sweigart",
    "Python for Data Analysis",
    "Fluent Python: Clear, Concise, and Effective Programming - Luciano Ramalho",
    "Python for Kids: A Playful Introduction To Programming - Jason R. Briggs",
    "Hello Web App: Learn How to Build a Web App - Tracy Osborn",
]

# Delete an item by its index position
del books[3] # delete the python for kids book
print(books)

books.pop(1) # deletes the python for data analysis book
print(books)

# Delete the last item in an list
books.pop() # delete the hello web app book
print(books)

