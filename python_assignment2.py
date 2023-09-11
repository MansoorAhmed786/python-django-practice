# 1. Print the following pattern using for loop:
# A) 
# **********
# **********
# **********
# **********
for i in range(0,4):
    for j in range(0,10):
        print("*",end='')
    print()

# Output
# **********
# **********
# **********
# **********

###############################
#Print the following
# 1 2 3 4 5 6 7 8 9 10
for i in range(1,11):
    print(i,end=' ' )
print()

#Output
# 1 2 3 4 5 6 7 8 9 10

#Print the following
# 2 4 6 8 10 12 14 16 18 20
for i in range(2,21,2):
    print(i,end=' ' )
print()

#Output
# 2 4 6 8 10 12 14 16 18 20 

#Print the following
# 3 6 9 12 15 18 21 24 27 30
for i in range(3,31,3):
    print(i,end=' ' )
print()

#Output
# 3 6 9 12 15 18 21 24 27 30

#Print the following
# 4 8 12 16 20 24 28 32 36 40
for i in range(4,41,4):
    print(i,end=' ' )
print()

#Output
# 4 8 12 16 20 24 28 32 36 40

#Print the following
# 5 10 15 20 25 30 35 40 45 50

for i in range(5,51,5):
    print(i,end=' ' )
print()
#Output
# 5 10 15 20 25 30 35 40 45 50

#Print the following
# 1
# 1 2
# 1 2 3
# 1 2 3 4
# 1 2 3 4 5

for i in range(1,6):
    for j in range(1,i+1):
        print(j,end =' ')
    print()

# 2. Write a Python program to multiplies all the items in a list.
list1=[1,2,3,4,5,6]
result=list1[0]
for i in range(1,len(list1)):
    result*=list1[i]

print(result)
# Output
# 720


# 3. Write a Python program to get the smallest number from a list.
list2=[5,7,8,1,4,9]
minimum= min(list2)
print(minimum)

# 4. Write a Python program to remove duplicates from a list
list3=[5,7,8,9,1,1,5,5,7,8,9,7]
new_list=list(set(list3))
print(new_list)
# Output
# 1

# 5. Write a Python program to clone or copy a list.
copy_list=list3
print(copy_list)
#Output
#[5, 7, 8, 9, 1, 1, 5, 5, 7, 8, 9, 7]

# 6. Write a Python program to print a specified list after removing the 0th, 4th and 5th elements.
# Sample list: ['Red','Green','White','Black','Pink','Yellow']
# Executed Sample: ['Green','White','Black']

sample_list =  ['Red','Green','White','Black','Pink','Yellow']
sample_list.pop(5)
sample_list.pop(4)
sample_list.pop(0)
print(sample_list)
#Output
#['Green', 'White', 'Black']