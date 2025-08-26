# Modulazizing Your Code 1

# 1. Introduction to Modularity
# * What modular programming means
# * Why modularity is important (readability, reusability, debugging, teamwork)

# What is Modular Programming?

# * Modular programming is a way of writing programs by dividing them into smaller, independent, and reusable parts (moodules) instead of writing one long block of code.
# * A module can be a function, a class, or a Python file (.py) that performs a specific task.
# These modules can then be combined to build a complete program.
# In simple words, modular programming = breaking big problems into smaller, manageable solutions.

# Why Modularity is Important

# * 1. Readability
# * Breaking code into smaller modules makes it easier to read and understand.
# * Instead of scrolling through hundreds of lines inside a file, you can just put them in different files within a folder and look at the specific file that has the codes you need.

# * 2. Reusability
# * Once you create a module, you can reuse it in different programs.
# * For example, A function that calculates the area of a circle can be used in a school project, an engineering project, or even in a game.

# * 3. Debugging and Maintenance
# * If there's an error, you only need to check the specific module where the problem is, instead of combing through the whole program.
# * Updating or improving one module doesn't break the rest of the system.
# * Lets say, you are building a banking application. If the payment module in the app has a bug, the user login module is unaffected.


# 4. Teamwork and collaboration
# * In real-world projects, different developers can work on different modules simultaneously.
# * Later, all modules are combined into the main project.
# * For example, In building a school management system.
#   * One developer handles student records
#   * Another handles teacher records
#   * Another handles payment system

# All parts are then combined to make one big system.


# Let's Put things in perspective

#   * Imagine we are planning a wedding event. If one person tries to do everything (cook, decorate, handle invitations, music, photography), itbecomes chaotic or nearly impossible.

#   * Instead, tasks are divided:
#       * The caterer handles food
#       * The decorator handles decoration
#       * The DJ handles music
#       * The photographer handles pictures
#   * At the end, when everyone brings their contribution together, the event runs smoothly.
#   * This is exactly how modular programming works in coding. Each part (module) does it's job, and together they form the complete program


#_Do you understand?_

# 2. Functions (first level of modularity)
#   * Definition of a function
#   * Defining and calling functions
#   * Function parameters and arguments
#   * Return values
#   * Use cases (math operations, repeated tasks, formatting output)

# Definition of a Function
#   * A function is a block of organized, reusable code that performs a single specific task. In python, we have the inbuilt functions, the user defined functions and lambda function(which is also a type of user defined function)

# Python Built-in Functions
#   * Built-in functions are functions that come pre-installed with Python. You don't need to import any library to use them. They are always available, just like how a phone comes with default apps (calculator, messages, clock.). And you have used some o fthem without even knowing.

# Common Categories of Built-in Functions.
# 1. Input and Output Functions
#   print() # Displays output.
#   input() # Takes user input.

# 2. Type Conversion Functions
#   * int(), float(), str(), bool(), list(), dict(), tuple(), set()

# 3. Mathematical Functions

# abs() # Absolute value

# pow(x, y) # x raised to power y
# round() # Round numbers to the defined decimal places
# min(), max() # Find smallest/largest

# 4. Sequences and Collection Functions

# len() # Length of a sequence
# sum() # Sum of elements
# sorted() # Sort items
# enumerate() # Track index and value

# 5. Utility Functions
# type() # Shows the type of an object(variables, datatypes, data structures, functions, classes)

# id() # Returns unique ID of object in memory
# help() # Documentation about an object

# 6. Special Built-ins
# range() # Generates a sequence of numbers
# zip() # Combines two lists element by element
# map() # Applies a function to all elements in a sequence
# filter() # Filters elements in a sequence based on condition

# See Examples of use here

# range()

for i in range(3):
    print(i) # 0, 1, 2


# zip()
names = ["Esther", "Precious", "Kennie", "Ope", "Sherif", "Mumu"]
scores = [85, 90, 75, 74, 48, 47]
for n, s in zip(names, scores):
    print(n, "scored", s)

# It's Ok, if you don't kmow what lambda is or how to use it. I will touch on it later. Just focus on the outputs
# map()

nums = [1, 2, 3, 4]
squared = list(map(lambda x: x**2, nums))
print(squared) # [1, 4, 9, 16]

# filter()
even_nums = list(filter(lambda x : x % 2 == 0, nums))
print(even_nums)  # [2, 4]


# Take a long look at the code below, please.

# Student performance and Feedback system

#Step 1: Input student data
name1 = input("Enter first student name: ")
score1 = int(input("Enter score for " + name1 + ": "))

name2 = input("Enter second student name: ")
score2 = int(input("Enter score for " + name2 + ": "))

name3 = input("Enter third student name: ")
score3 = int(input("Enter score for " + name3 + ":"))


# Step 2: Store in lists
names = [name1, name2, name3]
scores = [score1, score2, score3]

