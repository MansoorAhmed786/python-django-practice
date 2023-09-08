# practice of functools

from functools import partial

#that will create a simple functiion
def power(a, b):
	return a**b


# partial functions from functools
#that will fix the second parameter
pow2 = partial(power, b=2)
pow4 = partial(power, b=4)
pow5 = partial(power, 5)

#this will call simple power function
print(power(2, 3))  
#this will call pow2 partial function whos first parameter is given and second parameter is 2
print(pow2(4))
#this will call pow4 partial function whos first parameter is given and second parameter is 3
print(pow4(3))
#this will call pow5 partial function whos first parameter is given and second parameter is 5
print(pow5(2))



#if we want to call pow2 function without default parameter have to use func keyword
print('func used in partial function pow2 :', pow2.func(4,5))
#keywords is used to return default values
print('Default keywords for pow2 :', pow2.keywords)
#args is used to return arguments of function
print('Default arguments for pow5 :', pow5.args)


#######################################################
#Partial methods using class
from functools import partialmethod

class Demo:
	def __init__(self):
		self.color = 'black'

	def _color(self, type):
		self.color = type

	set_red = partialmethod(_color, type='red')
	set_blue = partialmethod(_color, type='blue')
	set_green = partialmethod(_color, type='green')


obj = Demo()
print(obj.color)
obj.set_blue()
print(obj.color)

######################################
#Functool total_ordering
#total ordering is a self called decorator which calls 
#__eq__ and some other functions life __lt__,__le__,__gt__ or __ge__
from functools import total_ordering

@total_ordering
class Number_comparision:
	#initialize the class
    #this is paremterized constructor of class
	def __init__(self, value):
		self.value = value
    #we must have to build this function for totall ordering
    #this function will automatically be called due to total_ordering
	def __eq__(self, other):
		return self.value == other.value


	def __gt__(self, other):
		return self.value > other.value
	def __it__(Self,other):
	    return self.value < other.value


print('6 > 2 :', Number_comparision(6)>Number_comparision(2))
print('3 < 1 :', Number_comparision(3)<Number_comparision(1))
print('2 <= 7 :', Number_comparision(2)<= Number_comparision(7))
print('9 >= 10 :', Number_comparision(9)>= Number_comparision(10))
print('5 == 5 :', Number_comparision(5)== Number_comparision(5))


###########################
#cache property
#it will store the pervios value as cache and reuse the value if needed

from functools import cache

@cache
#recusrive function
def factorial(n):
    return n * factorial(n-1) if n else 1

#this time no previous value is stored so it will run 11 times
print(factorial(10) )   
#this will return the cache information
print(factorial.cache_info())  
#as it  is needed for just 5 and we already have its value
print(factorial(5) )  
print(factorial.cache_info())     
#we have value upto 10 so it will run ruther 2 more times and use previous value
print(factorial(12) )  
print(factorial.cache_info())     

############################################
#Single Dispatch
#We can create function and overload the 
# function with the help of single distach


from functools import singledispatch


@singledispatch
#this function is for string
def fun(s):
	print(s)


#fun function is overloaded for interger
@fun.register(int)
def _(s):
	print(s * 2)
	
#fun function is again overloaded for float
@fun.register(float)
def _(s):
    print(s*10)


fun('Single Dispatch')
fun(10)
fun(5.6)


