"""
This challenge is pretty simple.

Here, we're using Loops and Variables.

Write a Python Script that print multiplication tables upto 10.

Here, We need to print multiplication tables from 1 to 10.
This is a super example of nested loops and
there is no need to take input from the user.
"""
number = 1 # as we're going to start from 1

while number <= 10: # we're going to print multiplication tables upto 10
	count = 1 # to start from 1
	while count <= 10:
		print(str(number)+' * '+str(count)+' = '+str(count*number))
		count = count + 1
	number = number + 1
