"""
In this exercise, we're going to challenge ourselves again.

We will be creating a complex function.

Challenge 1: 
Write a program that checks whether a particular string is a part
of another string.

Example:

o is a part of Loop
thon is a part of Hackathon
Canada is not a part of USA (It's true by the way!)
"""
def isPartOf(parent,child):
	# to check a string is a part of particular string or not
	# we need to use a special keyword - in
	return child in parent
	# in returns True or False

mainString = 'Hackathon'
subString = 'thon' 
# you can change the above values
if isPartOf(mainString,subString): 
	print(subString+' is a part of '+mainString)
else:
	print(subString+' is not a part of '+mainString)