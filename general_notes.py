# String interpolation in older versions of python
string_three = 'three'
print('The number %s is the same as the number 3.' %(string_three))

# The underscore variable (only in the REPL) returns the previous value printed
2 + 3 
# 5
# _
# 5

# Allow user input as a variable
value = input('Type something here to store it as a value')

# Sorting a list
# the original list is mutated to a sorted list
messy_list = [1, 4, 2, 3, 5]
messy_list.sort()

# The range function can generate a stream of numbers, counting from zero
numbered_list = list(range(4)) # [0, 1, 2, 3]
