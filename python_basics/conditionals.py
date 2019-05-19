# Conditionals

# if statement
value = 1
value_type = type(value)
value_is_string = value_type is str
value_is_int = value_type is int

if value_is_string:
  print('The variable "value" is a string')

# if else statement
if value_is_string:
  print('The variable "value" is a string.')
else:
  print('The variable "value" is not a string.')

# else if statement (written as elif)
if value_is_string:
  print('The variable "value" is a string.')
elif value_is_int:
  print('The variable "value" is not a string, but a integer.')
