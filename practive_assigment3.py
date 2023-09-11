# Implement a function that meets the specification below. Use a try-except block.
# def sumDigits(s):

# """Assumes s is a string
# Returns the sum of the decimal digits in s
# For example, if s is 'a2b3c' it returns 5"""

def sumDigit(s):
    sum=0
    try:
        for i in range(len(s)):
            if s[i].isdigit():
                sum+=int(s[i])
    except ValueError:
        pass   
    finally:
        return sum
    
inp=input("Enter String: ")
print(sumDigit(inp))

# Enter String: a2b3b3j3j
# 11


# With a given integer number n provided by the user, write a program to generate a dictionary
# that contains {i: i*i} as its key:value pair such that all the integer numbers between 1
# and n are included). At the end, your program should print the dictionary. Suppose the
# following input is supplied to the program:
# Enter a Number: 8
# Then, the output should be:
# {1: 1, 2: 4, 3: 9, 4: 16, 5: 25, 6: 36, 7: 49, 8: 64}

mydict={}
num=int(input("Enter Number: "))
for i in range(1,num+1):
    mydict[i]=i*i
print(mydict)

# Enter Number: 12
# {1: 1, 2: 4, 3: 9, 4: 16, 5: 25, 6: 36, 7: 49, 8: 64, 9: 81, 10: 100, 11: 121, 12: 144}


# Write a program that accepts a comma separated sequence of words as input and prints the
# words in a comma-separated sequence after sorting them alphabetically. Suppose the
# following input is supplied to the program:
# without,hello,bag,world
# Then, the output should be:
# bag,hello,without,world

string=input("Enter Comma Seperated String: ")
newstring=string.split(',')
newstring.sort()
print(newstring)

# Enter Comma Seperated String: mansoor,ahmed,talha
# ['ahmed', 'mansoor', 'talha']