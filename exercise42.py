"""
Why we need varargs?

In some scenario, we don't know the number of inputs. 
So instead of fixing the number of inputs and having limited number 
of arguments. We can create function with varargs.

In this exercise, we'll find the sum of any numbers.

Let's see an example
"""
def sum(*args): # not necessary to name it as args
	result = 0
	count = 0
	while count < len(args):
		result = result + args[count] 
		# args is an implicit list. so we can use index on it.
		count = count + 1
	return result

# with zero arguments
print(sum())

# with two arguments
print(sum(9,8))

# with five arguments
print(sum(1,2,3,4,5))
