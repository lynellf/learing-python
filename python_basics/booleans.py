# Booleans
true = True
false = False
print('A true statement returns the value {} and a false staement returns the value {}'.format(true, false))

# What values return true and or false
empty_string = '' # False
zero = 0 # False
one = 1 # True
empty_list = [] # False
empty_dictonary = {} # False
print('An empty string returns {}. The number zero returns {}. The number one returns {}. An empty list returns {}. An empty dictionary returns {}.'.format(
    bool(empty_string), bool(zero), bool(one), bool(empty_list), bool(empty_dictonary)))

# Conditionals
print(bool(1) and bool(0)) # False
print(bool(1) and bool(1)) # True
print(bool(1) or bool(0)) # True