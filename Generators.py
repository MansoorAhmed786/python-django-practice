#Simple Generator

def simpleGenerator():
	yield 1			
	yield 2			
	yield 3			

for value in simpleGenerator():
	print(value)


##################################3
#Generator using Iterator



def simpleGenerator1():
	yield 1
	yield 2
	yield 3


x = simpleGenerator1()


print(next(x))
print(next(x))
print(next(x))


####################################
#Generator for square function
#Easy to implement
def PowTwoGen(max=0):
    n = 0
    while n < max:
        yield 2 ** n
        n += 1

for i in PowTwoGen(5):
	print(i)