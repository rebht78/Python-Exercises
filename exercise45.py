"""
In this exercise, we'll learn about methods in strings.

We will print string in upper case if it is in lower case.
If it is in upper case, then we'll print string in lower case.
"""
word = raw_input('Enter any string: ')
# now, this is routine...no need to explain
# above line.

# how to identify whether a string is in lower or upper case
# python to the rescue....
# isupper and islower
# isupper returns True if string is in upper case and vice versa.

if word.isupper(): # it is a function but with objects so we call it
# as methods.
	print(word.lower()) # convert it to lower
else:
	print(word.upper()) # convert it to upper
