"""
Optional Arguments:

Whenever we have functions with arguments, it's mandatory
to provide it.

What if we don't want to?

We can create optional arguments for that purpose.

Let's see it action.
"""
def addition(number1=0,number2=0):
	# we've created optional arguments
	# we just need to provide default values
	sum = number1 + number2
	return sum

res1 = addition(20,34)
# providing arguments 20 and 34 to number1 and number2

res2 = addition(24)
# providing one argument not providing number2

res3 = addition()
# not providing any argument

print(res1)
print(res2)
print(res3)