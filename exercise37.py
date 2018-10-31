"""
In this and the next exercise, we're going to challenge ourselves.

We will be creating a complex function.

Challenge 1: 
Write a program that accepts a number and returns
True or False, True if it is perfect and False if it is not perfect.

Perfect numbers are those numbers whose sum of Factors lead to the 
same number

Example: 6
6 factors are 1,2, and 3 -> addition of factors give us 6
28 factors are 1,2,4,7,14 -> addition of factors give us 28

So 6 and 28 are Perfect numbers
"""
def checkPerfect(number):
	sum = 1 # creating a variable to store addition of factors
	# I am assigning 1 to sum as by default every number is divisible
	# by 1.
	count = 2 # creating a loop variable with 2 as value 
	while count <= number:
		if number%count == 0:
			sum = sum + count
		count = count + 1 # incrementing count by 1
	# note  the indentation
	if sum == number:
		return True
	else:
		return False

# calling checkPerfect in if block
# we can do that.
num = 20 # you can change the number as you like

if checkPerfect(num): # checkPerfect will return True or False
	# so it'll work perfectly with if.
	print('Perfect')
else:
	print('Not Perfect')