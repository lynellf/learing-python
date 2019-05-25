# Sometimes we don't want an entie list or string, just a part.

# A slice is a new list or string made from a previous list or string

favorite_things = ['raindrops on roses', 'whiskers on kittens', 'bright coppeer kettles', 'warm woolen mittens',
                   'bright paper packages tied up with string', 'cream colored ponies', 'crisp apple strudels']

# The number before the colon is the starting point. The number after is the end-point

some_favorite_things = favorite_things[0:2]
template = 'Some of my favorite things include {}'
print(template.format(some_favorite_things))

# we can omit the first number to always start from the first item
some_favorite_things = favorite_things[:2]
print(template.format(some_favorite_things))

# we can omit the second number to always select through the last item
some_favorite_things = favorite_things[3:]
print(template.format(some_favorite_things))

# copy a list
new_favorite_things = favorite_things[:]
print(template.format(new_favorite_things))

# Step through a sliced list (like every odd or even number)
# We can go from left to right with a positive number, or reverse with a negative number
numbered_list = list(range(21))
print(numbered_list[::-2])  # [20, 18, 16, 14, 12, 10, 8, 6, 4, 2, 0]

# We can use slices to delete or replace values

letters = ['a', 'b', 'c', 'd', 'e', 'f',
           'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n']
del letters[4:8]  # ['a', 'b', 'c', 'd', 'i', 'j', 'k', 'l', 'm', 'n']
letters = ['a', 'b', 'c', 'd', 'e', 'f',
           'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n']
letters[2:4] = ['hmm']
print(letters)

apple = ['a', 'p', 'p', 'l', 'e']
banana = ['b', 'a', 'n', 'a', 'n', 'a']


def sillycase(string):
    length = len(string)
    breakpoint = int(length / 2)
    first_half = string[:(breakpoint)].lower()
    second_half = string[breakpoint:length].upper()
    output = first_half + second_half
    return output


print(sillycase('BANANA'))
