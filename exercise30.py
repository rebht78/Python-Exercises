"""
Now, we are moving forward with another concept of Python.
perhaps the most important one : Functions.

Functions are blocks of code that has a name, using which
you can call it wherever you want to; instead of 
repeating the block of code again and again.

Syntax of function is as follows:

def <functionname>():
	<any python code here>

After creating function, you need to call it otherwise the block of code
is not getting executed.

Calling function Syntax:

<functionname>()

Let's see functions in action.
"""
# I am creating a simple function that print square of 5
def squareOfFive():
	number = 5
	print(number*number)

# you need to call squareOfFive
squareOfFive()
# that's how you call it

# Let's see more complex functions
# in the next exercises.