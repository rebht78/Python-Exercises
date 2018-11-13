"""
3. pop() : pop is used to delete elements from the list, if you know
the index of the element you want to delete.

Let's see an example of pop() method.
"""
fav_fruits = ['apples','oranges','pears','bananas','pineapples']

# printing favorite fruits
print(fav_fruits)

# using pop to delete pears
pears = fav_fruits.pop(2) # index of pears is 2

# printing the sorted list
print(fav_fruits)