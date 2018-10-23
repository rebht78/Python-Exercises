"""
We can access more than one elements using index range.

Suppose a list name is countries.

we can access elements like countries[startindex:endindex]

startindex: starting of index
endindex: till endindex-1

Let's see an example
"""
countries = ['USA','Canada','India','Russia','United Kingdom'];

print(countries[1:3]) # start from index:1 till 2
# will print 'Canada', 'India'

print(countries[1:]) # start from index:1 till the end of the list
# will print Canada','India','Russia','United Kingdom'

# print the whole list
print(countries[:])
