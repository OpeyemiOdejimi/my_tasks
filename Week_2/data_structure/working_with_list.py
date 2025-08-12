# Data Structures Continued... 2
# List

# A list in Python is an ordered, mutable(changeable) collection that can store different types of data that is, numbers, strings, booleans, even other lists.

# How to Create a list
# * You caan create an empty list when you don't have elements yet but plan to add later.

# Method 1: Using square brackets

empty_list = []
print(empty_list) # Output: []

# Method 2: Usng the list () constructor

empty_list2 = list()
print(empty_list2) # Output: []

# * Creating a List with initial Elements
#   * Lists can store multiple items separated by commas inside sqaure brackets

# List of strings

fruits = ["apple", "banana", "Cherry"]
print(fruits)

# List of integers

numbers = [1, 2, 3, 4, 5]
print(numbers)

# Mixed data types

mixed_list = ["Alice", 25, 5.8, False]
print(mixed_list)

# * Creating a List from Another Sequence. You can convert strings, tuples, or other iterables into a list.

# From a string (each character becomes an element)

chars = list("Hello")
print(chars)

# From a tuple

# Briefly, tuples are lists that are immutable (i.e), they cannot be changed like list.

my_tuple = (10, 20, 30)
list_from_tuple = list(my_tuple)
print(list_from_tuple)

# From a range

# numbers_range = list(range(5)) 
# print(numbers_range) # Output: [0, 1, 2, 3, 4]

#   *  Creating a List Using List Comprehension. List comprehensions are a concise way to create lists using a loop in one line. We will come back to this later

# Squares of numbers 0-4

squares = [x**2 for x in range(5)]
print(squares) # Output: [0, 1, 4, 9, 16]

# Even numbers between 0-10
evens = [x for x in range(11) if x % 2 == 0]
print(evens)

# * Creating a Nested List. A list can contain other list. It is useful for matrices or grouped data.

# Matrix-like list

# Matrix in Python is a list of list

matrix = [[1, 2], [3, 4], [5, 6]]
print(matrix)

# Accessing elements in a nested list
print(matrix[2])     # Output: [1, 2]
print(matrix[2][0])  # Output: 2


# Characteristics of a list
# 1. Ordered Collection
#   * The elements in a list maintain the order in which they are inserted.
#   * The first element has index 0, the second has index 1, and so on.

fruits = ["mango", "orange", "banana"]
print(fruits)
print(fruits[0])
print(fruits[2])


# 2. Allows Duplicates
#  * Lists can store the same value multiple times

items = ["rice", "beans", "yam", "rice"]
print(items)

# 3. Mutable (Can be changed)
# * You can modify a list after it's created - changed elements, add new ones, or remove existing ones.

numbers = [1, 2, 3]
numbers[2] = 20
print(numbers)

# 4. Can Contain Different Data Types
#    * A list can hold integers, strings, floats, booleans, and other lists

mixed = [10, "Nigeria", 3.14, True]
print(mixed)