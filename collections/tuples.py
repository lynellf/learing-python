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

