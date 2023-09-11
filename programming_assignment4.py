# Convert a non-negative integer to its English words representation and print in
# reverse if total characters in English words are more than total words in a
# sentence.

def to_num(num):
    if num == 0:
        return "Zero"
    result = ""
    if num < 0:
        print("Your must write non negative integer")
        num1=int(input('Enter Number again: '))
        to_num(num1)

    below_20 = ["", "One", "Two", "Three", "Four", "Five", "Six", "Seven", "Eight", "Nine",
                "Ten", "Eleven", "Twelve", "Thirteen", "Fourteen", "Fifteen", "Sixteen", "Seventeen", "Eighteen", "Nineteen"]

    tens = ["", "", "Twenty", "Thirty", "Forty", "Fifty", "Sixty", "Seventy", "Eighty", "Ninety"]

    thousands = ["", "Thousand", "Million", "Billion"]

    def check(num):
        if num == 0:
            return ""
        elif num < 20:
            return below_20[num] + " "
        elif num < 100:
            return tens[num // 10] + " " + check(num % 10)
        else:
            return below_20[num // 100] + " Hundred " + check(num % 100)


    for i in range(len(thousands)):
        if num % 1000 != 0:
            result = check(num % 1000) + thousands[i] + " " + result
        num //= 1000

    return result

num = int(input("Enter a non-negative integer: "))
print("English Words:", to_num(num))

# Given an input n, count the total number of digit 1 appearing in all non-
# negative integers less than or equal to n.
# For example:
# Given n = 13,
# Return 6, because digit 1 occurred in the following numbers: 1, 10, 11, 12, 13.
def countDigitOne(n):
    count = 0
    for i in range(1,n+1):
        count += str(i).count('1')
    return count

n = 13
result = countDigitOne(n)
print("Total number of times digit 1 appears: ", result)

# Total number of times digit 1 appears: 6



# Given an array, Rotate (shift left) an array of n elements to the right by k steps.
# For example, with n = 7 and k = 3, the array [1,2,3,4,5,6,7] is rotated
# to [5,6,7,1,2,3,4].
# After rotating the array add in into another array and display array index with
# minumum value.
def rotate_array(nums, k):
    n = len(nums)
    k %= n  
    nums[:] = nums[-k:] + nums[:-k] 

original_array = [1, 2, 3, 4, 5, 6, 7]
k = 3
rotate_array(original_array, k)
result_array = []
result_array.extend(original_array)

min_index = result_array.index(min(result_array))

print("Rotated Array:", result_array)
print("Index with Minimum Value:", min_index)


# You are given an n x n 2D matrix representing an image.
# Rotate the image by 180 degrees (anti-clockwise) but after sorting the n*n 2D array

def rotate_180(image_matrix):

    flattened = [element for row in image_matrix for element in row]
    flattened.sort()

    n = len(image_matrix)
    sorted_matrix = [[0] * n for _ in range(n)]
    index = 0

    for i in range(n):
        for j in range(n):
            sorted_matrix[i][j] = flattened[index]
            index += 1

    rotated_matrix = [list(reversed(row)) for row in reversed(sorted_matrix)]

    return rotated_matrix


original_matrix = [
    [3, 2, 1],
    [6, 5, 4],
    [9, 8, 7]
]

rotated_result = rotate_180(original_matrix)
for row in rotated_result:
    print(row)


# Given a string containing just the characters '(' and ')', find the length of the longest
# and shortest valid (well-formed) parentheses substring.
# For "(()", the longest valid parentheses substring is "()", which has length = 2.
# Another example is ")()())", where the longest valid parentheses substring is "()()",
# which has length = 4.

def longestValidParentheses(s):
    stack = []
    longest = 0
    shortest = 0

    for i in range(len(s)):
        if s[i] == '(':
            stack.append(i)
        else:
            if stack and s[stack[-1]] == '(':
                stack.pop()
                if not stack:
                    shortest = max(shortest, i + 1)
                else:
                    shortest = max(shortest, i - stack[-1])
            else:
                stack.append(i)

    while stack:
        right = stack.pop()
        left = -1 if not stack else stack[-1]
        shortest = max(shortest, right - left)
    
    return shortest, longest

# Example usage:
s1 = "(()"
s2 = "()()"

shortest1, longest1 = longestValidParentheses(s1)
shortest2, longest2 = longestValidParentheses(s2)

print("For shortest valid parentheses substring length: ", shortest1)
print("For shortest valid parentheses substring length: ", shortest2)