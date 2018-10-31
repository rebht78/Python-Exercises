"""
We have completed 42 exercises in Python.

We have learn variables, datatypes, strings and functions.

Let's move forward with some of the operations with string.

In this set of exercises 43 to 46, we'll be dealing with
various string operations from comparison to methods.

Let's see examples of it.
"""
# before using string, I want to introduce one more function
# raw_input() that helps us in taking inputs from the user.
words = raw_input('Enter any word: ')

if words == 'sherlock':
	print('Game is ON, Sherlockian')
# elif when the condition of if is false, then elif will be checked
elif words == 'moriarty':
	print('Did you miss me?')
# elif condition is false, then else part will get executed
else:
	print('Enter some other word, Watson!')