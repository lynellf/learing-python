# Tuples
# Tuples are like lists, but completely immutable

a_tuple = 1, 2, 3
another_tuple = (4, 5, 6)
converted_tuple = tuple(['a', 'b', 'c'])
print(converted_tuple)

# However, we can mutate mutable items within a tuple
# converted_tuple[0][0] = 'b'
new_tuple = [1, 2, 3], [4, 5, 6]
new_tuple[0][0] = 0
print(new_tuple)

# Tuples have simultanious assignment.
# Allows us to swap values around without adding a third assignment
a = [1, 2, 3]
b = a
a, b = b, a
b[0] = 10
values = {'a': a, 'b': b} # { 'a': 20, 'b': 5 }
print(values)

# Python packed the original assignments on the left hand side
# Python then unpacked the variables on the right hand side

# It seems like *args can only take a tuple as 
# a param and not any iterable like a list

def add(*nums):
    total = 0
    for num in nums:
        total += num
    return total
print(add(1, 2, 3)) #6

def sum(base, *nums):
    total = base
    for num in nums:
        total += num
    return total
print(sum(1, 2, 3)) #6

def multiply(*args):
    product = 1
    for arg in args:
        product *= arg
    return product
print(multiply(2, 2, 2)) #8

def logger(input):
    for key, value in input.items():
        template = 'The key {} has a value of {}'.format(key, value)
        print(template)
ezell = {'First Name': 'Ezell', 'Last Name': 'Frazier'}
logger(ezell)

string = 'Ezell'

def stringcases(string):
    upper = string.upper()
    lower = string.lower()
    title = string.title()
    _reverse = list(string)
    _reverse.reverse()
    reverse = ''.join(_reverse)
    return upper, lower, title, reverse
print(stringcases(string))

def combo(args):
    iterable_1 = args[0]
    iterable_2 = args[1]
    output = []
    index = 0
    for item in iterable_1:
        output.append((item, iterable_2[index]))
        index+= 1
    return output
test = ([1, 2, 3], 'abc')
print(combo(test))