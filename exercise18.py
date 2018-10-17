"""
Let's modify previous program to get what we want as output.

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
	print(str(number1)+' is greater than '+str(number2))

	# what is str?
	# don't worry in the next set of exercises we're going too deep
	# into it.
else:
	print(number2)
	print(' is greater than ')
	print(number1)

# don't change else, to see the difference.