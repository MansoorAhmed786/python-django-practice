# Write a program that asks the user to enter two numbers, obtains them from the user and
# prints their sum, product, difference, quotient and remainder.


num1=int(input("Enter First Number: "))
num2=int(input("Enter Second Number: "))
print("Sum: ",num1+num2)
print("Product: ",num1*num2)
print("Remainder: ",num1//num2)
print("Quotient: ",num1%num2)
# Enter First Number: 5
# Enter Second Number: 2
# Sum:  7
# Product:  10
# Remainder:  2
# Quotient:  1

# The distance between two cities (in km.) is input through the keyboard. Write a program
# to convert and print this distance in meters, feet, inches and centimeters.

distance=int(input("Enter distance: "))
print("In Meters: ",distance*1000)
print("In Inches: ",distance*39370)
print("In feet: ",distance*3280.84)
print("In Centimeter: ",distance*100000)

# Enter distance: 1
# In Meters:  1000
# In Inches:  39370
# In feet:  3280.84
# In Centimeter:  100000

# Write a program that takes the marks obtained by a student in five different subjects as
# input through the keyboard, then find out the total marks and percentage marks obtained
# by the student in each subject. Assume that the maximum marks that can be obtained by a
# student in each subject is 100.

sub1 =int(input("Enter marks of first subject: "))
sub2 =int(input("Enter marks of Second subject: "))
sub3 =int(input("Enter marks of Third subject: "))
sub4 =int(input("Enter marks of forth subject: "))
sub5 =int(input("Enter marks of fifth subject: "))
total_marks=5*100
obtained_marks=sub1+sub2+sub3+sub4+sub5
print(obtained_marks)
percentage1=(obtained_marks*100)/total_marks
print(percentage1)

# Enter marks of first subject: 100
# Enter marks of Second subject: 80
# Enter marks of Third subject: 80
# Enter marks of forth subject: 75
# Enter marks of fifth subject: 65
# 400
# 80.0

# Temperature of a city in Fahrenheit degrees is input through the keyboard. Write a
# program to convert this temperature into Centigrade degrees.
temprature=int(input("Enter temprature in Farenhiet: "))
print("Temprature in Celsius: ",(temprature - 32) * 5/9)

# The length & breadth of a rectangle are input through the keyboard. Write a program to
# calculate the area & perimeter of the rectangle.
length=int(input("Enter Length of rectange: "))
width=int(input("Enter Width of rectange: "))
print("Area of rectange is: ",length*width)
print("Area of rectange is: ",2*(length+width))

# Two numbers (base and exponent) are entered through the keyboard. Write a program to
# find the value of base raised to the power of exponent.
exponent=int(input("Enter Exponent: "))
base=int(input("Enter Base: "))
print("Power is: ",exponent**base)

# If a five-digit number is input through the keyboard, write a program to calculate the sum
# of its digits. (Hint: Use the modulus operator „%‟ to split the digits).
num3=int(input("Enter number: "))
sum=0
for i in range(0,5):
    sum+=num3%10
    num3=num3//10
print(sum)

# Enter number: 12345
# 15

# Write a program that reads in the radius of a circle and prints the circle‟s diameter,
# circumference and area. Use the constant value 3.14159 for pi. Perform each of these
# calculations inside the print statement(s) and use the conversion format specifier %f.
pi=3.14159
radius=int(input("Enter Radius: "))
print("Diameter is: ",radius*2)
print("Circumference is: ",2*pi*radius)
print("Area is: ",pi*radius*radius)

# Enter Radius: 1
# Diameter is:  2
# Circumference is:  6.28318
# Area is:  3.14159

# A company insures its drivers in the following cases:
# − If the driver is married.
# − If the driver is unmarried, male & above 30 years of age.
# − If the driver is unmarried, female & above 25 years of age.
# In all other cases, the driver is not insured. If the marital status, sex and age of the driver
# are the inputs, write a program to determine whether the driver is to be insured or not.

status=input("Enter martial status m for married and u for unmarried: ")
sex=input("Enter m for Male or f for Female : ")
age=int(input("Enter Age: "))
if status=='m':
    print("You are Insured")
elif status=='u' and sex =='m' and age>30:
     print("You are Insured")
elif status=='u' and sex =='f' and age>25:
    print("You are Insured")
else:
    print("You are not secured")

# Enter martial status m for married and u for unmarried: u
# Enter m for Male or f for Female : m
# Enter Age: 36
# You are Insured

# Write a program that take year as an input from user. Determine whether year is leap year
# or not.

year=int(input("Enter year: "))
if year % 4 == 0 and year % 100 != 0 or year % 400 == 0:
    print("This is a leap year")
else:
    print("This is not a leap year")

# Enter year: 2000
# This is a leap year


# Write a program that reads an integer and determines and prints whether it‟s odd or even.
num4=int(input("Enter Number: "))
if num4%2==0:
    print("This is even number")
else:
    print("This is an odd number")

# Enter Number: 5
# This is an odd number


# Write a program that reads in two integers and determines and prints whether the first is a
# multiple of the second. [Hint: Use the remainder operator.

num5=int(input("Enter First  Number: "))
num6=int(input("Enter Second Number: "))
if num5%num6==0:
    print("Second Number multiple of first number")
else:
    print("Not a Multiple")

# EnterFirst  Number: 5
# Enter Second Number: 2
# Not a Multiple

# Write a program that asks the user to enter two integers, obtains the numbers from the
# user, then prints the larger number followed by the words “is larger.” If the numbers are
# equal, print the message “These numbers are equal.” Use only the single-selection form
# of the if statement you learned in this chapter.
num7=int(input("Enter First  Number: "))
num8=int(input("Enter Second Number: "))
if num7>num8:
    print(num7,"is greater than ", num8)
elif num7==num8:
    print("Both numbers are equal")
else:
    print(num8 ," is greater than ",num7)

# Enter First  Number: 5
# Enter Second Number: 2
# 5 is greater than  2

# Write a program that inputs three different integers from the keyboard (i.e num1, num2,
# num3), then prints the sum, the average, the product, the smallest and the largest of these
# numbers. The screen dialogue should appear as follows:


# (Body Mass Index Calculator) We introduced the body mass index (BMI) calculator in
# The formulas for calculating BMI are
# BMI = (weightInKilograms) / (heightInMeters * heightInMeters)
# Create a BMI calculator application that reads the user‟s weight in kilograms and height
# in meters, then calculates and displays the user‟s body mass index. Also, the application

# should display the following information from the Department of Health and Human
# Services/National Institutes of Health so the user can evaluate his/her BMI:


weight_kg = float(input("Enter your weight in kilograms: "))
height_m = float(input("Enter your height in meters: "))
bmi = weight_kg / (height_m ** 2)
if bmi < 18.5:
    print( "Underweight")
elif 18.5 <= bmi < 24.9:
    print( "Normal")
elif 25 <= bmi < 29.9:
    print( "Overweight")
else:
    print( "Obese")

# Enter your weight in kilograms: 65
# Enter your height in meters: 5.11
# Underweight

# Write a program to check whether a triangle is valid or not, when the three angles of the
# triangle are entered through the keyboard. A triangle is valid if the sum of all the three
# angles is equal to 180 degrees.

num9=int(input("Enter first angle: "))
num10=int(input("Enter Second angle: "))
num11=int(input("Enter Third angle: "))
if num9+num10+num11 ==180:
    print("It is a valid triangle")
else:
    print("It is not a valid triangle")


# Given the length and breadth of a rectangle, write a program to find whether the area of
# the rectangle is greater than its perimeter. For example, the area of the rectangle with
# length = 5 and breadth = 4 is greater than its perimeter.
num12=int(input("Enter length: "))
num13=int(input("Enter Width: "))
if num13*num12 > 2*(num12+num13):
    print("Area is greater")
else:
    print("Perimeter is greater")

# A library charges a fine for every book returned late. For first5 days, the fine is 50 paise,
# for 6-10 days fine is one rupee and above 10 days fine is 5 rupees. If you return the book
# after 30days your membership will be cancelled. Write a program to accept the number
# of days the member is late to return the book and display the fine or the appropriate
# message.

days_late = int(input("Enter the number of days late: "))

fine = 0

if days_late <= 5:
    fine = 0. * days_late  
elif 6 <= days_late <= 10:
    fine = 1 * days_late  
else:
    fine = 5.00  
if days_late > 30:
    print("Your membership is canceled due to returning the book more than 30 days late.")
else:
    print(f"Fine for {days_late} days late: Rs. {fine:.2f}")


# If the three sides of a triangle are entered through the keyboard, write a program to check
# whether the triangle is isosceles, equilateral, scalene or right-angled triangle.
# Input the lengths of the three sides of the triangle
num14 = float(input("Enter the length of the first side: "))
num15 = float(input("Enter the length of the second side: "))
num16 = float(input("Enter the length of the third side: "))

if num14 + num15 > num16 and num14 + num15 > num16 and num14 + num15 > num16:
    if num14 == num15 == num16:
        print("equilateral triangle.")
    elif num14 == num15 or num14 == num16 or num14 == num16:
        print("isosceles triangle.")
    elif num14**2 == num15**2 + num16**2 or num15**2 == num14**2 + num16**2 or num16**2 == num16**2 + num15**2:
        print("right-angled triangle.")
    else:
        print("scalene triangle.")
else:
    print("Invalid triangle.")

# Enter the length of the first side: 1
# 1Enter the length of the second side: 1
# Enter the length of the third side: 1
# equilateral triangle.

# A university has the following rules for a student to qualify for a degree with A as the
# main subject and B as the subsidiary subject:
# (a) He should get 55 percent or more in A and 45 percent or more in B.
# (b) If he gets than 55 percent in A he should get 55 percent or more in B. However, he
# should get at least 45 percent in A.
# (c) If he gets less than 45 percent in B and 65 percent or more in A he can reappear in an
# examination in B to qualify.
# (d) In all other cases he is declared to have failed.

percentage_A = float(input("Enter the percentage marks for subject A: "))
percentage_B = float(input("Enter the percentage marks for subject B: "))

if percentage_A >= 55 and percentage_B >= 45:
    print("Congratulations!")
elif percentage_A >= 55 and percentage_B >= 55:
    print("Congratulations!.")
elif percentage_A >= 65 and percentage_B < 45:
    print("You can reappear in an examination for subject B to qualify.")
else:
    print("You have not met the qualification criteria. You have failed.")

# Enter the percentage marks for subject A: 55
# Enter the percentage marks for subject B: 60
# Congratulations!


# 21. Write a program that calculates the squares and cubes of the numbers from 0 to 10 and
# uses tabs to print the following table of values:
# number square cube
# 0 0 0
# 1 1 1
# 2 4 8
# 3 9 27
# 4 16 64
# 5 25 125

for i in range(11):
    print(i,i*i,i*i*i)

# 0 0 0
# 1 1 1
# 2 4 8
# 3 9 27
# 4 16 64
# 5 25 125
# 6 36 216
# 7 49 343
# 8 64 512
# 9 81 729
# 10 100 1000

# Write a program that calculates and prints the sum of the even integers from 2 to 30.
sum=0
for i in range(2,31,2):
    sum+=i
print(sum)

# 240

# Write a program to enter the numbers till the user wants and at the end it should display
# the count of positive, negative and zeros entered.
pos=0
neg=0
zer=0
numb=int(input("Enter Number or -99999 to quit: "))
if numb>0:
    pos+=1
elif numb<0:
    neg+=1
else:
    zer+=1
while(numb!=-99999):
    numb=int(input("Enter Number or -99999 to quit: "))
    if numb>0:
        pos+=1
    elif numb<0:
        neg+=1
    else:
        zer+=1

print("Positive are: ",pos)
print("Negative are: ",neg)
print("Zeros are: ",zer)


nu = int(input("Enter a decimal number: "))
binary_equivalent = bin(nu)
binary_equivalent = binary_equivalent[2:]
print(f"The binary equivalent of {nu} is: {binary_equivalent}")

# Enter a decimal number: 55
# The binary equivalent of 55 is: 110111


numbers = input("Enter a list of numbers separated by spaces: ").split()
numbers = [int(num) for num in numbers]


if not numbers:
    print("The list is empty. Cannot calculate the range.")
else:
    smallest = numbers[0]
    largest = numbers[0]
    for num in numbers:
        if num < smallest:
            smallest = num
        elif num > largest:
            largest = num
    range = largest - smallest
    print("The range of the numbers is:" ,range)


# Write a program to generate all combinations of 1, 2 and 3 using for loop.

for num1 in range(1, 4):
    for num2 in range(1, 4):
        for num3 in range(1, 4):
            print(num1, num2, num3)


# Develop a program that will determine the gross pay for each of several employees. The
# company pays “straight time” for the first 40 hours worked by each employee and pays
# “time-and-a-half” for all hours worked more than 40 hours. You‟re given a list of the
# employees of the company, the number of hours each employee worked last week and the
# hourly rate of each employee. Your program should input this information for each
# employee and should determine and display the employee's gross pay. Here is a sample
# input/output dialog:
# Enter # of hours worked (-1 to end): 39
# Enter hourly rate of the worker ($00.00): 10.00
# Salary is $390.00
# Enter # of hours worked (-1 to end): 40
# Enter hourly rate of the worker ($00.00): 10.00
# Salary is $400.00
# Enter # of hours worked (-1 to end): 41

# Enter hourly rate of the worker ($00.00): 10.00
# Salary is $415.00
# Enter # of hours worked (-1 to end): -1


employee_data = []
while True:
    hours_worked = float(input("Enter # of hours worked (-1 to end): "))
    if hours_worked == -1:
        break

    hourly_rate = float(input("Enter hourly rate of the worker ($00.00): "))
    if hours_worked <= 40:
        gross_pay = hours_worked * hourly_rate
    else:
        overtime_hours = hours_worked - 40
        gross_pay = (40 * hourly_rate) + (overtime_hours * (hourly_rate * 1.5))
    employee_data.append((hours_worked, hourly_rate, gross_pay))

for i, (hours, rate, pay) in enumerate(employee_data, start=1):
    print(f"Salary for Employee {i}: ${pay:.2f}")

# Enter # of hours worked (-1 to end): 5
# Enter hourly rate of the worker ($00.00): 5.6
# Enter # of hours worked (-1 to end): -1
# Salary for Employee 1: $28.00

# The factorial of a non negative integer n is written n! (pronounced “n factorial”) and is
# defined as follows:
# n! = n · (n - 1) · (n - 2) · ... · 1 (for values of n greater than or equal to 1)
# and n! = 1 (for n = 0).
# For example, 5! = 5 · 4 · 3 · 2 · 1, which is 120.

nu1=int(input("Enter nnumber: "))
if nu1 < 0:
    print("Factorial is not for negative numbers.")
elif nu1 == 0:
    print("1")
else:
    result = 1
    for i in range(1, nu1 + 1):
        result *= i
    print(result)

# Enter nnumber: 6
# 720

# Write a program to produce the following output using loop:

# 1
# 2 3
# 4 5 6
# 7 8 9 10

for i in range(1,11):
    for j in range(1,4):
        print(i*"   ",i,end='   ')
        break

# Write a program that takes the side of a square from user and then prints that square out
# of asterisks. Your program should work for squares of all side sizes between 1 and 20.
# For example, if your program reads a size of 4, it should print
# ****
# ****
# ****
# ****
number1=int(input("Enter Number from 1 to 20: "))
for i in range(0,number1):
    for j in range(0,number1):
        print("*",end='')
    print()

# Enter Number from 1 to 20: 5
# *****
# *****
# *****
# *****
# *****

# Write a program that prints the following diamond shape. You may use print statements
# that print either a single asterisk (*) or a single blank. Maximize your use of repetition
# (with nested for statements) and minimize the number of print statements.
# *
# ***
# *****
# *******
# *********
# *******
# *****
# ***
# *


for i in range(1,10,2):
    for j in range(0,10):
        print(i*"*")
        break
for k in range(9,0,-2):
    print(k*"*")

# *
# ***
# *****
# *******
# *********
# *********
# *******
# *****
# ***
# *
