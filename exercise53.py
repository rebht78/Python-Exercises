"""
There are some built-in functions (not methods) that help us 
in performing some quick operations on list.

Let's see example of them all.
"""
numbers = range(2,200)
# you know what range function does, right?

print('The length of gen. numbers is '+str(len(numbers)))

# using function chaining....
# len will return as length of numbers and
# str will convert int to str for concatenation

print('The max of gen. numbers is '+str(max(numbers)))

print('The min of gen. numbers is '+str(min(numbers)))

print('The sum of gen. numbers is '+str(sum(numbers)))
