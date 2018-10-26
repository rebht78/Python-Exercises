"""
In the previous example, we've one bug.

When we pass number1 greater than number2 then we doesn't get the 
even numbers.

Let's change the code and use a built-in function to solve it.
"""

def printEvenNumbers(number1, number2):
	# here, I'm using min() function of python
	# that returns me a minimum of numbers.
	# what returns (you would come to know in the next example)
	count = min(number1,number2) 
	# assigning minimum of number1 and number2 to count
	while count <= max(number1,number2): 
		# checking whether count is less than maximum of 
		# number1 and number2
		if count%2 == 0: # checking for divisbility by 2
			print(count) # printing count
		count = count + 1  # incrementing count by 1
		# to get closer to max of number1 and number2.

print('First List')
printEvenNumbers(1,5) # providing two arguments
# number1 = 1 and number2 = 5

#Let's call the function again
print('Second List!')
printEvenNumbers(1,20)

# this will not work
print('No third list!')
printEvenNumbers(20,1) # this will work now!