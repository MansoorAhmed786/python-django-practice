#File handling
# Open a file in read mode
file_name = input("Enter file name you want to read: ")
# r will open this file in read mode
file = open(file_name, "r")
# Read the entire file
content = file.read()
print(content)
# Read a single line
# line = file.readline()
# print(line)
# Read all lines into a list
lines = file.readlines()
print(lines)
# Open a file in write mode
# w will open this file in write mode
file_name = input("Enter file name you want to write: ")
file = open(file_name, "w")
#if we open with a it will append the file

# Write a single line if we use write
file.write("Hello, World!\n")


line1 = input("Enter Line 1 you want to read in file: ")
line2 = input("Enter Line 2 you want to read in file: ")

lines = [line1, line2]
# Write multiple lines from a list if we use writelines
file.writelines(lines)