# Step 3: Display data
print("\nStudent Data:")
for index, (n, s) in enumerate(zip(names, scores)):
    print(f"{index + 1}. {n} - {s}")


# Step 4: Summary using built-ins
total = sum(scores)
average = round(total / len(scores), 2)
highest = max(scores)
lowest = min(scores)

print("\nPerfromance Summary:")
print("Total Score:", total)
print("Average Score:", average)
print("Highest Score:", highest)
print("Lowest Score:", lowest)

# Step 5: Ranking (using sorted and zip)
ranked = sorted(zip(scores, names), reverse=True)
print("\nRanking:")
for rank, (score, name) in enumerate(ranked, 1):
    print(f"{rank}. {name} - {score}")


# Step 6: Check data types
print("\nData Type Checks:")
print("Type of names:", type(names))
print("Type of scores:", type(scores))
print("ID of names list: ", id(names))
print("ID of scores list:", id(scores))

# Step 7: Filter passing students (>=50)
passing = list(filter(lambda s : s >= 50, scores))
print("\nPassing Scores:", passing)

# Step 8: Map names to uppercase
upper_names = list(map(lambda n: n.upper(), names))
print("Uppercase Names:", upper_names)

# Step 9: USe help() to show documentation of len
print("\nHelp on len():")
help(len)


# # I just made use most of the built-in functions. You can write your own version of this code. Just think through it.

# # ValueError
# cell In[10], line5
#     1 # Student performmance & Feedback System
#     2 
#     3 # Step 1: Input student data
#     4 name1 = input("Enter first student name: ")



# User Defined Function

#   * Instead of writing the same code again and again, we put it inside a function and just call it whenever we need it.
#   * SO functions make programs cleaner, shorter, and easier to manage.
#   * Now, I need you to think of a function like a machine in a factory.
#       * You put something in(input),
#       * The machine works on it (process),
#       * Then gives you something out (output).

#   * In Python, we use the def keyword to define a function. Then we call the function whenever we want to use it.
#   * Lets see the function structure

# def function_name(takes in imnput):
#     process block
#     output block

#   * More explanation
# def function_name(input - here, you will insert an item or list of what the function will need to work):
#     "proces block -here will contain the logic or what you want the function to do"
#     "output - Then here will contain what you want the function to ouput. You can either use the 'return' keyword or 'print()' or 'yield'"

# Defining a function
def greet():
    print("Hello, welcome to AI Fellowship!")

# When you want to use a function, this is how to call it.
# And you can call it as many times as possible.
greet()
greet()
greet()

# Function Arguments and Parameters
# * Arguments are variables you add inside the function parenthesis when defining the function (placeholders). Sometimes, they can be optional.
# * Paramters are the actual values you pass inside the function parenthesis when calling the function.


# Function with an argument - the placeholder

def greet(name):
    print("Hello", name, "Welcome to Python learning!")


# Calling with paramter- the actual name
greet("Class rep")
greet("Ridwan")


# When to Use return, print(), and yield keywords inside a function

# * a. print()
# * You can use it if you are just interested in displaying your output (Not Storing). It does not give back a value you can use later.

# Think of it like shouting information out loud, but not recording it for reference purpose.
# * So you use it when you just want to show the results to the user. Example: printing menus, reports, or logs.

def greet(name):
    print("Hello", name)


# Function call
result = greet("Esther")

# You will notice that it did not store the name
print("Result:", result)

# b. return
# * You cam use it if you want to give back a value
# * return sends a value back to the function caller.
# * The function ends immediately once it hits return
# * Think of it like filling a form and handling it back, the caller now owns the result and can reuse it.
# So you can use return when you need the result for further computation or storage. For example, mah=th calculations, data processing, formatting text.


def add(a, b):
    return a + b

# Function call

result = add(4, 6)
print("The sum is:", result)

# Note the output and compare it with that of print()


# 3. yield
# - This is used for producing a sequence (Generators)
#   * yield works like return, but instead of ending the function, it pauses it and remembers its state.
#   * Next time you call it, it returns from where it stopped.
#   * This creates a generator.
#   You can use it when working with large data or infinite sequences.


def count_up_to(n):
    i = 1
    while i <= n:
        yield i   # pause and return i
        i += 1

# Using the generatoir
for number in count_up_to(5):
    print(number)

# Note the output: Instead of giving all numbers at once, the function yields them one at a time.
# 1
# 2
# 3
# 4
# 5


# More on Function Arguments(Types of Arguments)
#   * Functions can accept different types of arguments depending on how we want to pass data. Understanding these makes functions flexible and powerful.

# 1. Positional Arguments
#   * These are the most common.
#   * The order matters: value are assigned to parameters in the same order as they appear.
#   * Think of it like lining up children in the same order as roll call.


def introduce(name, track):
    print("My name is", name)
    print("I am learning", track, ".")


# function call
introduce("Ngozi")