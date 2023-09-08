#we create a simple function and pass the parameter to the fucntion
#but in lamda we use lambda and give implementatio

square = lambda n : n**2

print(square(5))

#if else using lambda
maximum = lambda x,y :x if x > y else y
print(maximum(6,11))

#loop using lambda
count1 = 5

decrement = lambda x: x - 1

while count1 > 0:
    print("Countdown:" ,count1)
    count1 = decrement(count1)



#######################################
#Maps
#map is used to run on whole list instead of loop
#combination of map and lambda
square = lambda x :x**2
numbers = [1, 2, 3, 4, 5]


squared_numbers = map(square, numbers)

for i in squared_numbers:
    print(i)

########################################################
#Filter
#Filter is used to filter using given condition
is_even= lambda x: x % 2==0

# Create a list of numbers
numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
even_numbers = filter(is_even, numbers)

for i in even_numbers:
    print(i)




#########################################
#If else in single line
x=5
is_even = True if x/2==0 else False
print(is_even)


##################################
#if else if in single line
x = 9
result = "Even" if x % 2 == 0 else "Divisible by 3" if x % 3 == 0 else "Odd"
print(result)

#################################
#For loop in single line
squared_numbers = [x**2 for x in range(1, 6)]
print(squared_numbers) 

################################3
#if else for loop in single line
#in range first parameter is starting point second parameter is ending point and thurd parameter is interval
result = [True if x % 2 == 0 else False for x in range(1,20,3)]
print(result)
 
