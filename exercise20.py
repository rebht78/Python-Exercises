"""
In the previous exercise, we got an error
while adding 'str' and 'int'

So, how to add or concatenate 'str' and other non-string type
We need to convert non-string type to sting using str function.

Let us see an example of it.
"""
# let us change the values

name = 'Sherlock ' # added a space
age = 32

# let us try again to concatenate name and age
# using str
details = name + str(age) # only age requires conversion
print(details)
