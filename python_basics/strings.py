# Strings
double_quotes = "I can't type to save my life"
single_quotes = 'I can\'t type to save my life'
print(double_quotes)
print(single_quotes)

# String Concatenation
part_one = 'Hello '
part_two = 'World!'
print(part_one + part_two)
print('Hello ' + part_two)

# Repeating Characters
exclamation = '!'
mad = 'Now I\'m angry' + exclamation * 3
print(mad)

# String Methods
# Obtain String Length
sentence_length = len(double_quotes)
print('The first sentence I typed in this program is %s characters long' %(sentence_length))

# All caps
big_mad = mad.upper()
print(big_mad)

# Lowecase everything
small_mad = mad.lower()
print(small_mad)

# Uppercase every first letter of a word (Includes letters after an escaped character)
proper_mad = mad.title()
print(proper_mad)

# Convert numbers to strings
converted_number = str(sentence_length)
print('Now that the number has been converted, I can concatenate two strings. Proof: ' + converted_number)

# Formatted strings
template = 'Hello {}!'
print(template.format('Ezell'))

# Substring checking
my_name = 'Ezell'
has_zell = 'zell' in my_name
print('Does my name contain zell?')
def yes_or_no(boolean):
  return 'yes' if boolean == True else 'no'
print(yes_or_no(has_zell))