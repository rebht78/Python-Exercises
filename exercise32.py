"""
Introducing Arguments:

Earlier functions were blocks of code but they were not dynamic.
I was not able to pass values to the function.

printFiveTimes was only able to print 'Sherlock'. 
If I want to print some other value what I need to do.

Do I need to change function block everytime?

Better solution is to pass arguments.

Let's see the updated printFiveTimes with argument
"""
def printFiveTimes(data):
	print(data*5) # we're using data within function

# calling printFiveTimes without any value
# you'll get an error just try it once.
# I am passing 'Watson' here.
printFiveTimes('Watson')

name = 'Kim'
printFiveTimes(name) # you can also pass variables
# but pass string only.