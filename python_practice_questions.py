#1. Write a Python program which accepts the user&#39;s first and last name and print them in
# reverse order with a space between them

first_name=input("Enter First Name: ")
last_name=input("Enter Last Name: ")
print(last_name,first_name)

# Enter First Name: mansoor
# Enter Last Name: ahmed-ass
# ahmed mansoor

# Write a Python program to display the first and last colors from the following list. 
# color_list = ['Red','Green','White' ,'Black']

color_list = ['Red','Green','White' ,'Black']
print(color_list[0])
print(color_list[len(color_list)-1])

# Red
# Black

# Write a Python program to get the difference between a given number and 17, if the
# number is greater than 17 return double the absolute difference.

num=int(input("Enter Number: "))
if num<17 :
    print(17-num)
else:
    print((num-17)*2)

#Enter Number: 1
#16

# Write a Python program to calculate the sum of three given numbers, if the values are
# equal then return thrice of their sum

num1=18
num2=18
num3=18
if num1==num2==num3:
    print(3*(num1+num2+num3))
else:
    print(num1+num2+num3)

# 162

# Write a Python program to count the number 4 in a given list.
list1=[1,5,7,8,9,4,4,4,5,6,4,4,4,5,4,7]
count=0
for i in range(0,len(list1)):
    if list1[i]==4:
        count+=1
print(count)

# 7


# Print table of 24, 50 and 29 using loop.
for i in range(10):
    print((i+1)*24,(i+1)*50,(i+1)*29)

# 24 50 29
# 48 100 58
# 72 150 87
# 96 200 116
# 120 250 145
# 144 300 174
# 168 350 203
# 192 400 232
# 216 450 261
# 240 500 290

# Print the following patterns using loop :
# a.
# *
# **
# ***
#****

for i in range(4):
    for j in range(i+1):
        print('*',end='')
    print()

# *
# **
# ***
# ****
