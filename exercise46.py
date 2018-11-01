"""
In this exercise, we'll learn about one of the most 
important methods of string.

find() method:

find() method is used to find a string in another string.

Let's see an example
"""
words = raw_input('Enter any string: ')
search = raw_input('Enter search word: ')

searchIndex = words.find(search)
# returning an output and storing it in searchIndex

if searchIndex == -1:
	print(search+' not found in '+words)
else:
	print(search+' found at '+str(searchIndex)+' in '+words)
