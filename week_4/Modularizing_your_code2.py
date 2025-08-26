# Modularizing Your Code 2

# 3. Python Modules
#   * What a module is (a.py file that can be resued)
#   * Importing built_in modules (math, random, datetime)
#   * Writng your own module (creating my_module.py and importing it)
#   * Aliasing modules (import numpy as np)


# What is a Module?
#   * A module in Python is simply a file with .py extension that contains Python code (functiomns, variables, or classes) whoich can be reused in other programs.
#   * Instead opf writing the same code again and agaoin, you can write it once in a module and then import it anywhere.
#   * Lets think of a module as a toolnbox. Each tool (function, variables, or classes) which can be reused in other programs.


# * Importing Built-in Modules

# * Python already comes with many pre-built modules that you canuse directly.
# * Some common examples are:
# * math -for mathematical operations
# * random - for generating random numbers
# * datetime - for working  with datesand time.
# etc.
# To use built in modules, you have to load them into your environment, that is, import them.


# Duiferent Ways to Import Modules

#1. Import the whole module

import math

# Lets put it to use

print(math.sqrt(9))
# - Note that you must specify the module name when calling a function within it.

'''
TypeError
call In[4], line 8
      3 import math
      6 # Lets put it to use
----> 8 print(math.sqrt())
      9 # - Note that you must specify the module name when calling a function within it.

TypeError: math.sqrt() takes exactly one argument (0 given)

'''

# 1. import as an alis

import math as m

# lets put it to use

print(m.sqrt(25))

# - This shirten the module name, this is common with libaries like numpy, pandas, etc

# 3. Import specific functions or variables

from math import sqrt, pi
print(sqrt(36))

# - here you don't need the prefix 'math.' anymore

# 4. Import everything from the module

from math import *

print(sqrt(49))
print(pi)

# - This is usually not recommended because it can cause name conflicts if two modules have functions with same name

# Writing Your Own Module
# - step1: Create a folder. Name it my_module
# - step2: Create a file inside the folder. Name it first.py
# - step3: Create another file inside the same folder. Name it second.py
# - step4: Create another file still inside inside the same folder. Name it main.py

# - here is the fok=lder structure

'''
project_folder/
│
├── my_module/
│   ├── first.py
│   ├── second.py
│   └── main.py

'''
#- Note that anyone with forward slash is a folder while the ones with extensions are the files.

# my_module/first.py

def add(a, b):
    return a + b

def subtract(a, b):
    return a - b

def multiply(a, b):
    return a * b

def divide(a, b):
    if b != 0:
        return a / b
    else:
        return "Cannot divide by zero"
    


# my_module/second.py


def greet(name):
    return f"Hello, {name}! I am creating my own module"

def reverse_string(string):
    return string[::-1]

def count_characters(string):
    return len(string)

def count_words(string):
    return len(string.split())



# my_module/main.py

import first
import second

# lets use the functions in the first.py file

print("=== Math Functions ===")
print("5 + 3 =", first.add(5, 3))
print("10 - 4 =", first.subtract(10, 4))
print("6 * 7 =", first.multiply(6, 7))
print("20 / 5 =", first.divide(20, 5))

# lets use the functions in the second.py file
print("\m=== String Functions ===")
print(second.greet("Ridwan"))
print("Reverse of 'Python' =", second.reverse_sr