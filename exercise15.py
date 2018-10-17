"""
Till now, we've created sequential programs.
In sequential programs, statements are executed one after another.

But what if we need to execute some statements based on condition.

Let's understand it with a scenario:

Suppose we need to display various messages according to password 
length.

If password length is greater than 10, we'll show 'Strong'
If password length is greater than 6 but less than 10, we want to show
'Medium'
else we need to show 'Weak'.

How can we write such a program?

Python has conditional statements for such kind of scenario.

Let's see the syntax of it:

if [condition]:
	[statement]

notice the indent in the above syntax.

Let's write the program using if block
"""
number = 20
# logic for finding even or odd
if number%2 == 0: 
# if the number when divided by 2 returns remainder as 0
# then it's Even
	print('Even')
print('Out of if statement!')

# change the value of number to odd numbers
# and check whether output is getting printed or not.
