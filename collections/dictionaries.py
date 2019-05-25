# Dictionaries
dictionary = {'name': 'Ezell', 'favorite_number': 9}
print(dictionary)

# Adding/ Updating keys
dictionary['name'] = 'James'
print(dictionary)

dictionary.update({'name': 'James Johnson', 'age': 30, 'favorite_number': 11})
print(dictionary)

# Packing and Unpacking Dictionaries
# Trasnform key-value arguments into a dictionary


def packer(**kwargs):
    print(kwargs)


packer(**{"name": "james", "age": "11"})  # { 'age': 11, 'name': 'james' }


def unpacker(first_name=None, last_name=None):
    if first_name and last_name:
        print('Hi {} {}!'.format(first_name, last_name))


unpacker(**{'first_name': 'James', 'last_name': 'Jones'})


def favorite_food(dict):
    return "Hi, I'm {name} and I love to eat {food}!".format(**dict)


print(favorite_food({'name': 'Ezell', 'food': 'pizza'}))

# Iterating dictionaries
# As I guessed, a for-in-loop

def keyPrinter(obj):
    if type(obj) is dict:
        for key in obj:
            print(key)

keyPrinter(dictionary)

# Obtaining keys from a dictionary
dictionary_keys = dictionary.keys()
dictionary_values = dictionary.values()
print(dictionary_keys)
print(dictionary_values)

# Iterate key and value pairs
for item in dictionary.items():
  print(item)

sentence = 'Hello, my name is ezell. My favorite language is python.'


def word_count(sentence):
    _input = sentence.lower().split()
    output = {}
    for word in _input:
        output[word] = _input.count(word)
    return output

print(word_count(sentence))


def stats(teachers):
    output = []
    for teacher in teachers:
        name = teacher
        count = len(teachers[name])
        stats = [name, count]
        output.append(stats)
    return output


teachers = {'Andrew Chalkley': ['jQuery Basics', 'Node.js Basics'],
'Kenneth Love': ['Python Basics', 'Python Collections']}

print(stats(teachers))