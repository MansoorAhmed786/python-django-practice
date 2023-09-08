###################################
# Simple Iterator using iret and next

mylist=["my","name","is","Mansoor","Ahmed"]
iterator = iter(mylist)

print(next(iterator))
print(next(iterator))
print(next(iterator))
print(next(iterator))
print(next(iterator))

#####################################
#Iterator using for loop

for i in mylist:
    print(i)



#########################################
# Customized Iterator
class MyNumbers:
  def __iter__(self):
    self.a = 1
    return self

  def __next__(self):
    x = self.a
    self.a += 1
    return x
#for stopiteration we will raisa
        #StopIteration

myclass = MyNumbers()
iterator1 = iter(myclass)

print(next(iterator1))
print(next(iterator1))
print(next(iterator1))
print(next(iterator1))
print(next(iterator1))



#######################################
# Another python customized iterator
#It will double each number
class PowTwo:

    def __init__(self, max=0):
        self.max = max

    def __iter__(self):
        self.n = 0
        return self

    def __next__(self):
        if self.n <= self.max:
            result = 2 ** self.n
            self.n += 1
            return result



numbers = PowTwo(3)

# create an iterable from the object
i = iter(numbers)

print(next(i)) 
print(next(i)) 
print(next(i)) 
print(next(i)) 
print(next(i)) 