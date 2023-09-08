#python decorators

def decorated_function(func):
    def inside_decorator():
        print("I am inside decorator")
        func()
    return inside_decorator

def simple_function():
    print("I am Outside decorator")

#making instance
decorated_func = decorated_function(simple_function)

# call the decorated function
decorated_func()

#we can use '@' symbol to make deecorated function


###############################################################
#chained decorators
def first_function(func):
    def inner(intt):
        print("In first Function  Before Function Execution")
        func(intt)
        print("In first Function  After Function Execution" )
    return inner


def second_function(func):
    def inner(intt):
        print("In Second Function  Before Function Execution" )
        func(intt)
        print("In Second Function  After Function Execution")
    return inner


@first_function
@second_function
def final_function(msg):
    print(msg)

final_function("Hello")


###########################################
#Parameterized Decorator:
# Create a decorator @repeat(n) that repeats the decorated function n times.
# It should also accept an argument for whether to print the results each time.
# Apply this decorator to a simple function


def repeat(n):
    def decorator_function(func):
        def inner_function(val1, val2):
            results = []
            for i in range(n):
                result = func(val1, val2)
                results.append(result)
                print(result)
                if i < n - 1:
                    user_input = input("Print results again? (y/n): ")
                    if user_input != 'y':
                        break
            return results
        return inner_function
    return decorator_function

# Apply the decorator to a simple function
@repeat(n=3)
def add(a, b):
    return a + b

add(2, 3)

##################################################
# Timing Decorator:
# Write a decorator @timing that measures the time it takes 
# for a function to execute and prints the execution time. 
# Apply this decorator to various functions and compare their execution times.

import time

def timing_decorator(func):
    def inner_function():
        start_time = time.time()
        result = func()
        end_time = time.time()
        execution_time = end_time - start_time
        print(execution_time)
        return result
    return inner_function

# Apply the @timing decorator to various functions
@timing_decorator
def first_function():
    time.sleep(2)

@timing_decorator
def second_function():
    time.sleep(2)

first_function()
second_function()



###################################################
# Basic Decorator:
# Create a decorator called @uppercase_decorator
# that converts the result of a function to uppercase. 
# Apply this decorator to a function that returns a string and test it.

def uper_case(func):
    def inner_function(name):
        name_uper=name.upper()
        return name_uper
    return inner_function

@uper_case
def uper_case(name):
    return name


input1 = uper_case(input("Enter String: "))
print (input1)


###############################################
#Class Based Custom Decorator

from time import time
class Timer:

	def __init__(self, func):
		self.function = func

	def __call__(self,val):
		start_time = time()
		result = self.function(val)
		end_time = time()
		time_total=end_time-start_time
		print(time_total)
		return result


# adding a decorator to the function
@Timer
def some_function(delay):
	from time import sleep

	sleep(delay)

# calling the function
some_function(3)