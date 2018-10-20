"""
In the previous exercise, we just need to print from 1 to 5

Let's say we need to print from 1 to 1000, 
we can't write print statement 1000 times.

Loops for rescue!

Loops as defined earlier repeats itself until the condition is true.

Loops has three parts:
1. start of the loop
2. step to be taken to get closer to terminating condition
3. terminating condition

in the example discussed above,
start = 1
step = +1
terminating condition = 1000

Loop syntax is given with example
"""
count = 1
# start of the loop

while count <= 100: # terminating condition
	# note that it is a block, so indent it
	print(count)
	count = count + 1
print("End of Loop!")
