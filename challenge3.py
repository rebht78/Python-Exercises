"""
This challenge is also in loops.

Here, we're using Loops and Variables again.

Write a Python Script that print sum of 'N' numbers

Here, we need to take input from the user.

Variables used will be:
number : to store input from the user
sum : to store sum of the numbers
count : to maintain count from 1 to number
"""
number = int(raw_input('Enter any number : '))
# we need to convert input into int.
sum = 0
count = 1

while count <= number:
	sum = sum + count
	count = count + 1
	# I'll print outside the while block
print('The sum is '+str(sum))