"""
Let's see two more examples of functions.

Here, I will create a function that takes two arguments
and display all even numbers between them.
"""
def printEvenNumbers(number1, number2):
	# here, I'm assuming number1 is always > than number2
	count = number1 # assigning number1 to count
	while count <= number2: 
		# checking whether count is less than number2
		if count%2 == 0: # checking for divisbility by 2
			print(count) # printing count
		count = count + 1  # incrementing count by 1
		# to get closer to number2

print('First List')
printEvenNumbers(1,5) # providing two arguments
# number1 = 1 and number2 = 5

#Let's call the function again
print('Second List!')
printEvenNumbers(1,20)

# this will not work
print('No third list!')
printEvenNumbers(20,1) # this will not print anything.
# can you find out why?