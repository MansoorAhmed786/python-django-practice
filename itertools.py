#Simple itertools upto specific count

#print the first four even numbers
import itertools

result = itertools.count(start = 0, step = 2)

for number in result:
# termination condition
    if number < 8:
        print (number)
    else:
        break

#Cycle Iterator

result = itertools.cycle('12345')
counter = 0

for number in result:
# termination condition
    if counter < 10 :
        print (number)
        counter = counter + 1
    else:
        break


#Repeat Iterator

result = itertools.repeat('hello', times = 2)

for i in result:
    print (i)

# Chain Iterator
#this will combine all lists and iterate them

list1 = ['a', 'b', 'c']
list2 =['d', 'e', 'f']
list3 = ['1', '2', '3']

result = itertools.chain(list1, list2, list3)

for element in result:
  print (element)

#Compress Iterator

names = ['Alice', 'James', 'Matt']
have_flu = [True, True, False]

result = itertools.compress(names, have_flu)

for element in result:
  print (element)