"""
In this exercise, we'll accept a string and if the string length is less
than 6, we'll reject it.

For this, we'll be using len() function of python.
"""
word = raw_input('Enter any string: ')
# print(len(word))
# the above line is just for testing purpose.
if len(word) > 6:
	print(word+' is VALID!')
else:
	print(word+' is INVALID, require more than six characters!!!')