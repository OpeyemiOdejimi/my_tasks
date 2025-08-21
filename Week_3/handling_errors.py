# Handling Errors in Python
#  * Errors in Python are classified into three main categories:
# 1. Syntax Errors
# 2. Runtime Errors
# 3. Semantic Errors


# Syntax Errors
# * It occur when the Python interpreter cannot understand your code because it breaks Python grammer rules.
# * Please note that Program will not run until the error is fixed.


# Common Subtypes of Syntax Errors
# a. IndentationError - Incorrect spacing

for i in range(3):
    print(i)  # Wrong indentation

# This will through error except you fix the indentation

# cell In[2], line 2
#   print(i)  # Wrong identation

# IndentationError: expected an indented block after 'for' statement on line 1

# b. Missing Colon/Parenthesis Error

if 5 > 3: # Missing colon
    print("Hello")

# c. Invalid Syntax - General grammar mistakes.

print ("Hello") # Missing parentheses in Python 3

# To fix: Double check Python grammer, colons, parentheses, and identation.


# 2. Runtime Errors

# * The program is syntactically correct, but an error occurs while it is running.
# * These are also called exceptioms.
# * They can be handled with try, except, and finally.

# Common Subtypes of Runtime Errors
# a. ZeroDivisionError - Dividing by zero.

x = 10 / 0 # This will throw error

# b. NameError - Using a variable before defining it.

print(age) # age not defined

# c. TypeError - Wrong data type in an operation.

result = "10" + 5 # str + int not allowed

# d. ValueError - Invalid value for a function

number = int("abc") # cannot conveert string to int


# e. IndexError - Accessing list index out of range.

fruits = ["apple", "banana"]
print(fruits[3])  # Index out of range


# f. KeyError - Accessing a dictionary with a missing key.

data = {"name": "Ada"}
print(data["age"]) # Key not found

# g. FileNotFoundError - File does not exist.

f = open("missing.txt") # File not found

# Handling Runtime Errors

# * Python provides exception handling to prevent programs from crashing when unexcepted errors occur.

# The keywords used are;
#  * a.try - block of code to test for errors.
#  * b. except - block of code that runs if an error occurs.
#  * c. finally - block of code that always runs (whether error occurs or not).

# The try Block
# * It is used to wrap code that might raise an error.
# * If no error occurs Python skips the except block.

try:
    x = 10 / 2
    print("Result:", x)


# The except Block

# * It defines what to do if an error occurs inside try.
# * It can catch specific errors or all errors.


# This is apecific exception

try:
    x = 10 / 0
except ZeroDivisionError: 
    print("Cannot divide by zero.")

# This is a case of mulyiple exception

try:
    number = int("abc") # ValueError
    result = 10 / 0 # zereoDivisionError
except ValueError:
    print("Invalid conversion to integer.")

except ZeroDivisionError:
    print(" Cannot divide by zero.")
