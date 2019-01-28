## DECORATORS ##

import time

def timing_function(some_function):
	def wrapper():
		t1 = time.time()
		some_function()
		t2 = time.time()
		print("The time it took to run the function:" +str((t2-t1)) + "\n")
	return wrapper
	

def my_function():
	num_list = []
	for num in range(0,1000):
		num_list.append(num)
	print("\n Sum of all numbers: "+ str((sum(num_list))))
	
	
wrapped_func = timing_function(my_function)
wrapped_func()


import time

def timing_function1(some_function):
	def wrapper():
		t1 = time.time()
		some_function()
		t2 = time.time()
		print("The time it took to run the function:" +str((t2-t1)) + "\n")
	return wrapper
	

@timing_function1
def my_function1():
	num_list = []
	for num in range(0,1000):
		num_list.append(num)
	print("\n Sum of all numbers (using decorators): "+ str((sum(num_list))))
	
	
my_function1()



# Output
# Sum of all numbers: 499500
# The time it took to run the function:0.0009407997131347656

# Sum of all numbers (using decorators): 499500
# The time it took to run the function:0.0010020732879638672

