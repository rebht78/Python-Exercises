"""
Let's do two more if...else programs to get used to new syntax 
of Python.

Problem Statement:
Write a program that display max of two numbers

Sample Input/Output:
3
5
5 is greater than 3

Let's write the program using if...else block
"""
number1 = 3
number2 = 5

if number1 > number2:
	# three statements in if...it is valid!
	print(number1)
	print(' is greater than ')
	print(number2)
else:
	print(number2)
	print(' is greater than ')
	print(number1)

# output is not what we expected, but we are getting there...