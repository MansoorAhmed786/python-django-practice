# Write a program which should count Vowels in the strings and return vowels in
# reverse order.

def count_and_reverse_vowels(input_string):
    vowels = "AEIOUaeiou"
    vowel_count = 0
    reverse_vowels = []

    for char in input_string:
        if char in vowels:
            vowel_count += 1
            reverse_vowels.append(char)

    reverse_vowels.reverse()
    return vowel_count, ''.join(reverse_vowels)

input_string = "Hello, World!"
vowel_count, reversed_vowels = count_and_reverse_vowels(input_string)
print("Vowel Count:",vowel_count)
print("Reversed Vowels: ",reversed_vowels)

# Vowel Count: 3
# Reversed Vowels:  ooe


# Write a function which should add the two vowels in the arrays and generate
# third array
def add_vowels(arr1, arr2):
    third_array = arr1 + arr2
    return third_array

array1 = ["a", "e"]
array2 = ["i", "o"]
result_array = add_vowels(array1, array2)
print(result_array)

# Vowel Count: 3
# Reversed Vowels:  ooe
# ['a', 'e', 'i', 'o']

# Write a program to return the third and last largest number in the array.
def third_and_last_largest(numbers):
    if len(numbers) < 3:
        return "Array should have at least 3 elements."

    unique_numbers = list(set(numbers))  # Remove duplicates
    unique_numbers.sort(reverse=True)  # Sort in descending order
    third_largest = unique_numbers[2]
    last_largest = unique_numbers[0]

    return third_largest, last_largest

# Example usage:
num_array = [5, 2, 9, 3, 6, 1, 9, 8]
third_largest, last_largest = third_and_last_largest(num_array)
print("Third Largest: ",third_largest)
print("Last Largest ",last_largest)

# Third Largest:  6
# Last Largest  9

# Given a string and a non-negative int a, return a larger string that is n copies of
# the original string. 
# string_times(&#39;Hi&#39;, 2) → &#39;HiHi&#39;
# string_times(&#39;Hi&#39;, 3) → &#39;HiHiHi&#39;
# string_times(&#39;Hi&#39;, 1) → &#39;Hi&#39;

def string_times(input_string, n):
    return input_string * n

# Example usage:
original_string = "Hi"
n = 3
result_string = string_times(original_string, n)
print(result_string)

# HiHiHi

# Given an array of ints, return True if .. 1, 2, 3,.. appears in the array
# somewhere. 
# array123([1, 1, 2, 3, 1]) → True
# array123([1, 1, 2, 4, 1]) → False
# array123([1, 1, 2, 1, 2, 3]) → True

def array123(nums):
    nums_str = ''.join(map(str, nums))
    return '123' in nums_str

# Test cases
print(array123([1, 1, 2, 3, 1]))  # Should return True
print(array123([1, 1, 2, 4, 1]))  # Should return False
print(array123([1, 1, 2, 1, 2, 3]))  # Should return True

# True
# False
# Tru

# Given 3 int values, a b c, return their sum. However, if one of the values is the
# same as another of the values, it does not count towards the sum. 
# lone_sum(1, 2, 3) → 6
# lone_sum(3, 2, 3) → 2
# lone_sum(3, 3, 3) → 0

def lone_sum(a, b, c):
    if a != b and a != c and b != c:
        return a + b + c
    elif a == b == c:
        return 0
    elif a == b:
        return c
    elif a == c:
        return b
    elif b == c:
        return a

print(lone_sum(1, 2, 3))  
print(lone_sum(3, 2, 3)) 
print(lone_sum(3, 3, 3)) 

# 6
# 2
# 0

# Given a string you are provided with the possible operations.
# We can group the adjacent substrings, for e.g ABCABCBC can be compressed as 
# 2ABC1BC or 1ABCA2BC
# Among all the possible options, task is to find the resultant string with the
# minimum length.
# In case if there are multiple solutions return the lexicographically smallest string.
# So for the above example the solution would be 2ABC1BC
# Another example would be
# FLFLAFLAFLAF
# Solution: 1FLF3LAF

def compress_string(s):
    min_length = len(s)
    result = s

    for i in range(1, len(s) // 2 + 1):
        substring = s[:i]
        count = s.count(substring)
        compressed = f"{count}{substring}"

        compressed_string = s.replace(substring * count, compressed)
        
        if len(compressed_string) < min_length or (len(compressed_string) == min_length and compressed_string < result):
            min_length = len(compressed_string)
            result = compressed_string

    return result

# Test cases
print(compress_string("ABCABCBC"))  # Should return "2ABC1BC"
print(compress_string("FLFLAFLAFLAF"))  # Should return "1FLF3LAF"



# You are provided a string with only digits [0 - 9], your task is to count the
# number of subsequences of string divisible by 6.
# For e.g. The given string is 1234566
# The subsequences divisible by 6 are 12, 24, 36, 6, 6, 66
# Hence the answer should be 6

def count_subsequences_divisible_by_6(s):
    n = len(s)
    
    # Initialize a table to store counts of subsequences
    dp = [[0] * 2 for _ in range(n + 1)]

    # Initialize the base case
    dp[0][0] = 1  # Empty subsequence has a sum of 0
    dp[0][1] = 0

    for i in range(1, n + 1):
        digit = int(s[i - 1])
        
        # Calculate modulo 6 for the current digit
        mod6 = digit % 6

        # Copy counts from the previous row
        dp[i][0] = dp[i - 1][0]
        dp[i][1] = dp[i - 1][1]

        # Update counts based on the current digit
        if mod6 == 0:
            dp[i][0] += dp[i - 1][0] + 1
        elif mod6 == 2 or mod6 == 4:
            dp[i][1] += dp[i - 1][0]
        elif mod6 == 3:
            dp[i][0] += dp[i - 1][1] + 1
        elif mod6 == 5:
            dp[i][1] += dp[i - 1][1]

    # The final answer is stored in dp[n][0] (for subsequences divisible by 6)
    return dp[n][0]

# Test case
input_string = "1234566"
result = count_subsequences_divisible_by_6(input_string)
print(result)  # Should print 6

# Write a the function LongestWord (sen) take the sen parameter being passed and
# return the largest word in the string. If there are two or more words that are the
# same length, return the first word from the string with that length. Ignore
# punctuation and assume sen will not be empty.

import re

def LongestWord(sen):
    # Remove punctuation and split the string into words
    words = re.findall(r'\b\w+\b', sen)

    # Initialize variables to keep track of the longest word and its length
    longest_word = ""
    max_length = 0

    # Iterate through the words and find the longest one
    for word in words:
        word_length = len(word)
        if word_length > max_length:
            longest_word = word
            max_length = word_length

    return longest_word

# Test case
sentence = "Hello, this is a sample sentence!"
result = LongestWord(sentence)
print(result)  # Should print "sentence"


# Write a function AlphabetSoup(str) take the str string parameter being passed
# and return the string with the letters in alphabetical order (ie. hello becomes
# ehllo). Assume numbers and punctuation symbols will not be included in the
# string.

def AlphabetSoup(str):
    # Convert the string to a list of characters, sort it, and join it back to a string
    sorted_str = ''.join(sorted(str))
    return sorted_str

# Test case
input_str = "hello"
result = AlphabetSoup(input_str)
print(result)  # Should print "ehllo"
