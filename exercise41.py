"""
Moving forward with functions in this exercise and next, we're going to 
learn about varargs (variable number of arguments)

function with varargs can take any number of arguments, even zero.

You need to specify argument with *
Let's see an example
"""
def argumentExample(*args):
	print('You have passed '+str(len(args))+' arguments.')
	# the above example is of chaining
	# where output of one function is passed as arguments to another 
	# function.
	# here, len's output is passed to str for conversion into string.

# calling argumentExample
argumentExample()

argumentExample(2,3)

argumentExample(2,3,4)

