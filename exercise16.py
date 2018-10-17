"""
In the previous exercise, we've seen if block.

In this exercise, we'll learn about if...else

if the condition is true, statement within if will get executed
if the condition is false, else part will get executed

Let's see the syntax of it:

if [condition]:
	[statement]
else:
	[statement]
notice the indent in the above syntax.

Let's write the program using if...else block
"""
number = 20
# logic for finding even or odd
if number%2 == 0: 
# if the number when divided by 2 returns remainder as 0
# then it's Even
	print('Even')
else:
	print('Odd!!!')
print('Out of if statement!')

# change the value of number to odd numbers
# to execute else block.
