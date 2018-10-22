"""
Let us see another example of loop.

Problem Statement:
Write a program that prints all the even numbers
from 1 to 100.

We need to check whether each number in the loop
is divisible by 2. Here we can use if statement.
"""
count = 2 #start of the loop
# as 1 is not even, we're not starting from it.
# why to check if we already know about it.

while count <= 100: # terminating condition
	if count%2 == 0:
		print(count)
	count = count + 1 # note the indentation
	# the above statement is outside if and within while
	# step
