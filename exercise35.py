"""
In the previous example, we used min and max functions to 
get minimum and maximum of numbers

In this example we'll create a function that will return 
some value instead of printing it.

Let's see then?
"""
def square(number):
	ans = number * number
	return ans # you need to use return to return a value

result = square(5) 
# 5 will be pass to number
# after processing, ans = 25 and that value
# will be returned and assigned to result.
print(result)
